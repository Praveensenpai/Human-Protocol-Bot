import asyncio
from contextlib import suppress
from datetime import datetime, timedelta, timezone
import random
import time
import traceback
from typing import Any
from env import Env
from humanproto.human import HumanProtocol
from utils.dt import iso_to_datetime
from utils.loggy import logger
from timecalculator import TimeCalculator


class HumanProtocolBot:
    def __init__(self, concurrency: int = 1) -> None:
        self.semaphore = asyncio.Semaphore(concurrency)

    async def xinterval_claim_task(
        self, human: HumanProtocol, user_info: dict[str, Any]
    ):
        try:
            logger.info(f"Starting claiming task for user: {user_info['username']}")
            last_claimed_at = iso_to_datetime(user_info["last_claimed_at"])
            time_difference = datetime.now(timezone.utc) - last_claimed_at
            threshold = timedelta(hours=2)
            if time_difference <= threshold:
                remaining_time = threshold - time_difference
                hours, remainder = divmod(remaining_time.seconds, 3600)
                minutes = remainder // 60
                logger.info(
                    f"Please wait {hours} hours and {minutes} minutes before claiming again."
                )
                await asyncio.sleep(remaining_time.total_seconds())
                logger.info("Time's up! You can now claim again.")

                extra_minutes = timedelta(
                    minutes=random.randint(
                        Env.RANDOM_EXTRA_DELAY_MIN_MN, Env.RANDOM_EXTRA_DELAY_MAX_MN
                    )
                )
                logger.info(
                    f"Adding an extra wait of {extra_minutes} minutes before claiming."
                )
                await asyncio.sleep(extra_minutes.total_seconds())
                logger.info("Extra wait time is over. You can now claim!")
            else:
                logger.info("More than 2 hours have passed. You're good to claim!")

            logger.info(f"Claiming for user: {user_info['username']}")

            async with self.semaphore:
                logger.info("Starting Daily Claim")
                await human.xclaim.xclaim()
                logger.info("Daily Claim Completed")
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.error(f"An unexpected error occurred: {e}")

    async def main(self):
        while True:
            try:
                human = HumanProtocol("imhmnbot")
                user_info = await human.login()
                if not user_info:
                    return

                tasks = [self.xinterval_claim_task(human, user_info)]
                await asyncio.gather(*tasks)

                logger.info(
                    f"Rest Period: Sleepng for {TimeCalculator.HOUR *  0.25} seconds"
                )
                await asyncio.sleep(TimeCalculator.HOUR * 0.25)
            except Exception as e:
                logger.error(f"An unexpected error occurred: {e}")
                logger.error(traceback.format_exc())
                logger.info(f"Sleepng for {TimeCalculator.HOUR * 1} seconds")
                await asyncio.sleep(TimeCalculator.HOUR * 1)

    def run(self):
        while True:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            try:
                loop.run_until_complete(self.main())
            except Exception as e:
                logger.error(traceback.format_exc())
                logger.error(f"Restarting event loop due to error: {e}")
            finally:
                with suppress(Exception):
                    loop.close()
                logger.info("Restarting the main loop...")
                time.sleep(10)


if __name__ == "__main__":
    HumanProtocolBot().run()

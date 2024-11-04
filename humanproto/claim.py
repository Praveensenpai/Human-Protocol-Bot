import httpx
from humanproto.endpoints import Endpoints
from utils.loggy import logger


class XClaim:
    def __init__(self, http_client: httpx.AsyncClient):
        self.http_client = http_client

    async def xclaim(self) -> bool:
        response = await self.http_client.post(Endpoints.CLAIM_POINTS)
        if response.status_code == 200:
            if response.json().get("success"):
                logger.info("Daily Claim Successful")
                return True
        return False

from typing import Any
import httpx
from loguru import logger
from humanproto.endpoints import Endpoints
from telegram.client import TGClient
from humanproto.claim import XClaim
from fake_useragent import UserAgent
from env import Env
from telegram.platform import Platform


class HumanProtocol:
    def __init__(
        self,
        peer_id: str,
        http_timeout: float = 60 * 2,
        platform: Platform = Platform.ANDROID,
    ):
        self.peer_id = peer_id
        self.http_client = httpx.AsyncClient(
            timeout=http_timeout,
            headers={
                "User-Agent": UserAgent(os=platform.value).random,
            },
        )
        self.xclaim = XClaim(self.http_client)

    async def login(self) -> dict[str, Any]:
        self.http_client.headers.pop("Authorization", None)
        tg_client = TGClient()
        query = await tg_client.get_query_string(self.peer_id, short_name="invite")
        response = await self.http_client.get(
            Endpoints.LOGIN,
            params={"refCode": Env.REF_ID},
            headers={"Authorization": f"Bearer {query}"},
        )

        access_token = response.json().get("token", "")
        if access_token:
            self.http_client.headers["Authorization"] = f"Bearer {access_token}"
            logger.success("Human Protocol Login successful")
            return response.json().get("user")
        raise Exception("Unable to login")

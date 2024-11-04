from typing import Final


class Endpoints:
    _API: Final[str] = "https://api.imhmn.xyz/v1"
    CLAIM_POINTS: Final[str] = f"{_API}/me/claim-coin"
    LOGIN: Final[str] = f"{_API}/user"

from pyenvloadermeta import EnvLoaderMeta


class Env(metaclass=EnvLoaderMeta):
    REF_ID: str
    SESSION_NAME: str
    API_ID: int
    API_HASH: str
    PHONE: str
    RANDOM_EXTRA_DELAY_MIN_MN: int
    RANDOM_EXTRA_DELAY_MAX_MN: int

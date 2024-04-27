class Config:
    SETTINGS = {
        "PROD": {
            "base_url": "https://ord.ozon.ru",
            "api_key": "api_key_production",
            "bucket": "media",
        },
        "TEST": {
            "base_url": "https://ord-sandbox.ozon.ru",
            "api_key": "api_key_production",
            "bucket": "media",
        },
    }

    @classmethod
    def set_api_key(cls, key: str, environment: str = "PROD"):
        cls.SETTINGS[environment]["api_key"] = key

    @classmethod
    def set_base_url(cls, url: str, environment: str = "PROD"):
        cls.SETTINGS[environment]["base_url"] = url

    @classmethod
    def set_bucket(cls, bucket: str, environment: str = "PROD"):
        cls.SETTINGS[environment]["bucket"] = bucket

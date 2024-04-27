import requests
from pathlib import Path
from requests.exceptions import RequestException
from tempfile import NamedTemporaryFile
from shutil import copyfileobj
from .config import Config
from .models import (
    FileUrl,
    ErrorResponse,
)


class OzonORDClient:
    """Базовый класс клиента для взаимодействия с API Ozon ORD."""

    _environment = "PROD"

    @classmethod
    def set_environment(cls, environment):
        cls._environment = environment

    @classmethod
    def get_base_url(cls):
        """Получение базового URL из конфигурации для указанного окружения."""
        return Config.SETTINGS[cls._environment]["base_url"]

    @classmethod
    def get_api_key(cls):
        """Получение API ключа из конфигурации или установленного значения."""
        return Config.SETTINGS[cls._environment]["api_key"]

    @classmethod
    def get_bucket(cls):
        """Получение значения bucket из конфигурации для указанного окружения."""
        return Config.SETTINGS[cls._environment]["bucket"]

    @classmethod
    def get_headers(cls):
        """Формирование заголовков для запроса."""
        api_key = cls.get_api_key()
        return {"Authorization": f"Bearer {api_key}"}

    @classmethod
    def request(
        cls,
        method,
        endpoint,
        data=None,
        files=None,
        headers=None,
        raw_response=False,
    ):
        """Отправка HTTP запроса к API."""
        base_url = cls.get_base_url()
        url = f"{base_url}{endpoint}"
        request_headers = cls.get_headers()
        request_headers.update(headers or {})
        if not files:
            request_headers["Content-Type"] = "application/json"

        try:
            response = requests.request(
                method, url, headers=request_headers, json=data, files=files
            )
            response.raise_for_status()
            if raw_response:
                return response
            else:
                if "error" in response.text:
                    return ErrorResponse.model_validate_json(response.text)
                return response.text
        except requests.exceptions.HTTPError as e:
            return f"HTTP error occurred: {str(e)}"
        except requests.exceptions.ConnectionError as e:
            return f"Connection error occurred: {str(e)}"
        except requests.exceptions.Timeout as e:
            return f"Timeout error occurred: {str(e)}"
        except RequestException as e:
            return f"An error occurred during the request: {str(e)}"
        except Exception as e:
            return f"An error occurred: {(e)}"

    @staticmethod
    def extract_filename_and_extension(url: FileUrl):
        """Получаем название файла из file_url."""
        path = Path(url.path)
        filename = path.name  # file-name.webp
        extension = path.suffix  # .webp
        return filename, extension

    @classmethod
    def upload_file(cls, bucket, file_url):
        filename, extension = cls.extract_filename_and_extension(file_url)
        full_filename = str(filename)
        if not extension:
            extension = ".bin"
            full_filename = f"{filename}{extension}"
        response = requests.get(file_url, stream=True)
        response.raise_for_status()
        with NamedTemporaryFile(delete=False) as tmp_file:
            copyfileobj(response.raw, tmp_file)
            tmp_file.seek(0)
            with open(tmp_file.name, "rb") as file_for_upload:
                files = {
                    "file": (
                        full_filename,
                        file_for_upload,
                        response.headers["Content-Type"],
                    )
                }
                endpoint = f"/api/external/file/{bucket}"
                return cls.request("POST", endpoint, cls._environment, files=files)

import re

from .client import OzonORDClient
from .models import (
    FileUploadData,
    FileUploadResponse,
    FileDownloadResponse,
)


class File(OzonORDClient):
    """Класс для работы с файлами в API Ozon ORD."""

    @classmethod
    def upload(cls, upload_data: FileUploadData) -> FileUploadResponse:
        """Метод для загрузки файла."""
        response = cls.upload_file(upload_data.bucket, upload_data.file_url)
        return FileUploadResponse.model_validate_json(response)

    @staticmethod
    def get_filename(content_disposition):
        """Получаем название файла из значения filename в Response Headers."""
        match = re.search(r'filename="?([^";]+)"?', content_disposition)
        if match:
            return match.group(1)
        return None

    @classmethod
    def download(cls, file_id: int) -> FileDownloadResponse:
        """Метод для скачивания файла."""
        endpoint = f"/api/external/file/{file_id}"
        response = cls.request("GET", endpoint, raw_response=True)
        filename = cls.get_filename(response.headers["Content-Disposition"])

        if response.status_code == 200:
            if not filename:
                filename = f"file-{file_id}.bin"
            return FileDownloadResponse(content=response.content, filename=filename)
        else:
            return FileDownloadResponse(
                error=f"Failed to download file: {response.status_code} {response.text}"
            )

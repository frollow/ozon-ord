from ozon_ord.file import File
from ozon_ord.models import FileUploadData

# Загрузка файла
upload_data = FileUploadData(
    file_url="https://resizer.mail.ru/p/6435849f-0ad2-5e31-a868-2aacb1946526/AQAGN3txpeH1ISw5hn05IJE676eq1wLhEdG_C9FeDVTV2qCKRXXgn2qEo1q4CqfJnerbdxIKX9ROyPeNS_DPTVf1wLQ.webp",
    bucket="media",
)
try:
    response = File.upload(upload_data)
    print(response)
    print(response.id)
except Exception as e:
    print("Ошибка при загрузке файла:", str(e))

# Скачивание файлов
file_id = 403603  # ID файла, который нужно скачать
download_response = File.download(file_id)

if download_response.error is None:
    with open(download_response.filename, "wb") as f:
        f.write(download_response.content)
    print(f"Файл успешно скачан и сохранен как {download_response.filename}.")
else:
    print("Ошибка при скачивании файла:", download_response.error)

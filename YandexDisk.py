import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path):
        """Метод загружает файл file_path на Яндекс.Диск"""
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        filename = file_path.split('/', )[-1]
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        params = {"path": f"Загрузки/{filename}", "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params).json()
        href = response.get("href", "")
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        # Проверяем статус
        if response.status_code == 201:
            return 'Успешно'
        else:
            return f"Ошибка загрузки! Код ошибки: {response.status_code}"


if __name__ == '__main__':
    path_to_file = 'C:/Users/Compumar/Desktop/HW_Object/info.txt'
    token = ''
    uploader = YaUploader(token)
    # Загружаем на диск
    print(f"Загружаем файл {path_to_file.split('/', )[-1]} на Яндекс.Диск")
    result = uploader.upload(path_to_file)
    print(result)
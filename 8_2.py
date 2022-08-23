from urllib import response
import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        
    def _get_upload_link(self, disc_file_path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disc_file_path, 'overwrite': 'true'}
        response = requests.get(url, headers=headers, params=params)
        return response.json()
    
    def upload(self, file_path: str, filename: str):
        href = self._get_upload_link(disc_file_path=file_path).get('href', '')
        response = requests.put(href, data=open(filename, 'rb'))
        if response.status_code == 201:
            print('Success!')

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'to_upload.txt'
    filename = 'to_upload.txt'
    token = '' #your authorization token
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file, filename)

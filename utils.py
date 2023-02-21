import os
import json
from pprint import pprint

from googleapiclient.discovery import build

'''Импорты'''


class Channel:
    """Класс, экземпляры которого инициализируют id конкретного ютуб-канала."""

    def __init__(self, channel_id):

        """Инициализация"""
        self.__channel_id = channel_id

        api_key: str = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        self.channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

        json_channel = json.dumps(self.channel, indent=2, ensure_ascii=False)
        json_load = json.loads(json_channel)
        self.title = json_load['items'][0]['snippet']['title']
        self.description = json_load['items'][0]['snippet']["description"]
        self.url = f'https://www.youtube.com/channel/{self.__channel_id}'
        self.subscriberCount = json_load['items'][0]["statistics"]["subscriberCount"]
        self.video_count = json_load['items'][0]["statistics"]["videoCount"]

    def to_json(self, file):
        with open(file, "w", encoding="UTF-8") as f:
            json_channel = json.dumps(self.channel, indent=2, ensure_ascii=False)
            f.write(json_channel)

    def print_info(self):
        """Выводит в консоль информацию о канале"""
        pprint(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @property
    def channel_id(self):
        return self.__channel_id

    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

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
        """Запись в json-файл"""
        with open(file, "w", encoding="UTF-8") as f:
            json_channel = json.dumps(self.channel, indent=2, ensure_ascii=False)
            f.write(json_channel)

    def print_info(self):
        """Выводит в консоль информацию о канале"""
        pprint(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @property
    def channel_id(self):
        """Возврат id-канала"""
        return self.__channel_id

    @staticmethod
    def get_service():
        """Возврат API-канала"""
        api_key: str = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def __str__(self):
        return f'{json_channel}'

    def __add__(self, other):
        if isinstance(other, Channel):
          return self.subscriberCount + other.subscriberCount
        else:
          raise ValueError('Не правильный формат')

'''
Реалузуйте возможность складывать два канала и сравнивать их на больше/меньше между собой. Сложение и сравнение идет по количеству подписчиков.'''
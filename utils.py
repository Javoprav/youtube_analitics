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
        """Вывод через информации о канале"""
        return f'Youtube-канал: {self.title}'

    def __add__(self, other):
        """Сложение кол-ва подписчиков"""
        if isinstance(other, Channel):
            return self.subscriberCount + other.subscriberCount
        else:
            raise ValueError('Не правильный формат')

    def __lt__(self, other) -> bool:
        """Сравнение"""
        if isinstance(other, Channel):
            return self.subscriberCount > other.subscriberCount
        else:
            raise ValueError('Не правильный формат')

    def __gt__(self, other) -> bool:
        """Сравнение"""
        if isinstance(other, Channel):
            return self.subscriberCount < other.subscriberCount
        else:
            raise ValueError('Не правильный формат')


class Video:
    """Класс видео, инициализируется по ID"""
    def __init__(self, id_video):
        self.id_video = id_video
        api_key: str = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        request = youtube.videos().list(part="snippet,statistics", id=id_video)
        response = request.execute()
        self.title = response['items'][0]['snippet']['title']
        self.viewCount = response['items'][0]['statistics']['viewCount']
        self.likeCount = response['items'][0]['statistics']['likeCount']

    def __str__(self):
        """Выводит название видео"""
        return self.title


class PLVideo(Video):
    """Класс плейлиста видео, инициализируется по ID видео и айдишником плейлиста, в котором он находится."""
    def __init__(self, id_video, playlist_id):
        super().__init__(id_video)
        self.id_plv = playlist_id
        api_key: str = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        self.playlist = youtube.playlists().list(id=playlist_id, part='snippet').execute()
        self.playlist_name = self.playlist['items'][0]['snippet']['title']
        # self.playlist_name = self.playlist['items'][0]['snippet']['title']


video1 = Video('9lO06Zxhu88')
video1 = Video('9lO06Zxhu88')
video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
pprint(video2.playlist)
print(video1)
# Как устроена IT-столица мира / Russian Silicon Valley (English subs)
print(video2)
# Пушкин: наше все? (Литература)
# шаблон: 'название_видео (название_плейлиста)'
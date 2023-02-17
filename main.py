import os
import json
from googleapiclient.discovery import build
'''Импорты'''

class Channel:
    """Класс, экземпляры которого инициализируют id конкретного ютуб-канала."""
    def __init__(self, channel_id):
        """Инициализация"""
        self.channel_id = channel_id

        api_key: str = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        self.channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

    def print_info(self):
        '''Выводит в консоль информацию о канале'''
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))


channel1 = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
print(channel1.print_info())
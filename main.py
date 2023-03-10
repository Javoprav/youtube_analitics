from utils import *


def main():
    vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')

    # получаем значения атрибутов
    pprint(vdud.title)
    # вДудь
    print(vdud.video_count)
    # 163
    print(vdud.url)
    # https://www.youtube.com/channel/UCMCgOm8GZkHp8zJ6l7_hIuA
    # менять не можем
    # vdud.channel_id = 'Новое название'
    # print(vdud.channel_id)
    # AttributeError: property 'channel_id' of 'Channel' object has no setter
    # можем получить объект для работы с API вне класса

    print(Channel.get_service())
    # <googleapiclient.discovery.Resource object at 0x000002B1E54F9750>

    # создать файл 'vdud.json' c данными по каналу
    vdud.to_json('vdud.json')

    print(vdud)
    # Youtube-канал: вДудь

    red = Channel('UC1eFXmJNkjITxPFWTy6RsWg')
    print(vdud.subscriberCount)
    print(red.subscriberCount)
    print(vdud > red)
    # True
    print(vdud < red)
    # False
    print(vdud + red)
    # 13940000

    video1 = Video('9lO06Zxhu88')
    video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
    print(video1)
    # Как устроена IT-столица мира / Russian Silicon Valley (English subs)
    print(video2)
    # Пушкин: наше все? (Литература)
    # шаблон: 'название_видео (название_плейлиста)'
    pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
    print(pl.title)
    # Редакция. АнтиТревел
    print(pl.url)
    # https://www.youtube.com/playlist?list=PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb
    duration = pl.total_duration
    print(duration)
    # 3:41:01
    print(type(duration))
    # <class 'datetime.timedelta'>
    print(duration.total_seconds())
    # 13261.0
    print(pl.show_best_video())
    # https://youtu.be/9Bv2zltQKQA

    broken_video = Video('broken_video_id')
    print(broken_video.title)
    # None
    print(broken_video.likeCount)
    # None


if __name__ == "__main__":
    main()

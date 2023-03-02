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



if __name__ == "__main__":
    main()

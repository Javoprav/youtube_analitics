import pytest
from main import *
from tests.conftest import test_data


def test_print_info():
    """Проверка получения инфо о канале"""
    channel_1 = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    assert channel_1.print_info() is None
    assert print(channel_1.print_info()) == print(test_data)


def test_to_json():
    """Проверка получения json-файла"""
    channel_1 = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    assert channel_1.to_json('vdud.json') == print(test_data)


def test_channel_id():
    """Проверка получения id"""
    vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    assert print(vdud.channel_id) is None
    assert vdud.channel_id == 'UCMCgOm8GZkHp8zJ6l7_hIuA'


'''def test_get_service(): ########## не проверяется
    """Проверка возврата id"""
    channel_2 = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    assert str(channel_2.get_service()) == str'''


def test___str__():
    """Проверка вывода str"""
    channel_3 = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    assert channel_3.__str__() == 'Youtube-канал: вДудь'


def test___add__():
    """Проверка соединения"""
    channel_4 = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    red_1 = Channel('UC1eFXmJNkjITxPFWTy6RsWg')
    assert channel_4 + red_1 == '103000003690000'


def test___lt__():
    """Проверка сравнения"""
    channel_5 = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    red_2 = Channel('UC1eFXmJNkjITxPFWTy6RsWg')
    assert channel_5.__lt__(red_2) is False
    assert red_2.__lt__(channel_5) is True


def test___gt__():
    """Проверка сравнения"""
    channel_6 = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    red_3 = Channel('UC1eFXmJNkjITxPFWTy6RsWg')
    assert channel_6.__gt__(red_3) is True
    assert red_3.__gt__(channel_6) is False
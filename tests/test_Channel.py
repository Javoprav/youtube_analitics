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


def test_get_service():
    """Проверка возврата id"""
    vduda = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    assert vduda.get_service() == '<googleapiclient.discovery.Resource object at 0x00000209043A1150>'

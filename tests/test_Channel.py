import pytest
from main import *
from tests.conftest import test_data


def test_print_info():
    """Проверка получения инфо о канале"""
    channel_1 = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    assert channel_1.print_info() is None
    assert print(channel_1.print_info()) == print(test_data)


def test_to_json():
    channel_1 = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    assert channel_1.to_json('vdud.json') == print(test_data)


def test_channel_id():
    vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    assert print(vdud.channel_id) is None


def get_service():
    assert print(Channel.get_service()) == '<googleapiclient.discovery.Resource object at 0x000002B1E54F9750>'

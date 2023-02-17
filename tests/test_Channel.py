import pytest
from main import *
from tests.conftest import test_data


def test_print_info():
    """Проверка получения инфо о канале"""
    channel_1 = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    assert channel_1.print_info() is None
    assert print(channel_1.print_info()) == print(test_data)
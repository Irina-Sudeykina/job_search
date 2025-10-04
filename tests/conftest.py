import pytest

from src.hh_api import HeadHunterAPI


@pytest.fixture
def head_hunter_api():
    return HeadHunterAPI()

import pytest
from api import count_tokens, get_company_details, get_moti_letter


def test_count_tokens():
    tokens = count_tokens("siema")

    assert tokens == 5


def test_get_company_details():
    pass


def test_get_moti_letter():
    pass
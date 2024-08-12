from chalicelib.swapidev import Swapidev


import pytest


@pytest.fixture
def swapidev():
    return Swapidev()


def test_get_starships(swapidev):
    assert isinstance(swapidev.get_starships(), list)
def test_get_manufacturer(swapidev):
    assert isinstance(swapidev.get_manufacturers(), list)



def test_get_starships_with_manufacturer(swapidev):
    result = swapidev.get_starships(manufacturer="Kuat Drive Yards")
    assert len([x for x in result if x["manufacturer"]!="Kuat Drive Yards"])==0
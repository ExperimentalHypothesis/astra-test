import pytest as pytest

from src.parser import Parser


@pytest.fixture
def parser():
    file_path = "test/raw_data/small.xml"
    return Parser(file_path)


def test_count(parser):
    assert parser.count == 3


def test_all_items(parser):
    all_items = parser.all_items
    assert all_items == ['a', 'b', 'c']
    assert len(all_items) == 3


def test_items_with_spare_parts(parser):
    spare = parser.items_with_spare_parts
    assert {'a': ['Arrma diferenciál kompletní 37T 1.35M', 'Arrma hřídel posuvná kompozit']} in spare

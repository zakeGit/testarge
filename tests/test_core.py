"""testarge çekirdek testleri."""
from testarge.core import greet


def test_greet_default_name():
    assert greet("Dünya") == "Merhaba, Dünya!"


def test_greet_custom_name():
    assert greet("Zafer") == "Merhaba, Zafer!"


def test_greet_strips_whitespace():
    assert greet("  Hermes  ") == "Merhaba, Hermes!"


def test_greet_falls_back_on_empty():
    assert greet("") == "Merhaba, Dünya!"
    assert greet("   ") == "Merhaba, Dünya!"

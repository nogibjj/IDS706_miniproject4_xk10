"""
Test goes here

"""

from main import add
import sys
import main


def test_add_positive_numbers():
    assert add(3, 5) == 8


def test_add_negative_numbers():
    assert add(-3, -5) == -8


def test_add_mixed_numbers():
    assert add(3, -5) == -2


if __name__ == "__main__":
    test_add_positive_numbers()
    test_add_negative_numbers()
    test_add_mixed_numbers()
    print("All tests passed.")


def test_get_python_version():
    assert main.get_python_version() == sys.version

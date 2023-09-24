"""
Main code
"""
import sys


def add(a, b):
    return a + b


def get_python_version():
    return sys.version


if __name__ == "__main__":
    result = add(3, 5)
    print(f"The result of adding 3 and 5 is {result}")
    print("Python Version:", get_python_version())

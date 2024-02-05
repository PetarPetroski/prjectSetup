"""This is a test file for my calculator program"""
from app import add, subtract, multiply, divide

def test_addition():
    """This is a test of the addition function"""
    assert add(2,2)==4

def test_subtraction():
    """This is a test of the subtraction function"""
    assert subtract(2,2)==0

def test_multiplication():
    """This is a test of the multiplication function"""
    assert multiply(3,2)==6

def test_division():
    """This is a test of the division function"""
    assert divide(6,2)==3
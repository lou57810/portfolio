# from django.test import TestCase

# Create your tests here.
import pytest


def division(numerator, denominator):
    return numerator / denominator


def test_division():
    numerator = 2
    denominator = 0
    with pytest.raises(ZeroDivisionError):
        division(numerator, denominator)




from triangles_zadanie1 import raznostorini_triangle, ravnobedreni_triangle, ravnostoroni_triangle

import pytest

def test_raznostorini_triangle():
    assert raznostorini_triangle(5, 4,7) == 9.8

def test_ravnobedreni_triangle():
    assert ravnobedreni_triangle(6, 6, 7) == 17.06

def test_ravnostoroni_triangle():
    assert ravnostoroni_triangle(5, 5, 5) == 10.83
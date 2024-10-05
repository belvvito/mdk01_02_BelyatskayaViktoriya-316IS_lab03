from triangles_zadanie2 import ostrougolni_triangle, tupougolni_triangle, pryamougolni_triangle

def test_ostrougolni_triangle():
    assert ostrougolni_triangle(5, 5, 3) == 7.15

def test_tupougolni_triangle():
    assert tupougolni_triangle(6, 5, 9) == 14.14

def test_pryamougolni_triangle():
    assert pryamougolni_triangle(4, 3, 5) == 6.0
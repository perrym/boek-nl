import pytest

from risicoscore import valideer_risicoscore


def test_geldige_score():
    assert valideer_risicoscore(75) == 75.0


def test_negatieve_score():
    with pytest.raises(ValueError):
        valideer_risicoscore(-1)


def test_tekstinvoer():
    with pytest.raises(TypeError):
        valideer_risicoscore("hoog")


@pytest.mark.parametrize("waarde", [0, 100])
def test_grenswaarden(waarde):
    assert valideer_risicoscore(waarde) == float(waarde)

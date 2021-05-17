from app import xinqi_draw


def test_xinqi_draw():
    assert 'Oh you are not xinqi' == xinqi_draw(1)
    assert 'Geez you are extremely xinqi' == xinqi_draw(2)
    assert 'Please try one more time' == xinqi_draw(3)
    assert 'Please try one more time' == xinqi_draw(6)

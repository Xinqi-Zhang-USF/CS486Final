from app import xinqi_draw


def test_xinqi_draw():
    assert 'Oh you are not xinqi' == lucky_draw(1)
    assert 'Geez you are extremely xinqi' == lucky_draw(2)
    assert 'Please try one more time' == lucky_draw(3)
    assert 'Please try one more time' == lucky_draw(6)

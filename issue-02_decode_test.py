import pytest
from morse import decode

@pytest.mark.parametrize('morse, letters', [
   ('.-- .... . .-. .   .- .-. .   -.-- --- ..- ..--..', 'WHERE ARE YOU?'),
   ('... --- ...', 'SOS'),
   ('.-- .... . .-. . ..--..', 'WHERE?')
])
def test_decode(morse, letters):
    assert decode(morse) == letters

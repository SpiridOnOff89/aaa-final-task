

from unittest.mock import patch
from what_is_year_now import what_is_year_now
import unittest
from io import StringIO


API_URL = 'http://worldclockapi.com/api/json/utc/now'

YMD_SEP = '-'
YMD_SEP_INDEX = 4
YMD_YEAR_SLICE = slice(None, YMD_SEP_INDEX)

DMY_SEP = '.'
DMY_SEP_INDEX = 5
DMY_YEAR_SLICE = slice(DMY_SEP_INDEX + 1, DMY_SEP_INDEX + 5)


def test_year_first_format():
    exp_response = '{"currentDateTime": "2021-12-02T13:52Z"}'
    with patch('urllib.request.urlopen', return_value=StringIO(exp_response)):
        actual = what_is_year_now()
    expected = 2021
    assert actual == expected


def test_year_second_format():
    exp_response = '{"currentDateTime": "02.12.2020T13:52Z"}'
    with patch('urllib.request.urlopen', return_value=StringIO(exp_response)):
        actual = what_is_year_now()
    expected = 2020
    assert actual == expected


def test_wrong_year():
    exp_response = '{"currentDateTime": "aaa.12.02"}'
    with patch('urllib.request.urlopen', return_value=StringIO(exp_response)):
        actual = what_is_year_now()
    expected = 2020
    assert actual == expected


if __name__ == '__main__':
    unittest.main()

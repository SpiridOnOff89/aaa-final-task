#### Для запуска тестов doctest функции encode():
- ввести в командной строке команду cd [адрес папки, в которой находятся файлы с тестами]
- ввести  в командной строке: python -m doctest -o NORMALIZE_WHITESPACE -v issue-01_encode_doctests.py (для стандартизации пробелов и переносов строк)
либо python issue-01_encode_doctests.py - v (для запуска без стандартизации). 

#### Для запуска тестов pytest функции decode():
- ввести в командной строке команду cd [адрес папки, в которой находятся файлы с тестами]
- ввести в командной строке: python -m pytest issue-02_decode_test.py

#### Для запуска тестов unittest функции fit_transform():
- ввести в командной строке команду cd [адрес папки, в которой находятся файлы с тестами]
- ввести в командной строке: python -m pytest issue-03_ohe_unittest.py

#### Для запуска тестов pythest функции fit_transform():
- ввести в командной строке команду cd [адрес папки, в которой находятся файлы с тестами]
- ввести в командной строке: python -m pytest issue-04_ohe_test.py

#### Для запуска тестов функции what_is_year_now():
- ввести в командной строке команду cd [адрес папки, в которой находятся файлы с тестами]
- ввести в командной строке: python -m pytest issue-05_year_unittest.py
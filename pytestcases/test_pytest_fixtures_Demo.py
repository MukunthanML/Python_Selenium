import pytest


@pytest.fixture()
def setup():
    print('\nBefore set up done')
    yield
    print('\nAfter set up done')


def test_insurance_01(conf_setup, setup):
    print('insurance 01 test')


def test_retail_01(conf_setup, setup):
    print('retail 01 test')


def test_data_check(data):
    print(data)


@pytest.mark.parametrize(
    "test_input,expected",
    [("3+5", 8), ("2+4", 6), pytest.param("6*9", 42, marks=pytest.mark.xfail)],
)
def test_eval(test_input, expected):
    assert eval(test_input) == expected



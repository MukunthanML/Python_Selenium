import pytest


def test_insurance_01():
    print('insurance 01 test')


@pytest.mark.regression
def test_insurance_02():
    print('insurance 02 test')


@pytest.mark.xfail
def test_insurance_03():
    print('insurance 03 test')


def test_retail_01():
    print('retail 01 test')


@pytest.mark.regression
def test_retail_02():
    print('retail 02 test')


@pytest.mark.skip
def test_retail_03():
    print('retail 03 test')


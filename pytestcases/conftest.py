import pytest


@pytest.fixture()
def conf_setup():
    print('\nConf Before set up done')
    yield
    print('\nConf After set up done')


@pytest.fixture()
def data():
    return ('python-user', 'pypassword', 'python@demo.com')


@pytest.fixture(scope='class')
def class_fixture():
    print('\nBefore class set up')
    yield
    print('\nAfter class set up')


@pytest.fixture(params=[('user1','pwd1'),('user2','pwd2'),('user3','pwd3')])
def data_provider(request):
    return request.param





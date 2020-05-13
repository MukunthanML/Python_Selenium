import pytest


@pytest.mark.usefixtures('class_fixture')
@pytest.mark.usefixtures('conf_setup')
@pytest.mark.usefixtures('data')
class TestDemo:

    def test_class_method1(self):
        print('Class test method1 execution')

    def test_class_method2(self):
        print('Class test method2 execution')

    def test_class_method3(self, data):
        print('Class test method3 execution')
        print(data[0])
        print(data[1])
        print(data[2])

    @pytest.mark.usefixtures('data_provider')
    def test_class_method4(self, data_provider):
        print('Class test method3 execution')
        print(data_provider[0])
        print(data_provider[1])



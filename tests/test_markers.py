import pytest

@pytest.mark.smoke
def test_some_case():
    print('smoke test case')

@pytest.mark.regression
def test_regression_case():
    print('regression test case')

@pytest.mark.smoke
class TestSuite:
    @pytest.mark.regression
    def test_case_1(self):
        ...

    def test_case_2(self):
        ...

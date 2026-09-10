import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize('number', [1, 2, -1, 4])
def test_numbers(number: int):
    assert number > 0
    print('Bigger than 0')

@pytest.mark.parametrize('number, expected',[(1,1), (2,4), (3,9)] )
def test_several_numbers(number, expected):
    assert number * number == expected

@pytest.mark.parametrize('os', ['macos', 'windows', 'linux', 'debian'])
@pytest.mark.parametrize('browser', ['chromium', 'firefox', 'webkit'])
def test_multiplication_of_numbers(os:str, browser:str):
    assert len(os + browser) > 0


@pytest.fixture(params=['chromium', 'firefox', 'webkit'])
def browser(request: SubRequest):
    return request.param


def test_open_browser(browser: str):
    print(f'Running test on browser: {browser}')

@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperations:

    @pytest.mark.parametrize('account', ['Credit card', 'Debit card'])
    def test_user_with_operations(self, user: str, account: str):
        print(f'User with operations {user}')


    def test_user_without_operations(self, user: str):
        print(f'User without operations {user}')


users = {
    '+1234567890':'user with money on bank account',
    '+0987654321':'user without money on bank account',
    '+1122334455':'user with operations on bank account'
}


@pytest.mark.parametrize(
        'phone_number',
        users.keys(),
        ids = lambda phone_number: f'{phone_number}:{users[phone_number]}'
)
def test_identifiers(phone_number : str):
    ...

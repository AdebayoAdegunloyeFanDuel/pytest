import pytest
from wallet import Wallet, InsufficientAmount


@pytest.fixture
def empty_wallet():
    '''Return a wallet instance with big zero balance'''
    return Wallet()


@pytest.fixture
def wallet():
    '''Return a wallet instance with a balance of 20'''
    return Wallet(20)


def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0


def test_setting_initial_amount(wallet):
    assert wallet.balance == 20


def test_wallet_add_cash(wallet):
    wallet.add_cash(80)
    assert wallet.balance == 100


def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10


def test_wallet_spend_cash_rasies_exception_on_insufficiet_amount(empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)


@pytest.fixture
def my_wallet():
    '''Return instance with zero balance'''
    return Wallet()

# testing various combination of earned cash and spent amount.
@pytest.mark.parametrize("earned, spent, expected", [
    (30, 10, 20),
    (20, 2, 18),
])
def test_transaction(my_wallet, earned, spent, expected):
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected
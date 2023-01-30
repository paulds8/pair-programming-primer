import pytest
from main import get_exchange_rates


def test_get_exchange_rates_is_dict():
    # Test that the function returns a dictionary
    rates = get_exchange_rates()
    assert isinstance(rates, dict), "rates is not a dict"


def test_get_exchange_rates_base_currency():
    # # Test that the base currency is in the response with a value of 1
    base_currency = "USD"
    rates = get_exchange_rates(base_currency)
    assert base_currency in rates, f"{base_currency} not in rates"
    assert (
        rates[base_currency] == 1.0
    ), f"{base_currency}={rates[base_currency]}, expected 1.0"


def test_request_invalid_base_currency():
    # Test that the function raises a ValueError when given an invalid base currency
    with pytest.raises(ValueError) as exc_info:
        rates = get_exchange_rates("invalid")
    assert exc_info.value.args[0] == "invalid not a supported option."

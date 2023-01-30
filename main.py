import requests
from typing import Dict
from collections import OrderedDict

VALID_BASE_CURRENCIES = ["USD", "ZAR"]


def get_exchange_rates(
    base_currency: str = "USD",
) -> Dict:

    if base_currency not in VALID_BASE_CURRENCIES:
        raise ValueError(f"{base_currency} not a supported option.")
    source = f"https://open.er-api.com/v6/latest/{base_currency}"
    response = requests.get(source)
    data = response.json()
    return data["rates"]


def convert_rate_to_percentage_difference(
    rates,
    base_currency="USD",
):
    rates_percentage = {}
    base_rate = rates[base_currency]

    for currency, amount in rates.items():
        rates_percentage[currency] = (amount - base_rate) / base_rate * 100

    sorted_by_value = OrderedDict(
        sorted(rates_percentage.items(), key=lambda item: item[1])
    )
    return sorted_by_value


if __name__ == "__main__":

    base_currency = "USD"
    rates = get_exchange_rates(
        base_currency=base_currency,
    )
    relative_rates = convert_rate_to_percentage_difference(
        rates=rates,
        base_currency=base_currency,
    )

    lowest = next(iter(relative_rates.items()))
    highest = next(reversed(relative_rates.items()))

    print(f"{lowest[0]} is {abs(lowest[1]):,.2f}% stronger than {base_currency}")
    print(f"{highest[0]} is {highest[1]:,.2f}% weaker than {base_currency}")

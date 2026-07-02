import requests


def convert_currency(amount: float,
                     from_currency: str,
                     to_currency: str) -> str:
    """
    Converts currency using ExchangeRate API.
    """

    url = f"https://open.er-api.com/v6/latest/{from_currency.upper()}"

    response = requests.get(url).json()

    if response["result"] != "success":
        return "Currency API Error"

    rates = response["rates"]

    if to_currency.upper() not in rates:
        return "Invalid target currency."

    converted = amount * rates[to_currency.upper()]

    return (
        f"{amount:.2f} {from_currency.upper()} = "
        f"{converted:.2f} {to_currency.upper()}"
    )
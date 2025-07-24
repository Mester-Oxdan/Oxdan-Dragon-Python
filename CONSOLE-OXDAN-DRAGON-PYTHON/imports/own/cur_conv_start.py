from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter  # Optional, for BTC
from colorama import Fore
import imports.own.will_go_to_start
import colorama
import requests
import re

# Fixer.io API key (replace this with your real key)
API_KEY = 'ac2c4f520953ea9b1cfac00d10732af1'

class FixerCurrencyRates(CurrencyRates):
    def __init__(self):
        super().__init__()
        self.api_key = API_KEY

    def get_rates(self):
        response = requests.get(f"https://data.fixer.io/api/latest?access_key={self.api_key}")
        data = response.json()
        if not data.get("success", False):
            raise Exception(f"API Error: {data.get('error', {}).get('info', 'Unknown error')}")
        return data["rates"]

    def convert(self, from_currency, to_currency, amount):
        rates = self.get_rates()

        if from_currency == "EUR":
            # direct conversion from EUR to target
            if to_currency not in rates:
                raise Exception(f"Unsupported currency code: {to_currency}")
            rate = rates[to_currency]
            return amount * rate

        if to_currency == "EUR":
            # converting from base to EUR
            if from_currency not in rates:
                raise Exception(f"Unsupported currency code: {from_currency}")
            rate = rates[from_currency]
            return amount / rate

        # Otherwise convert from `from_currency` to EUR, then EUR to `to_currency`
        if from_currency not in rates or to_currency not in rates:
            raise Exception(f"Unsupported currency code: {from_currency} or {to_currency}")

        amount_in_eur = amount / rates[from_currency]
        final_amount = amount_in_eur * rates[to_currency]
        return final_amount


def is_valid_currency_code(code):
    # Basic check: 3 uppercase letters
    return bool(re.match(r"^[A-Z]{3}$", code))

def convert_currency(amount, from_currency, to_currency):
    c = FixerCurrencyRates()

    try:
        converted_amount = c.convert(from_currency, to_currency, amount)
        return converted_amount
    except Exception as e:
        return str(e)

def cur_conv_start():
    print(Fore.RED + "\nEnter 'esc' (for exit)")
    amount = input(Fore.YELLOW + "Enter amount to convert: " + Fore.WHITE).strip()
    if imports.own.will_go_to_start.remove_098(amount.lower()) == "esc":
        imports.own.will_go_to_start.main()

    if not amount:
        print(Fore.RED + "(!ERROR!) Amount cannot be empty." + Fore.WHITE)
        imports.own.will_go_to_start.main()
        return

    try:
        amount = float(amount)
    except ValueError:
        print(Fore.RED + "(!ERROR!) Invalid number." + Fore.WHITE)
        imports.own.will_go_to_start.main()
        return

    from_currency = input(Fore.YELLOW + "Enter currency from (e.g., USD, EUR): " + Fore.WHITE).strip().upper()
    if imports.own.will_go_to_start.remove_098(from_currency.lower()) == "esc":
        imports.own.will_go_to_start.main()

    if not is_valid_currency_code(from_currency):
        print(Fore.RED + "(!ERROR!) Invalid currency code format." + Fore.WHITE)
        imports.own.will_go_to_start.main()
        return

    to_currency = input(Fore.YELLOW + "Enter currency to (e.g., USD, EUR): " + Fore.WHITE).strip().upper()
    if imports.own.will_go_to_start.remove_098(to_currency.lower()) == "esc":
        imports.own.will_go_to_start.main()

    if not is_valid_currency_code(to_currency):
        print(Fore.RED + "(!ERROR!) Invalid currency code format." + Fore.WHITE)
        imports.own.will_go_to_start.main()
        return

    # Warn user about free plan limitation
    if from_currency != "EUR":
        print(Fore.YELLOW + "Note: Free Fixer.io plan only supports EUR as the base currency. Conversion may fail." + Fore.WHITE)

    converted_amount = convert_currency(amount, from_currency, to_currency)

    if isinstance(converted_amount, float):
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    else:
        print(colorama.Fore.RED + "\n(!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + f" (!Error: {converted_amount}!)" + colorama.Fore.WHITE)

    imports.own.will_go_to_start.main()

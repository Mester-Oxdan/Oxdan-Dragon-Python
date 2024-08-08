from currency_converter import CurrencyConverter
from colorama import Fore
import imports.own.will_go_to_start
import colorama

def convert_currency(amount, from_currency, to_currency):
    # Initialize the CurrencyConverter
    c = CurrencyConverter()

    try:
        # Convert the amount
        converted_amount = c.convert(amount, from_currency, to_currency)
        return converted_amount
    except Exception as e:
        return str(e)

def cur_conv_start():
    # Example usage
    print(Fore.RED + "\nEnter 'esc' (for exit)")
    amount = str(input(Fore.YELLOW + "Enter amount to convert: " + Fore.WHITE))
    if imports.own.will_go_to_start.remove_098(amount.lower()) == "esc":

                imports.own.will_go_to_start.main()
    amount = float(amount)
    from_currency = input(Fore.YELLOW + "Enter currency from (e.g., USD, EUR): " + Fore.WHITE).upper()
    print(" ")
    if imports.own.will_go_to_start.remove_098(from_currency.lower()) == "esc":

                imports.own.will_go_to_start.main()
    to_currency = input(Fore.YELLOW + "Enter currency to (e.g., USD, EUR): " + Fore.WHITE).upper()
    print(" ")
    if imports.own.will_go_to_start.remove_098(to_currency.lower()) == "esc":

                imports.own.will_go_to_start.main()
    converted_amount = convert_currency(amount, from_currency, to_currency)

    if isinstance(converted_amount, float):
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
        imports.own.will_go_to_start.main()
    else:
        #print(f"Error: {converted_amount}")
        print(colorama.Fore.RED + "\n(!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + f" (!Error: {converted_amount}!)" + colorama.Fore.WHITE)
        imports.own.will_go_to_start.main()
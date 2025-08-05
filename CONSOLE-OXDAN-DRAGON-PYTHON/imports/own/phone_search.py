import phonenumbers
from phonenumbers import geocoder, carrier, number_type, PhoneNumberType
from phonenumbers.phonenumberutil import region_code_for_number
import pycountry
from colorama import Fore
import imports.own.will_go_to_start
from time import sleep

def get_location_by_number(number):
    try:
        # Parse number
        phone_number = phonenumbers.parse(number)

        # Validate number
        is_valid = phonenumbers.is_valid_number(phone_number)

        # Get region and country
        region = geocoder.description_for_number(phone_number, "en")
        country_code = region_code_for_number(phone_number)
        country = pycountry.countries.get(alpha_2=country_code)

        # Get carrier name
        provider = carrier.name_for_number(phone_number, "en")

        # Get number type
        type_lookup = {
            PhoneNumberType.FIXED_LINE: "Fixed line",
            PhoneNumberType.MOBILE: "Mobile",
            PhoneNumberType.FIXED_LINE_OR_MOBILE: "Fixed line or mobile",
            PhoneNumberType.TOLL_FREE: "Toll free",
            PhoneNumberType.PREMIUM_RATE: "Premium rate",
            PhoneNumberType.SHARED_COST: "Shared cost",
            PhoneNumberType.VOIP: "VoIP",
            PhoneNumberType.PERSONAL_NUMBER: "Personal number",
            PhoneNumberType.PAGER: "Pager",
            PhoneNumberType.UAN: "Universal access number",
            PhoneNumberType.VOICEMAIL: "Voicemail",
            PhoneNumberType.UNKNOWN: "Unknown",
        }
        num_type = number_type(phone_number)
        type_string = type_lookup.get(num_type, "Unknown")

        # Output result
        print(" ")
        print(f"VALID: {'Yes' if is_valid else 'No'}")
        sleep(0.01)
        print(f"CARRIER: {provider if provider else 'Unknown'}")
        sleep(0.01)
        print(f"TYPE: {type_string}")
        sleep(0.01)
        print(f"COUNTRY: {country.name if country else 'Unknown'}")
        sleep(0.01)
        print(f"REGION: {region}")
        sleep(0.01)
        print("CITY: Unknown")
        sleep(0.01)
        print("ZIP: Unknown")
        sleep(0.01)
        print("Y: Unknown")
        sleep(0.01)
        print("X: Unknown")
        sleep(0.01)

        imports.own.will_go_to_start.main()

    except Exception as e:
        print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + f" (!Error: {e}!)" + Fore.WHITE)
        imports.own.will_go_to_start.main()

def phone_search():
    # === Main ===
    print(Fore.RED + "\nEnter 'esc' (for exit)" + Fore.WHITE)
    input_number = input("Enter Phone Number With Country Code: ")
    if imports.own.will_go_to_start.remove_098(input_number.lower()) == "esc":
        imports.own.will_go_to_start.main()
    get_location_by_number(input_number)

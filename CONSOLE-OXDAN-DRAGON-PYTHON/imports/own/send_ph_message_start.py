import http.client
from colorama import Fore
import colorama
import imports.own.will_go_to_start

"""
 * Send an sms message by using Infobip API.
 *
 * This example is already pre-populated with your account data:
 * 1. Your account Base URL
 * 2. Your account API key
 * 3. Your recipient phone number
 *
 * THIS CODE EXAMPLE IS READY BY DEFAULT. HIT RUN TO SEND THE MESSAGE!
 *
 * Send sms API reference: https://www.infobip.com/docs/api#channels/sms/send-sms-message
 * See Readme file for details.
"""

def send_ph_message_start():

    try:
        print(colorama.Fore.RED + "\nWrite 'esc' (for exit)")
        API_KEY = input(Fore.YELLOW + "Enter api key to infobip(" + Fore.WHITE + "https://portal.infobip.com" + Fore.YELLOW + "): " + Fore.WHITE)
        if API_KEY == "esc":

            imports.own.will_go_to_start.main()

        RECIPIENT = input(Fore.YELLOW + "\nEnter phone number to recipient: " + Fore.WHITE)
        if RECIPIENT == "esc":

            imports.own.will_go_to_start.main()

        MESSAGE_TEXT = input(Fore.YELLOW + "\nEnter your message: " + Fore.WHITE)
        if MESSAGE_TEXT == "esc":

            imports.own.will_go_to_start.main()

        BASE_URL = "pwzyvl.api.infobip.com"
        #API_KEY = "App fb7c288f7b6f1221246dde1189484e54-94a12933-80a1-40c7-8d8d-0edc4677a65f"

        SENDER = "InfoSMS"
        #RECIPIENT = "14129089359"
        #MESSAGE_TEXT = "This is a sample message"

        conn = http.client.HTTPSConnection(BASE_URL)

        payload1 = "{\"messages\":" \
                  "[{\"from\":\"" + SENDER + "\"" \
                  ",\"destinations\":" \
                  "[{\"to\":\"" + RECIPIENT + "\"}]," \
                  "\"text\":\"" + MESSAGE_TEXT + "\"}]}"

        headers = {
            'Authorization': API_KEY,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        conn.request("POST", "/sms/2/text/advanced", payload1, headers)

        res = conn.getresponse()
        data = res.read()
        #print(data.decode("utf-8"))
        imports.own.will_go_to_start.main()

    except:

        print(colorama.Fore.RED + "\n(!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!Enter valid information!)\n" + colorama.Fore.WHITE)
        imports.own.will_go_to_start.main()
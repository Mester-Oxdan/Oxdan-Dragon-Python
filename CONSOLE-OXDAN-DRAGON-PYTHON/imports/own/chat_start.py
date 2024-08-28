import socket
import threading
from colorama import Fore
import imports.own.will_go_to_start

# Global storage for server details
servers = {}

def broadcast(message, _client, server_details):
    for client in server_details['clients']:
        if client != _client:
            try:
                client.send(message)
            except:
                remove(client, server_details)

def remove(client, server_details):
    if client in server_details['clients']:
        server_details['clients'].remove(client)

def handle_client(client_socket, client_address, server_details):
    print(Fore.GREEN + "[NEW CONNECTION]" + Fore.WHITE + f" {client_address} connected.")
    
    # Step 1: Receive and verify the PIN
    client_pin = client_socket.recv(1024).decode('utf-8')
    if client_pin != server_details['pin']:
        client_socket.send("Invalid PIN".encode('utf-8'))
        client_socket.close()
        print(Fore.RED + "[DISCONNECTED]" + Fore.WHITE + f" {client_address} disconnected due to invalid PIN.")
        return
    else:
        client_socket.send("OK".encode('utf-8'))

    # Step 2: Receive the client's name
    client_name = client_socket.recv(1024).decode('utf-8')
    print(f"{client_name} has joined the chat.")

    # Step 3: Start chatting
    client_connected = True
    while client_connected:
        try:
            message = client_socket.recv(1024)
            if message:
                full_message = f"{client_name}: {message.decode('utf-8')}"
                print(full_message)
                broadcast(full_message.encode('utf-8'), client_socket, server_details)
            else:
                client_connected = False
        except:
            client_connected = False
            remove(client_socket, server_details)
    
    print(f"{client_name} has left the chat.")
    client_socket.close()

def start_server():
    ip_address = socket.gethostbyname(socket.gethostname())
    port = int(input(Fore.YELLOW + "Enter port to host the server: " + Fore.WHITE))
    pin = input(Fore.YELLOW + "Create PIN for this server: " + Fore.WHITE)

    # Ensure the IP, port, and PIN are unique
    if any(s['ip'] == ip_address and s['port'] == port or s['pin'] == pin for s in servers.values()):
        #print("Error: IP, port, or PIN already in use.")
        print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!IP, Port, or PIN already in use!)\n" + Fore.WHITE)
        imports.own.will_go_to_start.main()
    
    server_details = {
        'ip': ip_address,
        'port': port,
        'pin': pin,
        'clients': []
    }
    
    servers[pin] = server_details
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip_address, port))
    server_socket.listen()
    print(Fore.YELLOW + "[LISTENING]" + Fore.WHITE + f" Server is listening on IP: {ip_address}, PORT: {port}, PIN: {pin}")
    
    while True:
        client_socket, client_address = server_socket.accept()
        server_details['clients'].append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address, server_details))
        thread.start()

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"{message}")
            else:
                break
        except:
            #print("An error occurred!")
            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Error occurred!)\n" + Fore.WHITE)
            client_socket.close()
            break

def start_client():
    SERVER_IP = input(Fore.YELLOW + "Enter server IP Address: " + Fore.WHITE)
    SERVER_PORT_2 = input(Fore.YELLOW + "Enter server Port: " + Fore.WHITE)
    SERVER_PIN = input(Fore.YELLOW + "Enter server PIN: " + Fore.WHITE)
    name_2 = input(Fore.YELLOW + "Enter your Name: " + Fore.WHITE)
    if imports.own.will_go_to_start.remove_098(SERVER_IP.lower()) == 'esc' or imports.own.will_go_to_start.remove_098(SERVER_PORT_2.lower()) == 'esc' or imports.own.will_go_to_start.remove_098(SERVER_PIN.lower()) == 'esc' or imports.own.will_go_to_start.remove_098(name_2.lower()) == 'esc':
        imports.own.will_go_to_start.main()
    SERVER_PORT = int(SERVER_PORT_2)
    name = imports.own.will_go_to_start.remove_098(name_2)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))
    
    # Send the PIN to the server for validation
    client_socket.send(SERVER_PIN.encode('utf-8'))
    
    # Receive server's response
    response = client_socket.recv(1024).decode('utf-8')
    if response == "OK":
        # Send the client's name to the server
        client_socket.send(name.encode('utf-8'))

        # Start a thread to listen for messages from the server
        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.start()
        
        while True:
            message = input()
            if imports.own.will_go_to_start.remove_098(message.lower()) == 'exit' or imports.own.will_go_to_start.remove_098(message.lower()) == 'quit' or imports.own.will_go_to_start.remove_098(message.lower()) == 'esc':
                imports.own.will_go_to_start.main()
            client_socket.send(message.encode('utf-8'))
    else:
        #print("Invalid PIN. Connection refused.")
        print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Invalid PIN!)\n" + Fore.WHITE)
        client_socket.close()
        imports.own.will_go_to_start.main()

def chat_start():
    print(" ")
    print(Fore.RED + "Enter 'esc' (for exit)" + Fore.WHITE)
    mode = input(Fore.YELLOW + "Enter '1' to start server or '2' to start client: " + Fore.WHITE).strip().lower()
    
    if imports.own.will_go_to_start.remove_098(mode.lower()) == '1':
        start_server()
    elif imports.own.will_go_to_start.remove_098(mode.lower()) == '2':
        start_client()
    elif imports.own.will_go_to_start.remove_098(mode.lower()) == 'esc':
        imports.own.will_go_to_start.main()
    else:
        print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Invalid option!)\n" + Fore.WHITE)
        imports.own.will_go_to_start.main()
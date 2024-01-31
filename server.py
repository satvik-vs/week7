import socket
import threading
import os

def send_file(client_address, file_path):
    with open(file_path, 'rb') as file:
        chunk = file.read(1024)
        while chunk:
            server_socket.sendto(chunk, client_address)
            chunk = file.read(1024)
    print(f"File '{file_path}' sent to {client_address}")

def handle_client(request, client_address):
    file_name = request.decode()
    file_path = os.path.join("/home/satvik/CN_LAB/Lab8/download.jpeg", file_name) 
    if os.path.exists(file_path):
        send_file(client_address, file_path)
    else:
        error_message = "File not found"
        server_socket.sendto(error_message.encode(), client_address)
        print(f"Error: {error_message}")

def server_listen():
    while True:
        request, client_address = server_socket.recvfrom(1024)
        client_handler = threading.Thread(target=handle_client, args=(request, client_address))
        client_handler.start()
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 8080)) 

print("Server listening on port 8080")
server_listen()

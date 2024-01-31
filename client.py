import socket

def receive_file(file_name):
    with open(file_name, 'wb') as file:
        while True:
            file_data, server_address = client_socket.recvfrom(1024)
            if not file_data:
                break
            file.write(file_data)
    print(f"File '{file_name}' received from the server")

def request_file(file_name):
    client_socket.sendto(file_name.encode(), ('localhost', 8080))

file_name = "/home/satvik/CN_LAB/Lab8/download.jpeg" 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

request_file(file_name)
receive_file(file_name)

client_socket.close()

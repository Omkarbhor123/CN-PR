import socket

def receive_file(file_name, client_address, client_port):
    with open(file_name, 'wb') as file:
        while True:
            try:
                data, addr = server_socket.recvfrom(1024)
            except ConnectionResetError:
                print(f"Client {client_address}:{client_port} disconnected")
                break
            if data == b'EOF':
                break
            file.write(data)
    print(f"File received successfully: {file_name}")

server_host = '0.0.0.0'  # Listen on all available interfaces
server_port = 12345  # Port to listen on

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_host, server_port))

print(f"Server is listening on {server_host}:{server_port}")

while True:
    data, addr = server_socket.recvfrom(1024)
    file_name = data.decode()
    print(f"Receiving file: {file_name} from {addr[0]}:{addr[1]}")
    receive_file(file_name, addr[0], addr[1])

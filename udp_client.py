import socket

def send_file(file_name):
    with open(file_name, 'rb') as file:
        data = file.read(1024)
        while data:
            client_socket.sendto(data, (server_host, server_port))
            data = file.read(1024)
        client_socket.sendto(b'EOF', (server_host, server_port))

server_host = 'localhost'  # Server address to connect to
server_port = 12345  # Server port number

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send text file
send_file('test.txt')

# Send audio file
# send_file('audio.wav')

# Send video file
# send_file('video.mp4')

# Send script file
# send_file('script.sh')

client_socket.close()

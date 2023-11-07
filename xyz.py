import socket

def get_host_by_address(ip_address):
    try:
        host_name, _, _ = socket.gethostbyaddr(ip_address)
        return host_name
    except socket.herror:
        return "Unknown host"

def get_address_by_host(host_name):
    try:
        ip_address = socket.gethostbyname(host_name)
        return ip_address
    except socket.gaierror:
        return "Unknown IP address"

while True:
    print("DNS Lookup Program")
    print("1. IP Address to URL")
    print("2. URL to IP Address")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        ip_address = input("Enter IP Address: ")
        url = get_host_by_address(ip_address)
        print(f"Corresponding URL: {url}\n")
    elif choice == "2":
        host_name = input("Enter URL: ")
        ip_address = get_address_by_host(host_name)
        print(f"Corresponding IP Address: {ip_address}\n")
    elif choice == "3":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.\n")

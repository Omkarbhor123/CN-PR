import sys

def get_subnet_mask(ip_address, number_of_hosts):
  
  network_address = ip_address.split(".")
  first_octet = int(network_address[0])
  second_octet = int(network_address[1])
  third_octet = int(network_address[2])
  fourth_octet = int(network_address[3])

  host_bits = 32 - number_of_hosts

  if(first_octet>=0 | first_octet<=127):
     subnet_mask = "255.0.0.0" + str(2**host_bits - 2)
     print("class A")

  elif(first_octet>=128 | first_octet<=191 ):
    subnet_mask = "255.255.0.0" + str(2**host_bits - 2)
    print("class B")

  else:
    subnet_mask = "255.255.255.0" + str(2**host_bits - 2)
    print("class C")


  subnet_mask = "255.255.0.0" + str(2**host_bits - 2)

  return subnet_mask

def main():
 
  print("Welcome to the subnetting calculator!")

  while True:
    print("1. Calculate subnet mask")
    print("2. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
      ip_address = input("Enter the IP address: ")
      number_of_hosts = int(input("Enter the number of hosts: "))

      subnet_mask = get_subnet_mask(ip_address, number_of_hosts)

      print("The subnet mask for " + ip_address + " is " + subnet_mask)

    elif choice == "2":
      break

    else:
      print("Invalid choice.")

if __name__ == "__main__":
  main()

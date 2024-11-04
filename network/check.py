import ipaddress

# Define an IPv4 address
ipv4_address = ipaddress.IPv4Address('192.168.1.1')
print(f"IPv4 Address: {ipv4_address}")

# Define an IPv6 address
ipv6_address = ipaddress.IPv6Address('2001:0db8:85a3:0000:0000:8a2e:0370:7334')
print(f"IPv6 Address: {ipv6_address}")

# Checking if an IP Address Belongs to a Network
ip = ipaddress.IPv4Address('192.168.1.10')
network = ipaddress.IPv4Network('192.168.1.0/24')

if ip in network:
    print(f"{ip} is in the network {network}")
else:
    print(f"{ip} is not in the network {network}")

# Check if an IP is private
print(f"Is {ipv4_address} private? {ipv4_address.is_private}")

# Get reverse DNS pointer
print(
    f"Reverse DNS pointer for {ipv4_address}: {ipv4_address.reverse_pointer}")

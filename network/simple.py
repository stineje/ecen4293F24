import ipaddress

# Define an IPv4 address
ipv4_address = ipaddress.IPv4Address('192.168.1.1')
print(f"IPv4 Address: {ipv4_address}")

# Define an IPv6 address
ipv6_address = ipaddress.IPv6Address('2001:0db8:85a3:0000:0000:8a2e:0370:7334')
print(f"IPv6 Address: {ipv6_address}")

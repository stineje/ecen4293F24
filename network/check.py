import ipaddress

ip = ipaddress.IPv4Address('10.203.8.126')
network = ipaddress.IPv4Network('10.203.8.0/24')

if ip in network:
    print(f"{ip} is in the network {network}")
else:
    print(f"{ip} is not in the network {network}")

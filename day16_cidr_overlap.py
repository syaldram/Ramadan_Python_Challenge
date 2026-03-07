import ipaddress

def cidr_overlaps(cidr1: str, cidr2: str) -> bool:
    network1 = ipaddress.ip_network(cidr1)
    network2 = ipaddress.ip_network(cidr2)
    return network1.overlaps(network2)

if __name__ == "__main__":
    print(cidr_overlaps("10.0.0.0/16", "10.0.1.0/24"))  # ➞ True
    print(cidr_overlaps("192.168.1.0/24", "192.168.2.0/24"))  # ➞ False
    print(cidr_overlaps("10.0.0.0/8", "10.255.0.0/16"))  # ➞ True
    print(cidr_overlaps("172.16.0.0/12", "192.168.0.0/16"))  # ➞ False
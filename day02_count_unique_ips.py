from collections import Counter

def count_ips(logs: list):
    
    ip_lst = []
    
    for record in logs:
        split = record.split()
        ip_lst.append(split[0])
        
    counts = Counter(ip_lst)
    
    return counts.most_common(5)    
    


if __name__ == "__main__":
    
    logs = [
    "192.168.1.1 - - [28/Feb/2026] GET /index.html",
    "10.0.0.5 - - [28/Feb/2026] POST /api/login",
    "192.168.1.1 - - [28/Feb/2026] GET /about.html",
    "10.0.0.5 - - [28/Feb/2026] GET /dashboard",
    "172.16.0.3 - - [28/Feb/2026] GET /index.html",
    "192.168.1.1 - - [28/Feb/2026] GET /contact"
]
    
    print(count_ips(logs))
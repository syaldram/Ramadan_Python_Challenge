"""
Day 1 - Reverse Log line
"""

def reverse_log(log: str):
    
    res = ' '.join(log.split()[::-1])
    print(res)
    return res


def parse_log(log: str) -> dict:

    log_data = log.split()
    res = {}
    
    for log in log_data:
        if log.isupper():
            res["level"] = log
        if any(char.isdigit() for char in log):
            res["date"] = log
    res["message"] = " ".join(log_data[2:])
    print(res)
    
    """    
    parts = log.split()
    return {
        "date": parts[0],
        "level": parts[1],
        "message": " ".join(parts[2:])
    }
    """
    return res
    


if __name__ == "__main__":
    
    reverse_log("2026-02-28 ERROR server crashed")
    reverse_log("2026-03-01 INFO deployment started")
    reverse_log("2026-03-02 WARN disk space low")
    
    parse_log("2026-02-28 ERROR server crashed")
    parse_log("2026-03-01 INFO deployment started")
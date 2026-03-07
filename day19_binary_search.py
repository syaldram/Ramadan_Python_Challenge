import bisect

def search_logs(logs, target):
    
    index = bisect.bisect_left(logs, target)
    
    if index < len(logs):
        return logs[index]
    else:
        return None
   


if __name__ == "__main__":
    logs = [
    "2026-03-01T08:00:00 Server started",
    "2026-03-01T09:15:00 User login",
    "2026-03-01T10:30:00 Error occurred",
    "2026-03-01T11:45:00 Deployment done",
    "2026-03-01T14:00:00 Backup completed"
]
    
    
    print(search_logs(logs, "2026-03-01T10:00:00"))
    print(search_logs(logs, "2026-03-01T12:00:00"))
    print(search_logs(logs, "2026-03-01T15:00:00"))
    

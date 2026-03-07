import time

def retry(max_attempts: int =3, delay: int =1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            current_delay = delay
            count = 1
            while count <= max_attempts:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"Attempt: {count}: {e}, waiting {current_delay}s...")
                    if count == max_attempts:
                        raise e
                    else:
                        count += 1
                        time.sleep(current_delay)
                        current_delay *= 2
                    
        return wrapper
    return decorator
                

if __name__ == "__main__":
    
    @retry(max_attempts=3, delay=1)
    def fetch_data():
        raise ConnectionError("timeout")
    
    print(fetch_data())
    
    @retry(max_attempts=3, delay=1)
    def get_status():
        return 200
    
    print(get_status())
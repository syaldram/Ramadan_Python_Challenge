from collections import OrderedDict

class LRUCache:
    
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
        
    def get(self, key: int) ->int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
        
    def put(self, key: int, value: str) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
    
if __name__ == "__main__":
    
    cache = LRUCache(2)
    print(cache.put(1, "ec2-instance"))
    print(cache.put(2, "s3-bucket"))
    print(cache.get(1))
    print(cache.put(3, "lambda-fn"))
    print(cache.get(2))
    print(cache.get(3))
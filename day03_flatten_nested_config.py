
def flatten(nest_dict: dict):
    
    result = {}
    
    if any(isinstance(val, dict) for val in nest_dict.values()):
    
        for k, v in nest_dict.items():
            for key, value in v.items():
                result[f"{k}.{key}"] = value
        return result
    else:
        return nest_dict
            

            
            
        
if __name__ == "__main__":
    
    print(flatten({"server": {"host": "0.0.0.0", "port": 8080}}))
    print(flatten({"db": {"primary": {"host": "db1", "port": 5432}}}))
    print(flatten({"name": "app"}))
    print(flatten({}))
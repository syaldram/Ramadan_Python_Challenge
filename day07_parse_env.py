
def parse_env(env_str: str):
    
    env_dict = {}
    
    
    res = env_str.splitlines()
    
    for line in res:
        line = line.strip()
        if line and not line.startswith("#"):
             split_ = line.split("=", 1)
             if len(split_) == 2 and split_[0].isupper():
                 env_dict[split_[0]] = split_[1]
            # strip quotes if value is quoted
                 if env_dict[split_[0]].startswith('"') and env_dict[split_[0]].endswith('"'):
                     env_dict[split_[0]] = env_dict[split_[0]][1:-1]
                 elif env_dict[split_[0]].startswith("'") and env_dict[split_[0]].endswith("'"):
                     env_dict[split_[0]] = env_dict[split_[0]][1:-1]
            # Handle empty values
                 if env_dict[split_[0]] == "":
                     env_dict[split_[0]] = None
        
    return env_dict

    
    
    



if __name__ == "__main__":
    
    env_str = """
    DB_HOST=localhost
    DB_PORT=5432
    # This is a comment
    API_KEY="secret-key-123"

    DEBUG=true
    """
    
    print(parse_env(env_str))
    print(parse_env("NAME=app"))
    print(parse_env("VERSION=1.0.0 ENV=production"))
    print(parse_env("# only comments"))
    print(parse_env("FOO="))
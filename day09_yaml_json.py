import json
import yaml

def yaml_to_json(str):
    
    data = yaml.safe_load(str)
    json_string = json.dumps(data, indent=2)
    
    return json_string
    
    
    



if __name__ == "__main__":
    
    yaml_str = "name: app\nport: 8080"
    print(yaml_to_json(yaml_str))
    
    yaml_str = "items:\n  - one\n  - two\n  - three"
    print(yaml_to_json(yaml_str))
    
    yaml_str = "debug: true"
    print(yaml_to_json(yaml_str))
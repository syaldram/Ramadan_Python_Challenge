import re

def is_valid_semver(semver: str):
    
    pattern = re.compile(r"^\d+\.\d+\.\d+$")
    return bool(pattern.match(semver))

    
    
def compare_semver(semver_v1: str, semver_v2: str):
    
    v1 = tuple(int(x) for x in semver_v1.split("."))
    v2 = tuple(int(x) for x in semver_v2.split("."))
    
    if v1 > v2:
        return semver_v1
    elif v1 == v2:
        return "equal"
    else:
        return semver_v2

    
    

if __name__ == "__main__":
    
    print(is_valid_semver("1.0.0"))
    print(is_valid_semver("2.11.3"))
    print(is_valid_semver("1.0"))
    print(is_valid_semver("abc.def.ghi"))
    print(is_valid_semver("1.0.0.0"))
    print(is_valid_semver("2.11.30"))
    print("""""")
    print("""""")
    print("""""")
    
    print(compare_semver("1.2.3", "1.2.4"))
    print(compare_semver("2.0.0", "1.9.9"))
    print(compare_semver("1.0.0", "1.0.0"))
    print(compare_semver("1.9.0", "1.10.0"))
    
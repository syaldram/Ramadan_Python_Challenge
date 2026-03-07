
def longest_prefix(list_of_strings):
    if not list_of_strings:
        return ""

    prefix = list_of_strings[0]

    for string in list_of_strings[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix



if __name__ == "__main__":
    
    print(longest_prefix(["s3://bucket/logs/2026/", "s3://bucket/logs/2025/"]))
    print(longest_prefix(["s3://data/raw/", "s3://data/processed/"]))
    print(longest_prefix(["flower", "flow", "flight"]))
    print(longest_prefix(["only_one"]))
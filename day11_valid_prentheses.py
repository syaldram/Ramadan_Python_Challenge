
def is_valid(s: str) -> bool:
    
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    return not stack
    
    

if __name__ == "__main__":
    print(is_valid("()"))
    print(is_valid("(]"))
    print(is_valid("{[()]}"))
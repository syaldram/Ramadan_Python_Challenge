import collections

def rotate(lst: list, num: int):
    
    #d = collections.deque(lst)
    #d.rotate(num)
    
    #return list(d)
    
    #return lst[-num:] + lst[:-num]
    
    num = num % len(lst)  # Handle cases where num > len(lst)
    # reverse entire list
    lst.reverse()
    # reverse first num elements
    lst[:num] = reversed(lst[:num])
    # reverse remaining elements
    lst[num:] = reversed(lst[num:])
    return lst



if __name__ == "__main__":
    
    print(rotate([1, 2, 3, 4, 5], 2))
    print(rotate([10, 20, 30, 40], 1))
    print(rotate([1, 2, 3], 3))
    print(rotate([1, 2, 3], 5))
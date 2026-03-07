from collections import deque

def merge_sorted(lst1: list, lst2: list):
    
    results = []
    i =0
    j = 0
    
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            results.append(lst1[i])
            i +=1
        else:
            results.append(lst2[j])
            j +=1
    
    if i < len(lst1):
        results.extend(lst1[i:])
    elif j < len(lst2):
        results.extend(lst2[j:])
        
    return results



if __name__ == "__main__":
    
    print(merge_sorted([1, 3, 5], [2, 4, 6]))
    print(merge_sorted([1, 2, 3], []))
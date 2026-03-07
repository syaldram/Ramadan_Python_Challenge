from collections import defaultdict

def group_anagrams(words):
    anagram_groups = defaultdict(list)
    
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagram_groups[sorted_word].append(word)
    
    return list(anagram_groups.values())

if __name__ == "__main__":
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # ➞ [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    
    print(group_anagrams(["listen", "silent", "enlist"]))
    # ➞ [["listen", "silent", "enlist"]]
    
    print(group_anagrams(["hello", "world"]))
    # ➞ [["hello"], ["world"]]
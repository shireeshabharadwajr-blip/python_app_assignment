from collections import Counter

def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

if __name__ == "__main__":
    print("Example 1:", isAnagram("anagram", "nagaram"))
    print("Example 2:", isAnagram("rat", "car"))

def lengthOfLongestSubstring(s: str) -> int:
    visited = [False] * 26
    left = 0
    max_len = 0
    for right in range(len(s)):
        idx = ord(s[right]) - ord('a')
        while visited[idx]:
            visited[ord(s[left]) - ord('a')] = False
            left += 1
        visited[idx] = True
        max_len = max(max_len, right - left + 1)
    return max_len

if __name__ == "__main__":
    print("Example 1:", lengthOfLongestSubstring("abcabcbb"))
    print("Example 2:", lengthOfLongestSubstring("bbbbb"))
    print("Example 3:", lengthOfLongestSubstring("pwwkew"))

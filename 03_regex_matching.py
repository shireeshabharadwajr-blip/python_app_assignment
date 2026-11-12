def isMatch(s: str, p: str) -> bool:
    memo = {}
    def dp(i, j):
        if (i, j) in memo: return memo[(i, j)]
        if j == len(p): return i == len(s)
        first_match = i < len(s) and p[j] in {s[i], '.'}
        if j + 1 < len(p) and p[j + 1] == '*':
            ans = dp(i, j + 2) or (first_match and dp(i + 1, j))
        else:
            ans = first_match and dp(i + 1, j + 1)
        memo[(i, j)] = ans
        return ans
    return dp(0, 0)

if __name__ == "__main__":
    print("Example 1:", isMatch("abcd", ".*"))
    print("Example 2:", isMatch("mississippi", "mis*is*p*."))
    print("Example 3:", isMatch("aa", "a"))

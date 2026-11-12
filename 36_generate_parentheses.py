def generateParenthesis(n: int):
    res = []
    def backtrack(s, left, right):
        if len(s) == 2 * n:
            res.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)
    backtrack("", 0, 0)
    return res

if __name__ == "__main__":
    print("Example 1 (n=3):", generateParenthesis(3))
    print("Example 2 (n=1):", generateParenthesis(1))

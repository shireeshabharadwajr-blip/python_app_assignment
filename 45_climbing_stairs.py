def climbStairs(n: int):
    res = []
    def backtrack(curr, path):
        if curr == n:
            res.append("+".join(map(str, path)))
            return
        if curr + 1 <= n:
            backtrack(curr + 1, path + [1])
        if curr + 2 <= n:
            backtrack(curr + 2, path + [2])
    backtrack(0, [])
    return len(res), res

if __name__ == "__main__":
    for n in [2, 3, 4]:
        ways, pats = climbStairs(n)
        print(f"n={n} -> Total Ways: {ways}, Patterns: {pats}")

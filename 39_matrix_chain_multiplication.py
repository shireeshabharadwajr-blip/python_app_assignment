def matrixChainOrder(p):
    n = len(p)
    dp = [[0] * n for _ in range(n)]
    split = [[0] * n for _ in range(n)]
    for L in range(2, n):
        for i in range(1, n - L + 1):
            j = i + L - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + p[i-1] * p[k] * p[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k
                    
    def get_parens(i, j):
        if i == j:
            return f"A{i}"
        return f"({get_parens(i, split[i][j])} x {get_parens(split[i][j]+1, j)})"
        
    return dp[1][n-1], get_parens(1, n-1)

if __name__ == "__main__":
    cost1, parens1 = matrixChainOrder([10, 30, 5, 60])
    print("Example 1 -> Min Cost:", cost1, "| Optimal:", parens1)
    cost2, parens2 = matrixChainOrder([40, 20, 30, 10, 30])
    print("Example 2 -> Min Cost:", cost2, "| Optimal:", parens2)

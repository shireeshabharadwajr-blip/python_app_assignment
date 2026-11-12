def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i], dp[i - c] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == "__main__":
    print("Example 1:", coinChange([1, 2, 5], 11))
    print("Example 2:", coinChange([2], 3))
    print("Example 3:", coinChange([1], 0))

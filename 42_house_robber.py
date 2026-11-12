def rob(nums) -> int:
    prev1, prev2 = 0, 0
    for num in nums:
        tmp = max(prev1, prev2 + num)
        prev2 = prev1
        prev1 = tmp
    return prev1

if __name__ == "__main__":
    print("Example 1:", rob([1, 2, 3, 1]))
    print("Example 2:", rob([2, 7, 9, 3, 1]))

def maxProduct(nums) -> int:
    res = max(nums)
    curMin, curMax = 1, 1
    for n in nums:
        tmp = curMax * n
        curMax = max(n * curMax, n * curMin, n)
        curMin = min(tmp, n * curMin, n)
        res = max(res, curMax)
    return res

if __name__ == "__main__":
    print("Example 1:", maxProduct([2, 3, -2, 4]))
    print("Example 2:", maxProduct([-2, 0, -1]))

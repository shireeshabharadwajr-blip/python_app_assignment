def missingNumber(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)

if __name__ == "__main__":
    print("Example 1:", missingNumber([3, 0, 1]))
    print("Example 2:", missingNumber([0, 1]))
    print("Example 3:", missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))

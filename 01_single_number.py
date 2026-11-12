def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

if __name__ == "__main__":
    print("Example 1:", singleNumber([2, 2, 1]))
    print("Example 2:", singleNumber([4, 1, 2, 1, 2]))
    print("Example 3:", singleNumber([1]))

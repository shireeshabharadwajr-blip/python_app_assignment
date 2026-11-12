from collections import Counter

def sumOfUnique(nums):
    counts = Counter(nums)
    unique_elements = [k for k, v in counts.items() if v == 1]
    return unique_elements, sum(unique_elements)

if __name__ == "__main__":
    print("Example 1:", sumOfUnique([1, 3, 2, 3, 2, 4]))
    print("Example 2:", sumOfUnique([10, 20, 10, 30, 40, 30]))
    print("Example 3:", sumOfUnique([5, 5, 5, 5]))

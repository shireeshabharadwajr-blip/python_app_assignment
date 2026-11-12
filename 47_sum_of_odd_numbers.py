# 1. Using a regular function parameter
def sum_odd_regular(nums):
    total = 0
    for x in nums:
        if x % 2 != 0:
            total += x
    return total

# 2. Using list comprehension
def sum_odd_comprehension(nums):
    return sum([x for x in nums if x % 2 != 0])

# 3. Using a user-defined filter helper
def is_odd(x):
    return x % 2 != 0

def sum_odd_udf(nums):
    return sum(filter(is_odd, nums))

if __name__ == "__main__":
    sample = [1, 2, 3, 4, 5, 6]
    print("Regular:", sum_odd_regular(sample))
    print("Comprehension:", sum_odd_comprehension(sample))
    print("User-defined:", sum_odd_udf(sample))

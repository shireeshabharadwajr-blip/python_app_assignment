def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

if __name__ == "__main__":
    print("Example 1:", plusOne([1, 2, 3]))
    print("Example 2:", plusOne([4, 3, 2, 1]))
    print("Example 3:", plusOne([9]))

def hammingWeight(n: int) -> int:
    return bin(n).count('1')

if __name__ == "__main__":
    print("Example 1:", hammingWeight(11))
    print("Example 2:", hammingWeight(128))
    print("Example 3:", hammingWeight(2147483645))

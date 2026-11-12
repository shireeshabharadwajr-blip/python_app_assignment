def countTrailingZeros(n: int) -> int:
    if n == 0: return 1
    bin_str = bin(n)[2:]
    return len(bin_str) - len(bin_str.rstrip('0'))

if __name__ == "__main__":
    print("Example 1:", countTrailingZeros(8))
    print("Example 2:", countTrailingZeros(12))

def reverseBits(n: int) -> int:
    res = 0
    for _ in range(32):
        res = (res << 1) | (n & 1)
        n >>= 1
    return res

if __name__ == "__main__":
    print("Example 1:", reverseBits(43261596))
    print("Example 2:", reverseBits(2147483644))

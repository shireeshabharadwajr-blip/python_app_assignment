def toggleBit(n: int, k: int) -> int:
    return n ^ (1 << k)

if __name__ == "__main__":
    print("Example 1:", toggleBit(5, 1))
    print("Example 2:", toggleBit(4, 2))

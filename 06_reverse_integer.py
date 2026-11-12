def reverse(x: int) -> int:
    sign = -1 if x < 0 else 1
    rev = int(str(abs(x))[::-1]) * sign
    if rev < -2**31 or rev > 2**31 - 1:
        return 0
    return rev

if __name__ == "__main__":
    print("Example 1:", reverse(123))
    print("Example 2:", reverse(-123))
    print("Example 3:", reverse(120))

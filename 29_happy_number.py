def isHappy(n: int) -> bool:
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(c)**2 for c in str(n))
    return n == 1

if __name__ == "__main__":
    print("Example 1:", isHappy(19))
    print("Example 2:", isHappy(2))

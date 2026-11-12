def midpoint(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

if __name__ == "__main__":
    print("Example 1:", midpoint((0, 0), (4, 4)))
    print("Example 2:", midpoint((1, 3), (5, 7)))
    print("Example 3:", midpoint((-2, 4), (2, 0)))

def sum_of_cubes(a, b):
    return sum(i**3 for i in range(a, b + 1))

if __name__ == "__main__":
    print("Example 1:", sum_of_cubes(4, 9))
    print("Example 2:", sum_of_cubes(1, 3))
    print("Example 3:", sum_of_cubes(5, 5))

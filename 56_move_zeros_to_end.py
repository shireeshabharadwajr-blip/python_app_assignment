def moveZeros(l):
    non_zeros = [x for x in l if x != 0]
    zeros = [x for x in l if x == 0]
    return non_zeros + zeros

if __name__ == "__main__":
    print("Example 1:", moveZeros([0, 1, 0, 2, 0, 3]))
    print("Example 2:", moveZeros([4, 0, 5, 0, 2, 0, 8]))

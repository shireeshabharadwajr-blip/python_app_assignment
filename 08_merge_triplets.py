def mergeTriplets(triplets, target):
    res = [False, False, False]
    for t in triplets:
        if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
            if t[0] == target[0]: res[0] = True
            if t[1] == target[1]: res[1] = True
            if t[2] == target[2]: res[2] = True
    return all(res)

if __name__ == "__main__":
    print("Example 1:", mergeTriplets([[2,5,3],[1,8,4],[1,7,5]], [2,7,5]))
    print("Example 2:", mergeTriplets([[3,4,5],[4,5,6]], [3,2,5]))
    print("Example 3:", mergeTriplets([[2,5,3],[2,3,4],[1,2,5],[5,2,3]], [5,5,5]))

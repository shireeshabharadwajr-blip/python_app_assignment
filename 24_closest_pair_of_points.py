import math

def closestPair(points):
    min_dist = float('inf')
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            dist = math.hypot(points[i][0] - points[j][0], points[i][1] - points[j][1])
            if dist < min_dist:
                min_dist = dist
    return min_dist

if __name__ == "__main__":
    print("Example 1:", closestPair([(0, 0), (1, 1)]))
    print("Example 2:", closestPair([(1, 1), (2, 2), (5, 5)]))
    print("Example 3:", closestPair([(0, 0), (3, 4), (6, 8)]))

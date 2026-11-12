def maxArea(height) -> int:
    l, r = 0, len(height) - 1
    max_area = 0
    while l < r:
        area = (r - l) * min(height[l], height[r])
        max_area = max(max_area, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_area

if __name__ == "__main__":
    print("Example 1:", maxArea([1,8,6,2,5,4,8,3,7]))
    print("Example 2:", maxArea([1,1]))
    print("Example 3:", maxArea([4,3,2,1,4]))

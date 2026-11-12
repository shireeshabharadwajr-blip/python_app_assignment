def trap(height) -> int:
    if not height: return 0
    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]
    ans = 0
    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            ans += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            ans += rightMax - height[r]
    return ans

if __name__ == "__main__":
    print("Example 1:", trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print("Example 2:", trap([4,2,0,3,2,5]))

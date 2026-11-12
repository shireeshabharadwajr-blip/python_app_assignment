def solveMaze(maze):
    n = len(maze)
    sol = [[0] * n for _ in range(n)]
    
    def isSafe(x, y):
        return 0 <= x < n and 0 <= y < n and maze[x][y] == 1 and sol[x][y] == 0

    def solve(x, y):
        if x == n - 1 and y == n - 1 and maze[x][y] == 1:
            sol[x][y] = 1
            return True
            
        if isSafe(x, y):
            sol[x][y] = 1
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if solve(x + dx, y + dy):
                    return True
            sol[x][y] = 0
            return False
        return False

    if solve(0, 0):
        return sol
    return None

if __name__ == "__main__":
    maze1 = [[1, 0, 0, 0], [1, 1, 0, 1], [0, 1, 0, 0], [1, 1, 1, 1]]
    res1 = solveMaze(maze1)
    print("Example 1:")
    if res1:
        for r in res1: print(" ".join(map(str, r)))
    else:
        print("No solution exists")

def spiralOrder(matrix):
    res = []
    while matrix:
        res.extend(matrix.pop(0))
        if matrix and matrix[0]:
            for row in matrix:
                res.append(row.pop())
        if matrix:
            res.extend(matrix.pop()[::-1])
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                res.append(row.pop(0))
    return res

if __name__ == "__main__":
    print("Example 1:", spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print("Example 2:", spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

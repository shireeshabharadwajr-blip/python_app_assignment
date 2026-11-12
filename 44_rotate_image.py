def rotate(matrix) -> None:
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

if __name__ == "__main__":
    m = [[1,2,3],[4,5,6],[7,8,9]]
    rotate(m)
    print("Rotated:", m)

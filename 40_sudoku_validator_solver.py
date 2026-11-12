def solveSudoku(board):
    # Initial validation
    for i in range(9):
        rows, cols, box = set(), set(), set()
        for j in range(9):
            if board[i][j] != '.':
                if board[i][j] in rows: return False, f"Duplicate '{board[i][j]}' in row {i+1}"
                rows.add(board[i][j])
            if board[j][i] != '.':
                if board[j][i] in cols: return False, f"Duplicate '{board[j][i]}' in col {i+1}"
                cols.add(board[j][i])
            r, c = 3 * (i // 3) + j // 3, 3 * (i % 3) + j % 3
            if board[r][c] != '.':
                if board[r][c] in box: return False, f"Duplicate '{board[r][c]}' in sub-grid {i+1}"
                box.add(board[r][c])

    def isValid(board, row, col, c):
        for i in range(9):
            if board[i][col] == c or board[row][i] == c: return False
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c: return False
        return True

    def backtrack(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for c in '123456789':
                        if isValid(board, i, j, c):
                            board[i][j] = c
                            if backtrack(board): return True
                            board[i][j] = '.'
                    return False
        return True

    backtrack(board)
    return True, board

if __name__ == "__main__":
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    valid, result = solveSudoku(board)
    print("Valid Sudoku:", valid)
    if valid:
        for row in result:
            print(" ".join(row))

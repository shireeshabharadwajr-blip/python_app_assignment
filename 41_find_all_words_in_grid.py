def findWords(board, words):
    trie = {}
    for w in words:
        node = trie
        for ch in w:
            node = node.setdefault(ch, {})
        node['$'] = w
        
    res = set()
    rows, cols = len(board), len(board[0])
    
    def dfs(r, c, node):
        ch = board[r][c]
        if ch not in node: return
        curr = node[ch]
        if '$' in curr:
            res.add(curr['$'])
            
        board[r][c] = '#'
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                dfs(nr, nc, curr)
        board[r][c] = ch

    for i in range(rows):
        for j in range(cols):
            dfs(i, j, trie)
    return list(res)

if __name__ == "__main__":
    board = [
        ["o","a","a","n"],
        ["e","t","a","e"],
        ["i","h","k","r"],
        ["i","f","l","v"]
    ]
    words = ["oath","pea","eat","rain"]
    print("Found Words:", findWords(board, words))

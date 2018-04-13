def getAdj(board, row, col):
    adjChars = {}
    adjs = set((dy,dx) for dy in range(-1,2) for dx in range(-1,2))
    adjs.discard((0,0))
    for adj in adjs:
        dr, dc = adj
        nr = row + dr
        nc = col + dc
        if (nr >= 0 and nr < len(board) and nc >= 0 and nc < len(board[row])):
            if board[nr][nc] not in adjChars:
                adjChars[board[nr][nc]] = set()
            adjChars[board[nr][nc]].add(adj)
    return adjChars
def findCoords(board, char):
    coords = set()
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == char:
                coords.add((row,col))
    return coords
def findWord(board, adjBoard, word):
    if len(word) > 0:
        coords = findCoords(board, word[0])
        for start in coords:
            visited = set()
            if (findWordH(adjBoard, word[1:], start, visited)):
                return True
    return False
def findWordH(adjBoard, word, pos, visited):
    if len(word) == 0:
        return True
    visited.add(pos)
    r,c = pos
    char = word[0]
    if char in adjBoard[r][c]:
        for adj in adjBoard[r][c][char]:
            dr, dc = adj
            nr = r+dr
            nc = c+dc
            if (nr,nc) not in visited:
                if (findWordH(adjBoard, word[1:], (nr,nc), visited)):
                    return True
    visited.discard(pos)
    return False
def wordBoggle(board, words):
    adjBoard = [[getAdj(board, row, col) for col in range(len(board[row]))] for row in range(len(board))]
    return sorted([word for word in words if findWord(board, adjBoard, word)])

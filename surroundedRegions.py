from collections import deque


def main():
    board = [["O","O","O"],["O","O","O"],["O","O","O"]]

    rows = len(board)
    columns = len(board[0])
    visit = set()

    def bfs(row, column):
        q = deque()
        q.append((row, column))
        visit.add((row, column))
        while q:
            r, c = q.popleft()
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                if (dr + r >= 0 and dr + r < rows and dc + c >= 0
                        and dc + c < columns and board[dr + r][dc + c] == "O"
                        and not (r+dr, c+dc) in visit):
                    visit.add((dr + r, dc + c))
                    q.append((dr + r, dc + c))
                    board[dr + r][dc + c] = "T"

    for r in range(rows):
        if (board[r][0] == "O" and not (r, 0) in visit):
            visit.add((r, 0))
            bfs(r, 0)
            board[r][0] = "T"
        if (board[r][columns - 1] == "O" and not (r, columns - 1) in visit):
            visit.add((r, columns - 1))
            bfs(r, columns - 1)
            board[r][columns - 1] = "T"

    for c in range(columns):
        if (board[0][c] == "O" and not (0, c) in visit):
            visit.add((0, c))
            bfs(0, c)
            board[0][c] = "T"
        if (board[rows - 1][c] == "O" and not (rows - 1, c) in visit):
            visit.add((rows - 1, c))
            bfs(rows - 1, c)
            board[rows - 1][c] = "T"

    for r in range(rows):
        for c in range(columns):
            if board[r][c] == "T":
                board[r][c] = "O"
            else:
                board[r][c] = "X"
    print(board)
    print(visit)
if __name__ == "__main__":
    main()
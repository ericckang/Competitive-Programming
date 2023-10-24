def numIslands(grid):
    row = len(grid)
    column = len(grid[0])
    count = 0
    for r in range (row):
        for c in range (column):
            if grid[r][c] == 1:
                bfs(r,c)
                count += 1



    return 0


def main():
    print(numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))



if __name__ == "__main__":
    main()

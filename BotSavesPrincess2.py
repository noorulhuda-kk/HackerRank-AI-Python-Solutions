def nextMove(n, r, c, grid):
    #We know bot's position as r and c variable
    #it's time to calcullate princess position
    #unfortunately we ll have to traverse the all grid until princess is found. because princess can be anywhere
    princess_row = princess_col = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p':
                princess_row, princess_col = i, j
                break

    #Calculate the first next move. Here, i am giving priority to horizontal movement over vertical
    if princess_col < c:
        return "LEFT"
    elif princess_col > c:
        return "RIGHT"
    elif princess_row < r:
        return "UP"
    elif princess_row > r:
        return "DOWN"

n = int(input())
r, c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n, r, c, grid))
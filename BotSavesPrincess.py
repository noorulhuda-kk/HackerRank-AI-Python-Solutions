def displayPathtoPrincess(n, grid):
    # print all the moves here

    # we know bot is at center always, so
    botRow = botColumn = (n // 2)
    princessRow = princessColumn = 0

    # princess is at one of the corner
    for i in [0, n - 1]:
        for j in [0, n - 1]:
            if grid[i][j] == 'p':
                princessRow = i
                princessColumn = j
                break

    # Now we know the location of princess, lets calculate distance of bot and princess
    rDistance = botRow - princessRow
    cDistance = botColumn - princessColumn

    #Moving the bot to princess while considering the fact that
    #if row distance is -ve, princess is below the bot, -ve --> above
    #same goes with column distance, -ve means right side, +ve means left side
    while rDistance != 0:
        if (rDistance < 0):
            print("DOWN")
            rDistance += 1
        elif (rDistance > 0):
            print("UP")
            rDistance -= 1
    while cDistance != 0:
        if (cDistance < 0):
            print("RIGHT")
            cDistance += 1
        elif (cDistance > 0):
            print("LEFT")
            cDistance -= 1

    #we can also combine the while loop, but then it will move it zigzag
    '''
    while (rDistance != 0 or cDistance != 0):
        if (rDistance < 0):
            print("DOWN")
            rDistance += 1
        elif (rDistance > 0):
            print("UP")
            rDistance -= 1
        if (cDistance < 0):
            print("RIGHT")
            cDistance += 1
        elif (cDistance > 0):
            print("LEFT")
            cDistance -= 1 
        '''


m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)

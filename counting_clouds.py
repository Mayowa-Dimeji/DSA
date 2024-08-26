# The problem typically involves a grid (2D array) where each cell can either represent part of a cloud (1) or clear sky (0). A cloud is defined as a contiguous block of 1s, either connected horizontally or vertically. The goal is to count the number of distinct clouds in the grid.
def counting_clouds(sky):
    if not sky:
        return 0

    def dfs(sky, i, j):
        if i < 0 or i >= len(sky) or j < 0 or j >= len(sky[0]) or sky[i][j] == '0':
            return
        sky[i][j] = '0'

        # check up, down,left and right
        dfs(sky, i-1, j)
        dfs(sky, i+1, j)
        dfs(sky, i, j-1)
        dfs(sky, i, j+1)

    count = 0
    for i in range(len(sky)):
        for j in range(len(sky[0])):
            if sky[i][j] == '1':
                dfs(sky, i, j)
                count += 1
    return count

class Solution:
    def numIslands(self, iceland_space):
        column = len(iceland_space)
        row = len(iceland_space[0]) if column else 0
        def space(i, j):
            if i < 0 or j < 0 or i == column or j == row or iceland_space[i][j] != "1":
                return None

            iceland_space[i][j] = "0"
            space(i - 1, j)
            space(i + 1, j)
            space(i, j - 1)
            space(i, j + 1)

        count = 0
        for i in range(column):
            for j in range(row):
                if iceland_space[i][j] == "1":
                    space(i, j)
                    count += 1

        return count


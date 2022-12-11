class Solution:
    def islandPerimeter(self, space: List[List[int]]) -> int:
        horizontals = len(space)
        verticals = len(verticals[0])

        que_islands = 0
        hello_neighbour = 0 

        for element in range(horizontals):
            for coordinate in range(verticals):
                if space[element][coordinate] == 1:
                    que_islands += 1
                    if element + 1 < horizontals and space[element + 1][coordinate] == 1:
                        hello_neighbour += 1 
                    if coordinate + 1 < verticals and space[element][coordinate+1] == 1:
                        hello_neighbour += 1 
        return que_islands * 4 - hello_neighbour * 2 

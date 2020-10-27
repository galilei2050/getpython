'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

'''


def max_area_of_island(grid) -> int:
    max_y = len(grid) - 1
    max_x = len(grid[0]) - 1
    visited = set()
    max_area = 0

    def get_area(x, y):
        this_area = 1
        visited.add((x, y))
        queue = [(x, y)]
        while queue:
            x, y = queue.pop(0)
            for point in [(x-1, y), (x+1, y),
                            (x, y-1), (x, y+1)]:
                if point in visited:
                    continue
                x, y = point
                if x < 0 or y < 0 or x > max_x or y > max_y:
                    continue
                if grid[y][x] == 0:
                    continue
                this_area += 1
                visited.add(point)
                queue.append(point)
        return this_area

    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            if grid[y][x] == 0 or (x, y) in visited:
                continue
            max_area = max(max_area, get_area(x, y))
    return max_area


print(max_area_of_island([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                          [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                          [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))

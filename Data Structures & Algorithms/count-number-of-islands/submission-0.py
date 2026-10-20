
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        islands = 0

        directions = [
            (-1, 0),  # up
            (1, 0),   # down
            (0, -1),  # left
            (0, 1)    # right
        ]

        for row in range(rows):
            for col in range(cols):

                # Skip water or land already explored
                if grid[row][col] == "0" or (row, col) in visited:
                    continue

                # New island discovered
                islands += 1

                stack = [(row, col)]
                visited.add((row, col))

                # Explore this entire island
                while stack:
                    current_row, current_col = stack.pop()

                    for dr, dc in directions:
                        nr = current_row + dr
                        nc = current_col + dc

                        # Check grid boundaries
                        if not (0 <= nr < rows and 0 <= nc < cols):
                            continue

                        # Skip water or previously visited land
                        if grid[nr][nc] == "0" or (nr, nc) in visited:
                            continue

                        # Discover a connected land cell
                        visited.add((nr, nc))
                        stack.append((nr, nc))

        return islands

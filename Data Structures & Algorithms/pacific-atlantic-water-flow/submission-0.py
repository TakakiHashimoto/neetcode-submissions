from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows = len(heights)
        cols = len(heights[0])

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        def dfs(starts):
            visited = set(starts)
            stack = list(starts)

            while stack:
                row, col = stack.pop()

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if not (0 <= nr < rows and 0 <= nc < cols):
                        continue

                    if (nr, nc) in visited:
                        continue

                    if heights[nr][nc] < heights[row][col]:
                        continue

                    visited.add((nr, nc))
                    stack.append((nr, nc))

            return visited

        pacific_starts = (
            [(0, c) for c in range(cols)] +
            [(r, 0) for r in range(rows)]
        )

        atlantic_starts = (
            [(rows - 1, c) for c in range(cols)] +
            [(r, cols - 1) for r in range(rows)]
        )

        pacific = dfs(pacific_starts)
        atlantic = dfs(atlantic_starts)

        return [[r, c] for r, c in pacific & atlantic]
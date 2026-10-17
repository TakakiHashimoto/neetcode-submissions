
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(row, col, index):
            # 1. Check boundaries
            if row < 0 or row >= rows:
                return False

            if col < 0 or col >= cols:
                return False

            # 2. Reject already-used cells
            if (row, col) in visited:
                return False

            # 3. Check the current character
            if board[row][col] != word[index]:
                return False

            # 4. Have we matched the entire word?
            if index == len(word) - 1:
                return True

            # 5. Mark the current cell as visited
            visited.add((row, col))

            directions = [
                (-1, 0),
                (1, 0),
                (0, -1),
                (0, 1)
            ]

            # 6. Explore each neighboring cell
            for dr, dc in directions:
                if dfs(row + dr, col + dc, index + 1):
                    visited.remove((row, col))
                    return True

            # 7. Backtrack
            visited.remove((row, col))
            return False

        # 8. Try every cell as a starting point
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False

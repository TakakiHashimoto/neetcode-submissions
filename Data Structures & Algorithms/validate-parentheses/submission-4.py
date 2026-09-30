class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in s:
            # Opening bracket
            if char in "([{":
                stack.append(char)

            # Closing bracket
            else:
                # Nothing available to close
                if not stack:
                    return False

                # Most recent opening bracket must match
                if stack[-1] != pairs[char]:
                    return False

                stack.pop()

        # Every opening bracket must have been closed
        return len(stack) == 0
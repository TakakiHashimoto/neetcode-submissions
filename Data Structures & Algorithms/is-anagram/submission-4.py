class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

# alphabetically sort and the two need to be same
        return sorted(s) == sorted(t)
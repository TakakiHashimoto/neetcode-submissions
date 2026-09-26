class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortedSet = sorted(set(nums)) # { -1, 0, 3,4,5,6,7,8,9} for example
        streak = 0
        streak_list = []
        expected = 0 
        if len(nums) == 0:
            return 0
        for i, item in enumerate(sortedSet):
            if i == 0:
                expected = item + 1
                streak += 1
                streak_list.append(streak)
            else:
                if item == expected:
                    streak += 1
                    expected = item + 1
                    streak_list.append(streak)
                else:
                    expected = item + 1
                    streak_list.append(streak)
                    streak = 1

        return sorted(streak_list, reverse=True)[0]


# My solution
class Solution:
    # [A, B, B, A]
    # [A, B, C, C, C, C]
    # [A, A, B, C, D, D, D] k = 2
    def characterReplacement(self, s: str, k: int) -> int:
        # まず連続を見つける find the consecutive
        # 連続が途切れるまでwindowを伸ばす elongate the window until the consecutive ends
        # 途切れたら、substitudeする substitude the char and cycle back
        # 繰り返して、kがゼロになるまでやる
        # return the longest length
        consecutives = set()
        beginning = 0
        trail = beginning + 1
        try_counts = 0
        max_length = 0

        while beginning < len(s):
            if s[beginning] != s[trail]:
                beginning += 1
                continue
            while try_counts < k:
                if trail >= len(s):
                    try_counts += 1
                elif s[beginning] != s[trail]:
                    try_counts += 1
                trail += 1
            max_length = max(max_length, trail - beginning + 1)
            beginning = trail + 1

        return max_length
                
            

# ChatGPT
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_frequency = 0
        max_length = 0

        for right in range(len(s)):
            char = s[right]

            count[char] = count.get(char, 0) + 1

            max_frequency = max(
                max_frequency,
                count[char]
            )

            while (right - left + 1) - max_frequency > k:
                count[s[left]] -= 1
                left += 1

            max_length = max(
                max_length,
                right - left + 1
            )

        return max_length
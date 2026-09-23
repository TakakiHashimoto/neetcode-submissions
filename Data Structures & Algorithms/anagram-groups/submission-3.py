class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pair = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in pair.keys():
                pair[sorted_word].append(word)
            else:
                pair[sorted_word] = [word]

        return list(pair.values())

        
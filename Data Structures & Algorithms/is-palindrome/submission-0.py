class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        clensed_chars = []
        for char in s:
            if char in alphanumeric_list:
                clensed_chars.append(char.lower())
        trimed_word = "".join(clensed_chars)
        i = 0
        j = -1
        for _ in range(int(len(trimed_word) / 2)):
            if trimed_word[i] != trimed_word[j]:
                return False
            j -= 1
            i += 1

        return True

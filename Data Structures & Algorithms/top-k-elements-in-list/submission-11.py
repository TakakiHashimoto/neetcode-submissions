class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        sorted_frequency = sorted(frequency.items(),key=lambda item: item[1],
        reverse=True)[:k]
        # frequency.items() = [(3,4), (1,3), (4,5)...]
        # lambda = like a callback function in js, item[1] is the right side of tuble

        return [num for num, count in sorted_frequency[:k]]
        
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = []
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    pair.append(i)
                    pair.append(j)
                    return pair
                j += 1

        return pair
        
                
        
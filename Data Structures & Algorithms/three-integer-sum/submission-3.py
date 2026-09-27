## my solution
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         i = 0
        
#         res = []
#         while i < len(nums) - 2:
#             j = i + 1
#             while j < len(nums) - 1:
#                 k = j + 1
#                 while k < len(nums):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         res.append([nums[i], nums[j], nums[k]])
#                     k += 1
#                 j += 1
#             i += 1

#         return res

## optimal solution
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        for i in range(len(nums) - 2):

            # Don't process the same first number twice
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1

                elif total > 0:
                    right -= 1

                else:
                    res.append([
                        nums[i],
                        nums[left],
                        nums[right]
                    ])

                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return res
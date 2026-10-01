# class Solution:
#     # [32, 44, 47, 10, 17]
#     def findMin(self, nums: List[int]) -> int:
#         search_array = nums
#         while len(search_array) != 1:
#             index = int(len(search_array) / 2 - 1)
#             target_num = search_array[index]
#             if target_num > search_array[0] and target_num > search_array[-1]:
#                 search_array = search_array[index:]
#             elif target_num < search_array[0]:
#                 search_array = search_array[:index]
#             elif target_num > search_array[0] and target_num < search_array[-1]:
#                 search_array = search_array[0:1]

#         return search_array[0]        

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
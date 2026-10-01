class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the sorted half
        # if target in between the sorted half?
        # keeps shrinking the array
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2

            if nums[middle] == target:
                return middle

            # Left half is sorted
            if nums[left] <= nums[middle]:

                # Target belongs inside the sorted left half
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1

            # Otherwise, right half must be sorted
            else:

                # Target belongs inside the sorted right half
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1

        return -1
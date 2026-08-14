class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)

        if n == 0:
            return 0

        if n == 1:
            return 1

        i = 0
        j = 1

        while j < n:
            if nums[i] != nums[j]:
                nums[i + 1] = nums[j]
                i += 1
            j += 1

        return i + 1
        
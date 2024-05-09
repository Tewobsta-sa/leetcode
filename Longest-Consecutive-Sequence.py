class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        count = 1
        cur = 1

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                cur += 1
            elif nums[i] != nums[i-1]:
                count = max(count, cur)
                cur = 1

        count = max(count, cur)

        return count

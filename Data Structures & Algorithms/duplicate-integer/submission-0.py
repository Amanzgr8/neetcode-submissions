class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        index = 1
        for i in nums:
            if index < len(nums) and i == nums[index]:
                return True
            else:
                index += 1
                continue
        return False
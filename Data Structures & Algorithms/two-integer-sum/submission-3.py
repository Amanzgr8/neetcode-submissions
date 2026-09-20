class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2 = sorted(nums)
        index1 = 0
        index2 = len(nums) - 1
        index3 = 0
        index4 = 0
        while index2 > index1:
            if nums2[index1] + nums2 [index2] == target:
                break
            elif nums2[index1] + nums2 [index2] > target:
                index2 -= 1
            elif nums2[index1] + nums2 [index2] < target:
                index1 += 1

        for i in nums:
            if i == nums2[index1]:
                break
            index3 += 1
        for i in nums:
            if i == nums2[index2] and index3 != index4:
                break
            index4 += 1
        return sorted([index3, index4])
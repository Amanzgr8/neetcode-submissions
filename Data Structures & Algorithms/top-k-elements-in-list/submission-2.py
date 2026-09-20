class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        counter = 0
        numsDict = {}
        largerNum = 0
        for i in nums:
            numsDict[i] = numsDict.get(i,0) + 1
        while counter < k:
            largerOcc = 0
            for i in numsDict:
                if numsDict[i] > largerOcc:
                    largerOcc = numsDict[i]
                    largerNum = i
            del numsDict[largerNum]
            output.append(largerNum)
            counter += 1
        return output
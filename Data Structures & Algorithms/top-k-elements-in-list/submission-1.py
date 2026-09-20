class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        counter = 0
        numsDict = {}
        for i in nums:
            numsDict[i] = numsDict.get(i,0) + 1
        while counter < k:
            #largerOcc = 0
            largerNum = 0
            for i in numsDict:
                if numsDict[i] >= numsDict.get(largerNum,0):
                    #largerOcc = numsDict[i]
                    largerNum = i
            del numsDict[largerNum]
            output.append(largerNum)
            counter += 1
        return output
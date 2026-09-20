class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strList = []
        strDict = {}
        finalList = []
        index = 0
        for i in strs:
            strList.append("".join(sorted(i)))
        for i in strList:
            helper = strDict.get(i, [])
            helper.append(index)
            strDict[i] = helper
            index += 1
        for i in strDict:
            smlList = []
            for x in strDict[i]:
                smlList.append(strs[x])
            finalList.append(smlList)
        return finalList
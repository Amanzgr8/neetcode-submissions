class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) >= 3:
            index1 = 0
            index2 = index1 + 2
            maxMiddle = height[index1+1]
            output = []
        else:
            return 0
            
        while index2 < len(height):
            if maxMiddle >= height[index1]: #or  
                index1 += 1
                index2 += 1
                maxMiddle = height[index1+1]

            elif maxMiddle >= height[index2]:
                if height[index1] > height[index2] and (index2 + 1) < len(height):
                    maxMiddle = max(maxMiddle, height[index2])
                    index2 += 1
                else:
                    index1 += 1
                    index2 = index1 + 2
                    maxMiddle = height[index1+1]
                    
            else:
                output.append((index2 - index1 - 1) * (min(height[index2], height[index1])- maxMiddle))
            
                if height[index1] > height[index2] and (index2 + 1) < len(height):
                    maxMiddle = max(maxMiddle, height[index2])
                    index2 += 1
                else:
                    index1 += 1
                    index2 = index1 + 2
                    maxMiddle = height[index1+1]

        return sum(output)
        
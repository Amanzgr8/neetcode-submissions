class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers) - 1 
        output = []
        while index2 > index1:
            if numbers[index1] + numbers[index2] == target:
                output.append(index1 + 1)
                output.append(index2 + 1)
                return output
            elif numbers[index1] + numbers[index2] > target:
                index2 -= 1
            elif numbers[index1] + numbers[index2] < target:
                index1 += 1
        
             
        
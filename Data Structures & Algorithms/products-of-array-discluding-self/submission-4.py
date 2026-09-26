class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        product  = 0
        hasZero = False
        zeroCount = 0

        for i in nums:
            if i == 0:
                hasZero = True
                zeroCount += 1
                continue
            else:
                if product == 0:
                    product = 1
                product *= i

        for i in nums:
            if i == 0 and zeroCount < 2:
                output.append(product)
            else:
                if hasZero:
                    output.append(0)
                else:
                    output.append(round(product * (i**-1)))
        return output
        
        
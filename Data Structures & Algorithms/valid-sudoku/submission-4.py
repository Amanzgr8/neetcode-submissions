class Solution:
    def is_int(s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        internalDict = {}
        internalDict2 = {}
        internalDict3 = {}
        dotKey = 10
        index2 = 0
        counterX = 0
        counterY = 0

        for i in board:
            internalDict = {}
            for j in i:
                if j != ".":
                    internalDict[j] = ""
                else:
                     internalDict[dotKey] = ""
                     dotKey += 1
            if len(internalDict) != 9:
                return False
                
        while index2 < 9:
            internalDict = {}
            index = 0
            while index < 9:
                if board[index][index2] != ".":
                    internalDict[board[index][index2]] = ""
                else:
                     internalDict[dotKey] = ""
                     dotKey += 1
                index += 1 
            if len(internalDict) != 9:
                return False
            index2 += 1

    
        for i in board:
            counterX = 0
            if counterY == 0 or counterY == 3 or counterY == 6:
                internalDict = {}
                internalDict2 = {}
                internalDict3 = {}
            for j in i:
                if counterX < 3:
                    if j != ".":
                        internalDict[j] = ""
                    else:
                        internalDict[dotKey] = ""
                        dotKey += 1
                elif counterX < 6:
                    if j != ".":
                        internalDict2[j] = ""
                    else:
                        internalDict2[dotKey] = ""
                        dotKey += 1
                elif counterX < 9:
                    if j != ".":
                        internalDict3[j] = ""
                    else:
                        internalDict3[dotKey] = ""
                        dotKey += 1
                counterX += 1
            counterY += 1

            if counterY == 3 or counterY == 6 or counterY == 9:
                if len(internalDict) != 9:
                    return False
                elif len(internalDict2) != 9:
                    return False
                elif len(internalDict3) != 9:
                    return False

        return True


        

        
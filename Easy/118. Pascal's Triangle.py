class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = [[1]]
        if numRows == 1: return result
        result.append([1, 1])
        if numRows == 2: return result
        result.append([1, 2, 1])
        if numRows == 3: return result
        
        currRow = 3
        while currRow < numRows:
            req_calcs = currRow - 1
            tmp = [1, 1]
            for i in range(req_calcs):
                tmp.insert(i+1, result[currRow-1][i] + result[currRow-1][i+1])
                    
            result.append(tmp)
            currRow += 1 
            
        return result

s = Solution()

r = s.generate(6)

print(r)

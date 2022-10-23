class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = [[1]]
        if numRows == 1: return result
        result.append([1, 1])
        if numRows == 2: return result
        result.append([1, 2, 1])
        if numRows == 3: return result
        
        p = 3
        while p is not numRows:
            for i in len(result[p-2]):
                
            p += 1 
            
        print(result)  
        return result

s = Solution()

r = s.generate(4)

print(r)

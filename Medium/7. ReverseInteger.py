class Solution:
    def reverse(self, x: int) -> int:
        if x > -10 and x < 10:
            return x
        
        rev = int(str(x)[::-1]) if x > 0 else int(str(x)[:0:-1])*-1
        if rev >= -2**31 and rev <= 2**31 - 1:
            return rev
        return 0
        
s = Solution()

print(s.reverse(-811))
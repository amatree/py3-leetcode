class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        if n == 3: return 3
        return self.climbStairs(n-1) + self.climbStairs(n-2)
        # TODO: use another method since recursion gets exponentially expensive after 30s 
        
        
# n = 2 => 2
# n = 3 => 3
# n = 4 => 5
# n = 5 => 8
# n = 6 => 13
# n = 7 => 21
# n = 8 => 34
# n = 9 => 55
# n = 10 => 89
        
s = Solution()
print(s.climbStairs(38))
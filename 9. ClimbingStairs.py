class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        if n == 3: return 3
        
        a = [0]*(n-3)
        a.insert(0, 3)
        a.insert(0, 2)
        a.insert(0, 1)
        i = 3
        while i < n:
            a[i] = a[i-1] + a[i-2]
            i += 1
        
        return a[n-1]
        
# n = 2 => 2
# n = 3 => 3
# n = 4 => 5
# n = 5 => 8
# n = 6 => 13
# n = 7 => 21
# n = 8 => 34
# n = 9 => 55
# n = 10 => 89

# n = 5
[1, 1, 1, 1, 1] #1
[1, 1, 1, 2] #4 
[1, 2, 2] #3 [1, 2, 2] [2, 1, 2] [2, 2, 1]

# n = 6
[1, 1, 1, 1, 1, 1] #1
[1, 1, 1, 1, 2] #5 [1, 1, 1, 1, 2] [1, 1, 1, 2, 1] [1, 1, 2, 1, 1] [1, 2, 1, 1, 1] [2, 1, 1, 1, 1]
[1, 1, 2, 2] #6 [1, 1, 2, 2] [1, 2, 1, 2] [2, 1, 1, 2] [2, 1, 2, 1] [2, 2, 1, 1] [1, 2, 2, 1]
[2, 2, 2] #1

# n = 7
[1, 1, 1, 1, 1, 1, 1] #1
[1, 1, 1, 1, 1, 2] #6
[1, 1, 1, 2, 2] #9
                # [1, 1, 1, 2, 2] [1, 1, 2, 1, 2] [1, 2, 1, 1, 2] [2, 1, 1, 1, 2] 
                # [2, 1, 1, 2, 1] [2, 1, 2, 1, 1] [2, 2, 1, 1, 1]
                # [1, 1, 2, 2, 1] [1, 2, 2, 1, 1]
[1, 2, 2] #3



s = Solution()
print(s.climbStairs(10))
# print(s.climbStairs(38))
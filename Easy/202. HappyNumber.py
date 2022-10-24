class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1: return True
        
        _curr = str(n)
        _prev = (n,)
        while True:
            _next = str(sum([int(_curr[i])**2 for i in range(len(_curr))]))
            if _next == "1": 
                return True
            if _next not in _prev:
                _curr = _next
                _prev += (_next,)
            else: 
                return False
        
s = Solution()

print(s.isHappy(19))
                            
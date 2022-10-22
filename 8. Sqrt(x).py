class Solution:
    def mySqrt(self, x: int) -> int: # Babylonian method (also known as Heron's method)
        prev_r = x / 2.0
        accuracy = 10**-6
        
        while True:
            r = (prev_r + x/prev_r)/2
            
            if abs(r - prev_r) < accuracy:
                return int(r)
            prev_r = r

print(Solution().mySqrt(2147395599))
# a = 2147395599
# x = math.e**(0.5 * math.log(a))
# print(int(round(x, 10)))

# for i in [int(x) for x in range(1,65)]:
#     print(f"sqrt({i}) = {Solution().mySqrt(i)}")
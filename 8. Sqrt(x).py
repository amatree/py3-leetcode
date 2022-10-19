import math
class Solution:
    def mySqrt(self, x: int) -> int:
        unit_digits = [x%10, 10-x%10]
        if 0 in unit_digits: unit_digits.remove(0)
        if 5 in unit_digits: unit_digits.remove(5)
        print(len(str(x)))
        
    # very slow when x gets bigger
    def sqrt(self, x: int) -> int:
        if x < 4 and x > 0:
            return 1

        r = 2
        inl = False
        while True:
            while r**2 > x:
                inl = True
                r = r - int(r/(r-1))
            if inl: break
            if r**2 < (r+1)**2:
                r = r + int(x/2)
            elif r**2 > x - 1 and r**2 < (r+1)**2:
                break

        return r

# print(Solution().mySqrt(2147395599))
print(int(round(math.e**(0.5 * math.log(2147395599)), 22)))
# for i in [int(x) for x in range(1,65)]:
#     print(f"sqrt({i}) = {Solution().mySqrt(i)}")
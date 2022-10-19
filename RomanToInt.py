class Solution(object):            
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_char_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        prev = 0
        curr = 0
        result = 0
        
        for char in s:
            if prev == 0:
                prev = roman_char_dict.get(char)
                continue
            else:
                curr = roman_char_dict.get(char)
                if (prev < curr):
                    result += curr - prev
                    prev = 0
                else:
                    result += prev
                    prev = curr
        
        return result + prev
                
test = Solution()

t1 = test.romanToInt("III")
t2 = test.romanToInt("LVIII")
t3 = test.romanToInt("MCMXCIV")

print(t1)
print(t2)
print(t3)
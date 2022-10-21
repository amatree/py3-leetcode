class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        length = len(s)
        while i < int(length / 2) + length%2:
            s[i], s[length - i - 1] = s[length - i - 1], s[i]
            i += 1
            
s = Solution()

string = ["h", "e", "l", "l", "o"]

print("Before:", string)

s.reverseString(string)

print("After:", string)
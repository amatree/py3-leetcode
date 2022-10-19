class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return [*str(int("".join(map(str, digits))) + 1)]
        

s = Solution()
print(s.plusOne([9,9]))
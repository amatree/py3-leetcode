class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen: 
                return True
            seen.add(i)
        return False
    
    
s = Solution()

arr = [1,2,3,4,5]
print(s.containsDuplicate(arr))
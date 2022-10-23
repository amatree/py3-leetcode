class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        pairs = []
        for i in nums:
            if i not in pairs:
                pairs.append(i)
            elif i in pairs:
                pairs.remove(i)
        return pairs[0] if len(pairs) > 0 else None


s = Solution()

arr = [1,1]

single_num = s.singleNumber(arr)
print(single_num)

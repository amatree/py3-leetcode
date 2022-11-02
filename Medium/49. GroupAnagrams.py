class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if len(strs) == 1: return [strs]

        sorted_strs = []
        for i in strs:
            sorted_strs.append("".join(sorted(i, key=str.lower)))
        
        result = []
        while len(sorted_strs) > 0:
            indices = [idx for idx, val in enumerate(sorted_strs) if sorted_strs[0] == val][::-1]
            tmp = []
            for idx in indices:
                tmp.append(strs[idx])
                sorted_strs.pop(idx)
                strs.pop(idx)
            result.append(tmp)
        return result


strs = ["eat","tea","tan","ate","nat","bat"]
sol = [["bat"],["nat","tan"],["ate","eat","tea"]]
sc = Solution()
s = sc.groupAnagrams(strs)

print(s)
print(s == sol)

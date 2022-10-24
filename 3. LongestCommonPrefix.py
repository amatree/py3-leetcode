class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        shortest_s = min(strs, key=len)
        count = 0
        prefix = ""
        
        while True:
            if (count < len(shortest_s)):
                prefix += strs[0][count]
            else:
                return prefix
            
            for s in shortest_s[1:]:
                if s[count] != prefix[count]:
                    return prefix[:-1]
            count += 1
            
    def longestCommonPrefix_fast(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        answer = ""

        for i in zip(*strs):
            if len(set(i)) == 1:
                answer += i[0]
            else:
                break
        return answer
            
t = Solution()
strs = ["flow", "flower", "fleet"]
print(t.longestCommonPrefix_fast(strs))

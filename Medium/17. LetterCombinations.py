class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if digits == "": return
        nokia = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        total_n = 1
        all_n = [4 if d in ["7","9"] else 3 for d in digits]
        for i in all_n:
            total_n *= i

        result = [""]*total_n
        # print(total_n)
        for pos in range(len(digits)):
            digit = digits[pos]
            length = 1
            for i in range(pos+1, len(all_n)):
                length *= all_n[i]
            
            start_i = 0
            r = int(total_n / (length * len(nokia[digit])))
            for k in range(r):
                for letter in nokia[digit]:
                    for i in range(length):
                        result[start_i] += letter
                        start_i += 1
                        if start_i >= total_n: start_i = 0
        
        return result
    
s = Solution()
# "72"
# ["pa","pb","pc","qa","qb","qc","ra","rb","rc","sa","sb","sc"]
a = s.letterCombinations("723")
# "723"
b = ["pad","pae","paf","pbd","pbe","pbf","pcd","pce","pcf","qad","qae","qaf","qbd","qbe","qbf","qcd","qce","qcf","rad","rae","raf","rbd","rbe","rbf","rcd","rce","rcf","sad","sae","saf","sbd","sbe","sbf","scd","sce","scf"]
print(a)
print(a==b)
print(["pad","pae","paf","pbd","pbe","pbf","pcd","pce","pcf","qad","qae","qaf","qbd","qbe","qbf","qcd","qce","qcf","rad","rae","raf","rbd","rbe","rbf","rcd","rce","rcf","sad","sae","saf","sbd","sbe","sbf","scd","sce","scf"])
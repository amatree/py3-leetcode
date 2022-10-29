class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        nokia = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mnl",
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
        for digit in digits:
            letters_count = len(nokia[digit])
            length = int(total_n / letters_count)
            start_i = 0
            if digit == digits[-1]:
                for letter in nokia[digit]:
                    start_i += 1
                    for i in range(length):
                        pos = (start_i-1) + (letters_count)* i
                        result[pos] += letter
                        # print(f"{i}<>{start_i} letter:", letter, f"x{length} (pos: {pos})")
                        # print(result)
                break
            else:
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
# ["pad","pae","paf","pbd","pbe","pbf","pcd","pce","pcf","qad","qae","qaf","qbd","qbe","qbf","qcd","qce","qcf","rad","rae","raf","rbd","rbe","rbf","rcd","rce","rcf","sad","sae","saf","sbd","sbe","sbf","scd","sce","scf"]
print(a)
print()
print(["pad","pae","paf","pbd","pbe","pbf","pcd","pce","pcf","qad","qae","qaf","qbd","qbe","qbf","qcd","qce","qcf","rad","rae","raf","rbd","rbe","rbf","rcd","rce","rcf","sad","sae","saf","sbd","sbe","sbf","scd","sce","scf"])
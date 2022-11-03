class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        if len(board) == 1 and len(board[0]) == 1:
            if board[0] != words: 
                return []
            return words
        result = []

        for word in words:
            skip = False
            letter_lists = []
            for letter in word:
                p = [idx for idx, word in enumerate(board) if letter in word]
                tmp = []
                for idx in p:
                    for i, l in enumerate(board[idx]):
                        if l == letter:
                            tmp.append(idx*4 + i)
                skip = len(tmp) == 0
                if skip: break
                letter_lists.append(tmp)
            if skip: continue
            
            if len(letter_lists) == 1:
                found = False
                for set in board:
                    if word in set:
                        found = True
                if found:
                    result.append(word)
                    continue
            tmp = []
            while True:
                if len(letter_lists[0]) == 0: break
                i_check = [letter_lists[0].pop(0)]
                count = 1
                while count < len(word):
                    backup = letter_lists[count].copy()
                    if len(letter_lists[count]) == 0:
                        letter_lists[count] = backup
                        break
                    next_i = letter_lists[count].pop(0)
                    if next_i in [i_check[count-1]-1, i_check[count-1]+1, i_check[count-1]+4, i_check[count-1]-4]:
                        if i_check.count(next_i) + 1 > 1:
                            break
                        i_check.append(next_i)
                        count += 1
                    elif len(letter_lists[count]) == 0:
                        letter_lists[count] = backup + [next_i]
                        break
                        
                
                if count == len(word):
                    result.append(word)
                    break
                
        return result


board = [["o","a","a","n"],
         ["e","t","a","e"],
         ["i","h","k","r"],
         ["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
sol = ["eat","oath"]

board = [["a","b","c","e"],
         ["x","x","c","d"],
         ["x","x","b","a"]]

words = ["abc","abcd"]
sol = ["abc","abcd"]

sc = Solution()
s = sc.findWords(board, words)
print("---"*10)
print(s)
print(s == sol)

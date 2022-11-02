class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        result = []

        for word in words:
            pos = []
            all_p = []
            for letter in word:
                p = [idx for idx, word in enumerate(board) if letter in word]
                for i in range(len(board[p])):

            for p in all_p:
                print(*p)

            break
                
        return result


board = [["o","a","a","n"],
         ["e","t","a","e"],
         ["i","h","k","r"],
         ["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
sol = ["eat","oath"]
sc = Solution()
s = sc.findWords(board, words)

print(s)
print(s == sol)

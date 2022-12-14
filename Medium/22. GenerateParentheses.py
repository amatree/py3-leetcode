class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        result = []
        
        def backtrack(open, closed):
            if open == closed == n:
                result.append("".join(stack))
                return
            if open < n:
                stack.append("(")
                backtrack(open + 1, closed)
                stack.pop()
            if closed < open:
                stack.append(")")
                backtrack(open, closed + 1)
                stack.pop()
        
        backtrack(0,0)
        return result
# n=2:
# me: ["(())","()()"]

# n=3:
# me: ["((()))","(()())","(())()","()(())","()()()"]

# n=4:
# me: ["(((())))","(((())))","((()()))","((())())","(()(()))","(()()())","(()(()))"]
# lc: ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]

# n=5:
# lc: ["((((()))))","(((()())))","(((())()))","(((()))())","(((())))()","((()(())))","((()()()))","((()())())","((()()))()","((())(()))","((())()())","((())())()",
#       "((()))(())","((()))()()","(()((())))","(()(()()))","(()(())())","(()(()))()","(()()(()))","(()()()())","(()()())()","(()())(())","(()())()()","(())((()))",
#       "(())(()())","(())(())()","(())()(())","(())()()()","()(((())))","()((()()))","()((())())","()((()))()","()(()(()))","()(()()())","()(()())()","()(())(())",
#       "()(())()()","()()((()))","()()(()())","()()(())()","()()()(())","()()()()()"]


sols = [["()"],
        ["(())", "()()"],
        ["((()))", "(()())", "(())()", "()(())", "()()()"],
        ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()",
         "(())(())", "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"],
        ["((((()))))", "(((()())))", "(((())()))", "(((()))())", "(((())))()", "((()(())))", "((()()()))", "((()())())", "((()()))()", "((())(()))", "((())()())", "((())())()", "((()))(())", "((()))()()", "(()((())))", "(()(()()))", "(()(())())", "(()(()))()", "(()()(()))", "(()()()())", "(()()())()",
         "(()())(())", "(()())()()", "(())((()))", "(())(()())", "(())(())()", "(())()(())", "(())()()()", "()(((())))", "()((()()))", "()((())())", "()((()))()", "()(()(()))", "()(()()())", "()(()())()", "()(())(())", "()(())()()", "()()((()))", "()()(()())", "()()(())()", "()()()(())", "()()()()()"],
        ]

s = Solution()
num = 4
p = s.generateParenthesis(num)

print(p)

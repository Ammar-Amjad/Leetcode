class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = set(['+', '-', '/', '*'])
        stack = []
        for i in range(len(tokens)):
            token = tokens[i]
            if token not in ops:
                stack.append(int(token))
            else:
                B = stack.pop()
                A = stack.pop()
                if token == '+':
                    C = A + B
                elif token == '-':
                    C = A - B
                elif token == '/':
                    C = int(A / B)
                elif token == '*':
                    C = A * B
                stack.append(C)
        return stack.pop()
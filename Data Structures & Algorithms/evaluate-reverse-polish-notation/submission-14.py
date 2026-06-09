class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] == "+":
                r = stack.pop()
                s = stack.pop()
                stack.append(s+r)
            elif tokens[i] == "-":
                r = stack.pop()
                s = stack.pop()
                stack.append(s-r)
            elif tokens[i] == "*":
                r = stack.pop()
                s = stack.pop()
                stack.append(s*r)
            elif tokens[i] == "/":
                r = stack.pop()
                s = stack.pop()
                stack.append(int(s/r))
            else:
                stack.append(int(tokens[i]))
            
        return stack[-1]
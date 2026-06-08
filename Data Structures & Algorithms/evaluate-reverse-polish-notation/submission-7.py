class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] == "+" or tokens[i] == "-" or tokens[i] == "*" or tokens[i] == "/":
                if tokens[i] == "+":
                    r = stack.pop()
                    s = stack.pop()
                    stack.append(s+r)
                elif tokens[i] == "-":
                    r = stack.pop()
                    s = stack.pop()
                    stack.append(s-r)
                if tokens[i] == "*":
                    r = stack.pop()
                    s = stack.pop()
                    stack.append(s*r)
                if tokens[i] == "/":
                    r = stack.pop()
                    s = stack.pop()
                    if s/r <= 0 and s/r > 1:
                        stack.append(0)
                    else:    
                        stack.append(s//r)
            else:
                stack.append(int(tokens[i]))
        
        return stack[-1]


        
class Solution:
    def asteroidCollision(self, ast: List[int]) -> List[int]:
        stack = []

        for i in range(len(ast)):
            if ast[i] > 0:
                stack.append(ast[i])
            else:
                if not stack:
                    stack.append(ast[i])
                elif stack and stack[-1] < 0:
                    stack.append(ast[i])
                elif stack and stack[-1] > 0 and abs(stack[-1]) == abs(ast[i]):
                    stack.pop()
                else:
                    if stack and abs(stack[-1]) > abs(ast[i]):
                        continue
                    else:
                        while stack and abs(stack[-1]) < abs(ast[i]):
                            stack.pop()
                        stack.append(ast[i])
                    
        return stack

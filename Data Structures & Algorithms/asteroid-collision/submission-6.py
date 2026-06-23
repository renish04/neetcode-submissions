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
                else:
                    while stack and stack[-1] > 0:
                        if abs(stack[-1]) == abs(ast[i]):
                            stack.pop()
                            break
                        elif ast[i]*stack[-1] < 0 and abs(stack[-1]) < abs(ast[i]):
                            stack.pop()
                        elif abs(stack[-1]) > abs(ast[i]):
                            break
                        elif not stack or stack[-1] < 0:
                            stack.append(ast[i])
        return stack

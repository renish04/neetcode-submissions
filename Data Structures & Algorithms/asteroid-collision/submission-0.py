class Solution:
    def asteroidCollision(self, ast: List[int]) -> List[int]:
        stack = []

        for i in range(len(ast)):
            if stack == []:
                stack.append(ast[i])
            elif stack[-1]*ast[i] < 0:
                if abs(ast[i]) > abs(stack[-1]):
                    stack.pop()
                    stack.append(ast[i])
                elif abs(ast[i]) == abs(stack[-1]):
                    stack.pop()
                else:
                    continue
            else:
                stack.append(ast[i])
        
        return stack
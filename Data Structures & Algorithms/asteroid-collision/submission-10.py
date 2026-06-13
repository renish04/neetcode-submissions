class Solution:
    def asteroidCollision(self, ast: List[int]) -> List[int]:
        stack = []
        
        for i in range(len(ast)):
            if ast[i] > 0:
                stack.append(ast[i])
            else:
                if not stack or stack[-1] < 0:
                    stack.append(ast[i])
                elif abs(ast[i]) == abs(stack[-1]):
                    stack.pop()
                elif abs(ast[i]) < abs(stack[-1]):
                    continue
                else:
                    alive = True
                    while stack and ast[i]*stack[-1] < 0:
                        if abs(ast[i]) == abs(stack[-1]):
                            stack.pop()
                            alive = False
                            break
                        elif abs(ast[i]) < abs(stack[-1]):
                            alive = False
                            break
                        else:
                            stack.pop()
                    if alive == True:
                        stack.append(ast[i])
        
        return stack

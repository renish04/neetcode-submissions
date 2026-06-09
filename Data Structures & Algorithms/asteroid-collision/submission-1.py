class Solution:
    def asteroidCollision(self, ast: List[int]) -> List[int]:
        stack = [ast[0]]

        for i in range(1, len(ast)):
            if ast[i] > 0:
                stack.append(ast[i])
            else:
                if stack[-1] < 0:
                    stack.append(ast[i])

                elif abs(ast[i]) == abs(stack[-1]):
                    stack.pop()
                
                else:
                    while ast[i]*stack[-1] < 0 and abs(ast[i]) > abs(stack[-1]):
                        stack.pop()
                    if stack == [] or stack[-1] < 0:
                        stack.append(ast[i])
                    elif abs(stack[-1]) == abs(ast[i]):
                        stack.pop()
                    else:
                        continue

        return stack
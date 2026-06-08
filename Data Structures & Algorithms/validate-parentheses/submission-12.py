class Solution:
    def isValid(self, s: str) -> bool:
        mapp = {"]":"[", "}":"{", ")":"("}
        stack = []

        for i in range(len(s)):
            if s[i] not in mapp:
                stack.append(s[i])
            else:
                if len(stack) != 0 and stack[-1] != mapp[s[i]]:
                    return False
                elif len(stack) != 0 and stack[-1] == mapp[s[i]]:
                    stack.pop()
                else:
                    return False
            
        if len(stack) == 0:
            return True
        else:
            return False
                


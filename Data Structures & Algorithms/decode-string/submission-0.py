class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0

        while i < len(s):
            if s[i] == "]":
                x = ""
                while stack[-1] != "[":
                    w = stack.pop()
                    x = w + x
                stack.pop()
                factor = stack.pop()
                stack.append(int(factor)*x)
                i += 1
            else:
                stack.append(s[i])
                i += 1

        out = ""
        for m in stack:
            out += m
        
        return out

        

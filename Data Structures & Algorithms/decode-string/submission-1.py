class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        nums = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        while i < len(s):
            if s[i] == "]":
                x = ""
                while stack[-1] != "[":
                    w = stack.pop()
                    x = w + x
                stack.pop()
                factor = ""
                while stack and stack[-1] in nums:
                    f = stack.pop()
                    factor = f + factor
                stack.append(int(factor)*x)
                i += 1
            else:
                stack.append(s[i])
                i += 1

        out = ""
        for m in stack:
            out += m
        
        return out

        

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] == "{" or s[i] == "[" or s[i] == "(":
                stack.append(s[i])
            elif s[i] == "}":
                if stack != [] and stack[-1] == "{":
                    stack.pop(-1)
                else:
                    return False
            elif s[i] == "]":
                if stack != [] and stack[-1] == "[":
                    stack.pop(-1)
                else:
                    return False           
            elif s[i] == ")":
                if stack != [] and stack[-1] == "(":
                    stack.pop(-1)
                else:
                    return False        
        if stack == []:
            return True
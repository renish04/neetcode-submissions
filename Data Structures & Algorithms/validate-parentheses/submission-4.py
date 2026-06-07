class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] == "{" or s[i] =="(" or s[i] == "[":
                stack.append(s[i])
            elif s[i] == "}" and stack[-1] == "{":
                stack.pop(-1)
            elif s[i] == ")" and stack[-1] == "(":
                stack.pop(-1)
            elif s[i] == "]" and stack[-1] == "[":
                stack.pop(-1)
            else:
                return False
            print(stack)
        return True
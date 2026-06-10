class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0

        while i < len(path):
            if path[i] == "/":
                if stack and stack[-1] == "/":
                    i += 1
                else:
                    stack.append(path[i])
            
            elif path[i] == ".":
                if i == len(path)-1 or path[i+1] == "/":
                    i += 1

                elif path[i+1] == ".":
                    if i+1 == len(path)-1 or path[i+2] == "/":
                        slash = stack.pop()
                        if stack:
                            stack.pop()
                            stack.pop()
                        stack.append(slash)
                        i += 1
                    else:
                        s = ""
                        while i < len(path) and path[i] != "/":
                            s += path[i]
                            i += 1
                        stack.append(s)

            else:
                s = ""
                while i < len(path) and path[i] != "/":
                    s += path[i]
                    i += 1
                stack.append(s)

        
        if len(stack)>1 and stack[-1] == "/":
            stack.pop()

        final = []
        for m in range(len(stack)):
            w = stack.pop()
            final.append(w)
        
        strfinal = ""
        for x in range(len(final)):
            r = final.pop()
            strfinal += r
        
        return strfinal



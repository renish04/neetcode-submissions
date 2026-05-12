class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mini = 0
        x = strs[0]

        for i in range(1, len(strs)):
            if len(x) <= len(strs[i]):
                y = len(x)

            if len(strs[i]) < len(x):
                y = len(strs[i])

            for j in range(y):
                m = strs[i]
                if m[0] != x[0]:
                    print(m[0])
                    print(x[0])
                    return ""
                if m[j] != x[j]:
                    if mini == 0:
                        mini = j
                    elif j < mini:
                        mini = j

        return x[0:mini] 
        
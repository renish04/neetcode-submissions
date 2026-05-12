class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mini = 0
        min_y = len(strs[0])   # <-- add this
        x = strs[0]
        for i in range(1, len(strs)):
            if len(x) <= len(strs[i]):
                y = len(x)
            if len(strs[i]) < len(x):
                y = len(strs[i])
            min_y = min(min_y, y)   # <-- add this
            for j in range(y):
                m = strs[i]
                if m[0] != x[0]:
                    return ""
                if m[j] != x[j]:
                    if mini == 0:
                        mini = j
                    elif j < mini:
                        mini = j
        if mini == 0:
            return x[:min_y]   # <-- was x[0], now use min_y
        return x[0:mini]
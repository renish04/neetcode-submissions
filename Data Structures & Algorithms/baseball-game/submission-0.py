class Solution:
    def calPoints(self, ops: List[str]) -> int:
        new = []
        tot = 0
        for i in range(len(ops)):
            if ops[i] == "+":
                x = new[len(new)-1] + new[len(new)-2]
                new.append(x)
            elif ops[i] == "D":
                y = 2*new[len(new)-1]
                new.append(y)
            elif ops[i] == "C":
                new.pop(len(new)-1)
            else:
                new.append(int(ops[i]))
            
        for i in range(len(new)):
            tot += new[i]
        
        return tot


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        for i in range(len(ops)):
            if ops[i] == "+":
                ops.append(ops[-1] + ops[-2])
            elif ops[i] == "C":
                ops.pop()
            elif ops[i] == "D":
                ops.append(2*ops[-1])
            else:
                ops.append(int(ops[i]))
            
        tot = 0
        for i in range(len(ops)):
            tot += ops[i]
        
        return tot
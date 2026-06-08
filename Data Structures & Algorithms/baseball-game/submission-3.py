class Solution:
    def calPoints(self, ops: List[str]) -> int:
        cal = []
        for i in range(len(ops)):
            if ops[i] == "+":
                cal.append(cal[-1] + cal[-2])
            elif ops[i] == "C":
                cal.pop()
            elif ops[i] == "D":
                cal.append(2*cal[-1])
            else:
                cal.append(int(ops[i]))
            
        tot = 0
        for i in range(len(cal)):
            tot += cal[i]
        
        return tot
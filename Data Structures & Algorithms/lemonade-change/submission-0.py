class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_hash = {5:0, 10:0, 20:0}
        check = True

        for i in range(len(bills)):
            if bills[i] == 5:
                bill_hash[5] += 1

            elif bills[i] == 10:
                if bill_hash[5] == 0:
                    check = False
                else:
                    bill_hash[5] -= 1
                    bill_hash[10] += 1
            
            elif bills[i] == 20:
                if bill_hash[10] != 0 and bill_hash[5] != 0:
                    bill_hash[10] -=1
                    bill_hash[5] -= 1
                    bill_hash[20] += 1

                elif bill_hash[5] >= 3:
                    bill_hash[5] -= 3
                    bill_hash[20] += 1

                else:
                    check = False
                
        return check


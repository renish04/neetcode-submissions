class Solution:
    def findDuplicate(self, arr: List[int]) -> int:
        slow = 0
        fast = 0
        slow = arr[slow]
        fast = arr[arr[fast]]
        
        while slow != fast :
            slow = arr[slow]
            fast = arr[arr[fast]]
        
        slow2 = 0

        while slow != slow2:
            slow = arr[slow]
            slow2 = arr[slow2]
        
        return slow


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element = None
        count = 0

        for i in range(len(nums)):
            if element == None:
                element = nums[i]
                count = 1
            else:
                if nums[i] == element:
                    count += 1
                else:
                    count -= 1
                    if count == 0:
                        element = None
                
        
        return element
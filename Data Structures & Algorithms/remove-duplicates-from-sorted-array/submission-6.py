class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = i+1
        swap = 0

        while i < len(nums)-1:
            if nums[i] == nums[j]:
                j += 1

            else:
                nums[i+1], nums[j] = nums[j], nums[i+1]
                swap += 1
                i += 1
                j += 1 
            
        return swap

        
                    
        
        


        

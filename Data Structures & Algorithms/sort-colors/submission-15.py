class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left = 0
        right = len(nums) - 1
        i = 0
        
        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                # WHY i += 1? 
                # Because the number we just swapped from 'left' into 'i' 
                # has already been examined by 'i' in the past. It is GUARANTEED 
                # to be a 1 (or a 0 if i == left). We don't need to re-examine it.
                i += 1
                
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
                # WHY NO i += 1?
                # Because the number we just swapped from the far 'right' is completely
                # unknown. It could be a 0, 1, or 2. Our scout 'i' must stay exactly
                # where it is to examine this new number on the next loop iteration.
                
            else: # nums[i] == 1
                i += 1
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        element1 = nums[0]
        count1 = 0
        element2 = 0
        count2 = 0

        for i in range(len(nums)):
            if nums[i] == element1:
                count1 += 1
            elif count2 == 0:
                element2 = nums[i]
                count2 += 1
            elif nums[i] == element2:
                count2 += 1
            else:
                count1 -=1
                count2 -= 1
                if count1 == 0:
                    element1 = nums[i]
                    count1 +=1
                elif count2 == 0:
                    element2 = nums[i]
                    count2 += 1 
        element_1_count = 0
        element_2_count = 0

        for i in range(len(nums)):
            if nums[i] == element1:
                element_1_count += 1
            if nums[i] == element2:
                element_2_count +=1
        
        if element_1_count > (len(nums)/3) and element_2_count > (len(nums)/3):
            return [element1, element2]
        elif element_1_count > (len(nums)/3):
            return [element1]
        elif element_2_count > (len(nums)/3):
            return [element2]
        else:
            return []

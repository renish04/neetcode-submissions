class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        sortArray = self.sortArray
        merge = self.merge
        n = len(nums)

        if n <=1 :
            return nums
        
        mid = n // 2
        left = sortArray(nums[:mid])
        right = sortArray(nums[mid:])

        return merge(left, right)

    def merge(self, left, right):
        # self.left = left
        # self.right = right
        i = 0
        j = 0
        
        final = []

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                final.append(left[i])
                i += 1
            else:
                final.append(right[j])
                j += 1

        final.extend(left[i:])
        final.extend(right[j:]) 

        return final     
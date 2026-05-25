class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = n-1
        if m != 0:
            i = m-1
        else:
            i = 0
        k = m+n-1

        while j >= 0:
            if nums1[i] > nums2[j]:
                nums1[i], nums1[k] = nums1[k], nums1[i]
                if k != 0:
                    k -=1
                if i != 0:
                    i -=1

            elif nums1[i] <= nums2[j] or i == 0:
                nums1[k] = nums2[j]
                j -= 1
                if k != 0:
                    k -=1
    

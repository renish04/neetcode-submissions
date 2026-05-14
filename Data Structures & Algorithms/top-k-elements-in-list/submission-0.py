class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        final = []
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] += 1
        
        for i in range(k):
            x = max(hashmap, key=hashmap.get)
            final.append(x)
            hashmap.pop(x)
             
        return final
        


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1

        arr = []

        for freq in hashmap:
            if hashmap[freq] >= k:
                arr.append(freq)
            
        return arr
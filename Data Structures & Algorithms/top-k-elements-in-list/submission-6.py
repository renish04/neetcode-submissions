class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashi = {}
        final = []
        for i in range(len(nums)):
            if nums[i] not in hashi:
                hashi[nums[i]] = 1
            else:
                hashi[nums[i]] += 1

        pos_list = []
        for i in range(len(nums)+1):
            pos_list.append([])

        for i in hashi:
            x = hashi[i]
            pos_list[x].append(i)

        for i in range(len(pos_list)-1, -1, -1):
            if pos_list[i] == []:
                continue

            else:
                for j in range(len(pos_list[i])):
                    if len(final) < k:
                        final.append(pos_list[i][j])
        return final
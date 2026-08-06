class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp=defaultdict(int)
        for x in nums:
            mp[x]+=1
        mp=list(sorted(mp.items(), key=lambda x:x[1],reverse=True))
        output=[i[0] for i in mp[:k]]
        return output
        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp=defaultdict(list)
        for w in strs:
            ws="".join(sorted(w))
            mp[ws].append(w)
        return list(mp.values())
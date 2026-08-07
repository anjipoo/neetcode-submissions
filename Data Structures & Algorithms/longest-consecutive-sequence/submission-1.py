class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        ans=1
        curr=1
        n=len(nums)
        for i in range(1,n):
            if nums[i]==nums[i-1]:
                continue
            elif nums[i]==nums[i-1]+1:
                curr+=1
            else:
                curr=1
            ans=max(ans,curr)
        return ans

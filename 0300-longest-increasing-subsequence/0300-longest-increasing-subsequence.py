class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[i]>nums[j]:
                    dp[i]+=1
                    dp[j]=max(dp[i],dp[j])
                return max(dp)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total_subarray = 0
        for i in range(len(nums)):
            sum=0
            for j in range(i, len(nums)):
                sum+=nums[j]
                if sum==k:
                    total_subarray+=1
        return total_subarray
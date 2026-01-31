class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_N = (n*(n+1))//2
        sumN = sum(nums)
        return sum_N - sumN

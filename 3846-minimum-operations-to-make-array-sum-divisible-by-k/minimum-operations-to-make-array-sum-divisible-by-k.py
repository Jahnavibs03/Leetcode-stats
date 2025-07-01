class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sum = 0
        res = 0
        for x in nums:
            sum += x
        if sum < k:
            return sum
        else:
            res = sum % k
            return res
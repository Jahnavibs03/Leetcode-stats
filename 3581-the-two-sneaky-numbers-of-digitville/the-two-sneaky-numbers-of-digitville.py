class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        cnt = {}
        res = []
        for x in nums:
            if x not in cnt:
                cnt[x] = 1
            else:
                cnt[x] = cnt[x] + 1
                if cnt[x] == 2:
                    res.append(x)
                    if len(res) == 2:
                        return res
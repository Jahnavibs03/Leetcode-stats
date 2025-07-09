class Solution:
    def findLucky(self, arr: List[int]) -> int:
        luc = 0
        mxl = -1
        cnt = {}
        for x in arr:
            if x in cnt:
                cnt[x] = cnt[x] + 1
            else:
                cnt[x] = 1
        for x in cnt:
            if x == cnt[x]:
                if x > mxl:
                    mxl = x
        print(mxl)
        return mxl
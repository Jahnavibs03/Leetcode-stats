class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        r = ""
        for i in range(len(s)):
            if i % k == 0 and i > 0:
                res.append(r)
                r = ""
            r = r + s[i]
        if len(r) == k:
            res.append(r)
        else:
            for i in range(k-len(r)):
                r = r + fill
            res.append(r)
        #print(res)
        #print(r)
        return res

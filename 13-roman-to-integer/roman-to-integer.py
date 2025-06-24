class Solution:
    def romanToInt(self, s: str) -> int:
        val = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        num = 0
        if len(s) == 1:
            return val[s[0]]
        for i in range(len(s)):
            if i == 0 and val[s[i]] < val[s[i+1]]:
                continue
            if i < len(s)-1 and val[s[i]] < val[s[i+1]]:
                continue
            if i > 0 and val[s[i]] > val[s[i-1]]:
                r = val[s[i]] - val[s[i-1]]
                num += r
            else:
                num += val[s[i]]
            #print(num)
        return num
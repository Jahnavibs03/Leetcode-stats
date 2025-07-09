class Solution:
    def kthCharacter(self, k: int) -> str:
        s = "a"
        while len(s) < k:
            p = ""
            for x in s:
                n = ord(x)
                #print(n)
                m = n + 1
                if m > 122:
                    m = ((n + 1) % 123) + 97
                #print(m)
                p = p + chr(m)
            s = s + p
            #print(s)
        return s[k-1]
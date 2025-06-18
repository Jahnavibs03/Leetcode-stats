class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        j = 0
        p = []
        for j in range(len(nums)):
            #print(j)
            p.append(nums[j])
            if (j+1) % 3 == 0:
                res.append(p) 
                p = []
            
        print(res)
        for x in res:
            r = []
            r.append(x[0])
            r.append(x[1])
            r.append(x[2])
            d1 = r[1] - r[0]
            d2 = r[2] - r[1]
            d3 = r[2] - r[0]
            if d1 <= k and d2 <= k and d3 <= k:
                continue
            else:
                return []
        return res
            


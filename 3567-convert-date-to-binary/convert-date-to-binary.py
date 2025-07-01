class Solution:
    def convertDateToBinary(self, date: str) -> str:
        arr = date.split("-")
        res = format(int(arr[0]),'b') + "-" + format(int(arr[1]),'b') + "-" + format(int(arr[2]),'b')
        print(res)
        return res

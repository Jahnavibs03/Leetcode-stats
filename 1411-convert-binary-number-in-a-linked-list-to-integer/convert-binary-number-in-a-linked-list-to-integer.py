# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        s = ""
        node = ListNode()
        node = head
        while node != None:
            s += str(node.val)
            node = node.next
        #print(s)
        num = int(s,2)
        #print(num)
        return num


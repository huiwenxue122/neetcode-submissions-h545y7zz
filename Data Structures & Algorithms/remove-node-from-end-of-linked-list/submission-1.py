# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        fast = dummy
        slow = dummy

        # fast先走n+1步
        for _ in range(n + 1):
            fast = fast.next

         # 一起走
        while fast:
            fast = fast.next
            slow = slow.next
            
        # 删除节点
        slow.next = slow.next.next

        return dummy.next




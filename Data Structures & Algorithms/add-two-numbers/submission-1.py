# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 先建结果链表的头
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0 #取当前两个链表的值，如果某个链表走完了，就当作 0
            v2 = l2.val if l2 else 0
            # 做加法：
            total = v1 + v2 + carry
            carry = total // 10
            digit = total % 10
            # 新建节点：
            cur.next = ListNode(digit)
            cur = cur.next
            # 链表往后走：
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next

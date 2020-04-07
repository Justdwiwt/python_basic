class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        flag = 0
        res = ListNode(0)
        tmp = res
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            value = x + y + flag
            flag = value // 10
            tmp.next = ListNode(value % 10)
            tmp = tmp.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if flag != 0:
            tmp.next = ListNode(1)
        return res.next

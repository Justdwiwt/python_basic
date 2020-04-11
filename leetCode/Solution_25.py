class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def reverseKGroup(head: ListNode, k: int) -> ListNode:
        pHead = ListNode(-1)
        pHead.next = head
        p = pHead
        p_list = [None for _ in range(k)]
        while True:
            pNode = p
            for i in range(k):
                if p is None:
                    break
                p = p.next
                p_list[i] = p
            if p is None:
                break
            pNode.next = p_list[k - 1]
            p_list[0].next = p_list[k - 1].next
            for i in range(k - 1, 0, -1):
                p_list[i].next = p_list[i - 1]
            p = p_list[0]
        return pHead.next

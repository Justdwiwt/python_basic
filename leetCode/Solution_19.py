class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        global i
        if head is None:
            i = 0
            return None
        head.next = self.removeNthFromEnd(head.next, n)
        i += 1
        return head.next if i == n else head

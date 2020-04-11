import heapq
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def mergeKLists(lists: List[ListNode]) -> ListNode:
        que, curs = [], []
        for index, node in enumerate(lists):
            if node is not None:
                heapq.heappush(que, (node.val, index))
            curs.append(node)
        node = ListNode(-1)
        cur = node
        while que:
            val, index = heapq.heappop(que)
            cur.next = lists[index]
            cur = cur.next
            lists[index] = lists[index].next
            if lists[index] is not None:
                heapq.heappush(que, (lists[index].val, index))
        return node.next

from typing import Optional
from datatypes.linked_list import ListNode

class Solution:
    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next

        return False

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.hasCycle(None) is False)
    print(solution.hasCycle(ListNode(1)) is False)
    print(solution.hasCycle(ListNode(1, ListNode(2))) is False)
    print(solution.hasCycle(ListNode(1, ListNode(2, ListNode(3)))) is False)

    node = ListNode(1)
    node.next = node
    print(solution.hasCycle(node) is True)

    node = ListNode(1, ListNode(2))
    node.next.next = node
    print(solution.hasCycle(node) is True)

    node = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node.next = node2
    node2.next = node3
    node3.next = node2
    print(solution.hasCycle(node) is True)

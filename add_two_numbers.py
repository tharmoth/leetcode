from typing import Optional
from datatypes.linked_list import ListNode

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head
        carry = 0
        while l1 or l2 or carry:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry = int(val / 10)

            current.next = ListNode(val % 10)
            current = current.next

        return head.next


if __name__ == "__main__":
    solution = Solution()
    print(solution.addTwoNumbers(None, None) is None)
    print(solution.addTwoNumbers(ListNode(1), None) == ListNode(1))
    print(solution.addTwoNumbers(None, ListNode(1)) == ListNode(1))
    print(solution.addTwoNumbers(ListNode(1), ListNode(1)) == ListNode(2))
    print(solution.addTwoNumbers(ListNode(1, ListNode(2)), ListNode(1)) == ListNode(2, ListNode(2)))
    print(solution.addTwoNumbers(ListNode(1), ListNode(1, ListNode(2))) == ListNode(2, ListNode(2)))
    print(solution.addTwoNumbers(ListNode(1, ListNode(2)), ListNode(1, ListNode(2))) == ListNode(2, ListNode(4)))
    print(solution.addTwoNumbers(ListNode(1, ListNode(2)), ListNode(9, ListNode(2))) == ListNode(0, ListNode(5)))

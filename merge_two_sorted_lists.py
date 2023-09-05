from typing import Optional
from datatypes.linked_list import ListNode
from datatypes.linked_list import list_to_linkedlist
from datatypes.linked_list import linkedlist_to_list


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        top_node = None
        current_node = None
        while True:
            if (list1 is not None and list2 is not None and list1.val <= list2.val) or (list1 is not None and list2 is None):
                next_node = list1
                list1 = list1.next
            elif (list1 is not None and list2 is not None) or (list1 is None and list2 is not None):
                next_node = list2
                list2 = list2.next
            else:
                break

            if current_node is not None:
                current_node.next = next_node
            else:
                top_node = next_node

            current_node = next_node

        return top_node


if __name__ == '__main__':
    solution = Solution()
    print(linkedlist_to_list(solution.mergeTwoLists(list_to_linkedlist([1, 2, 4]), list_to_linkedlist([1, 3, 4]))))
    print(linkedlist_to_list(solution.mergeTwoLists(list_to_linkedlist([1, 2, 4]), list_to_linkedlist([1, 3, 4]))) == [1, 1, 2, 3, 4, 4])
    print(linkedlist_to_list(solution.mergeTwoLists(list_to_linkedlist([]), list_to_linkedlist([]))) == [])
    print(linkedlist_to_list(solution.mergeTwoLists(list_to_linkedlist([]), list_to_linkedlist([0]))) == [0])
    print(linkedlist_to_list(solution.mergeTwoLists(list_to_linkedlist([0]), list_to_linkedlist([]))) == [0])
    print(linkedlist_to_list(solution.mergeTwoLists(list_to_linkedlist([1, 2, 3]), list_to_linkedlist([]))) == [1, 2, 3])
    print(linkedlist_to_list(solution.mergeTwoLists(list_to_linkedlist([]), list_to_linkedlist([1, 2, 3]))) == [1, 2, 3])
    print(linkedlist_to_list(solution.mergeTwoLists(list_to_linkedlist([1, 2, 3]), list_to_linkedlist([1, 2, 3]))) == [1,1,2,2,3,3])
    print(linkedlist_to_list(solution.mergeTwoLists(list_to_linkedlist([1, 2, 3]), list_to_linkedlist([4, 5, 6]))) == [1,2,3,4,5,6])

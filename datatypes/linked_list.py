class ListNode:
    """
    Definition for singly-linked list.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + ", " + (str(self.next) if self.next is not None else "")

    def __eq__(self, other):
        return isinstance(other, ListNode) and self.val == other.val and self.next == other.next


def list_to_linkedlist(lst):
    """
    Convert a list to a linked list.
    """
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def linkedlist_to_list(head):
    """
    Convert a linked list to a list.
    """
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

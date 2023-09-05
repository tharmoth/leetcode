### Description

>Given `head`, the head of a linked list, determine if the linked list has a cycle in it.
>
>There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.
>
> Return `true` _if there is a cycle in the linked list_. Otherwise, return `false`.

---
## Hashtable

### Method
The first that occurred to me was to traverse the list and store seen nodes in a hash table. As we traverse the list we check each node to see if it is in the hash table and if it is than we have found a loop.
### Complexity
Time Complexity - O(n) We only traverse the list once
Space Complexity - O(n) We store each value in the table
### Code
```py
def hasCycle(self, head: Optional[ListNode]) -> bool:  
    seen = set()  
    while head:  
        if head in seen:  
            return True  
        seen.add(head)  
        head = head.next  
  
    return False
```

---

## Floyd's Algorithm
### Method
We use two pointers, a _slow_ pointer, and a _fast_ pointer where the slow pointer chases the fast pointer though the list and if they meet than there is a cycle and if the fast pointer reaches the end there is not
### Complexity
Time Complexity - O(n) for the worst case we only traverse the list once
Space Complexity - O(1) We only store the two pointers
### Code
```py
def hasCycle(self, head: Optional[ListNode]) -> bool:  
    fast = head  
    slow = head  
    while fast and fast.next:  
        slow = slow.next  
        fast = fast.next.next  
        if slow == fast:  
            return True  
  
    return False
```

---
### Links

[Leetcode](https://leetcode.com/problems/linked-list-cycle)
## Tags:

#linked-list #hash-table #floyds-algorithm
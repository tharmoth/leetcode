## Description 

>You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
>
>You may assume the two numbers do not contain any leading zero, except the number 0 itself.

---
## Iteration

### Method

In order to solve this problem we can iterate though the two linked lists with a carry bit. We must take in to account that one of the lists may be longer than the other list and that there may be a carry bit left over at the end.

I took special consideration to minimize the if statements by having the head be initialized to a blank node and then retuning it's next in order to not deal with border values in the while loop.

### Complexity
Time complexity - O(n) We have to iterate through both lists once
Space Complexity - O(n) We generate a list the size of the longest list

## Code
```py
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
```

### Links

[Leetcode](https://leetcode.com/problems/add-two-numbers)
## Tags: 

#linked-list 
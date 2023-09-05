### Description

> Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (`push`, `peek`, `pop`, and `empty`).
>
>Implement the `MyQueue` class:
>
>- `void push(int x)` Pushes element x to the back of the queue.
>- `int pop()` Removes the element from the front of the queue and returns it.
>- `int peek()` Returns the element at the front of the queue.
>- `boolean empty()` Returns `true` if the queue is empty, `false` otherwise.
---
## Two Stacks
### Method
I initially didn't understand the question and implemented this with only one stack, which is substantially easier, and for Leetcode's test cases faster. But After examining other solutions I understood this is asking for a specific implementation not actually required by their checker. This COULD be useful in some sort of threading or perhaps with a very specific data flow.

In any case. I implemented this using two stacks one input stack and one output stack. The output stack is update when it is empty in the peek method.

### Complexity

Time Complexity - O(1) Each call of the functions should average out to O(1) though it could be longer when switching stacks

Space Complexity - O(n) we store all of the input values
### Code
```py
class MyQueue:  
    def __init__(self):  
        self.input = []  
        self.output = []  
  
    def push(self, x: int) -> None:  
        self.input.append(x)  
  
    def pop(self) -> int:  
        self.peek()  
        return self.output.pop(0)  
  
    def peek(self) -> int:  
        if len(self.output) == 0:  
            while self.input:  
                self.output.append(self.input.pop(0))  
        return self.output[0]  
  
    def empty(self) -> bool:  
        return len(self.input) == 0 and len(self.output) == 0
```
### Problems in my solution
Slight python improvements could be made since empty lists are False

---
### Links:

[Leetcode](https://leetcode.com/problems/implement-queue-using-stacks/)
[Github](https://github.com/tharmoth/leetcode)

### Tags:
#stack #queue


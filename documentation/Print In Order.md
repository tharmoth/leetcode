### Description

> The same instance of `Foo` will be passed to three different threads. Thread A will call `first()`, thread B will call `second()`, and thread C will call `third()`. Design a mechanism and modify the program to ensure that `second()` is executed after `first()`, and `third()` is executed after `second()`.
---
## Dumb Lock
### Method

This method involves only the time library and simulates the underlying functionality of the more complex python threading libraries. However it is not ultimately thread safe (it would be with Atomics in Java).

We simply create two Booleans to track if the first and second methods have been called and if the appropriate methods have not been called then we wait the thread.

### Complexity
Time Complexity - O(1) We are either waiting or printing
Space Complexity - O(1) We only store two locking booleans

### Code
```py
class Foo:  
  
    def __init__(self):  
        self.first_fired = False  
        self.second_fired = False  
  
    def first(self, printFirst: 'Callable[[], None]') -> None:  
  
        # printFirst() outputs "first". Do not change or remove this line.  
        printFirst()  
  
        self.first_fired = True  
  
    def second(self, printSecond: 'Callable[[], None]') -> None:  
  
        while not self.first_fired:  
            time.sleep(.001)  
  
        # printSecond() outputs "second". Do not change or remove this line.  
        printSecond()  
  
        self.second_fired = True  
  
    def third(self, printThird: 'Callable[[], None]') -> None:  
  
        while not self.first_fired or not self.second_fired:  
            time.sleep(.001)  
  
        # printThird() outputs "third". Do not change or remove this line.  
        printThird()
```
### Problems in my solution

I should really use the python threading libraries to do this properly. Doing it this method, while ultimately very similar to the final method, looks bad. 

---
### Links:

[Leetcode](https://leetcode.com/problems/print-in-order/)
[Github](https://github.com/tharmoth/leetcode)

### Tags:

#threading #redo

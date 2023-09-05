
### Description

> Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm). The order of the elements may be changed. Then return _the number of elements in_ `nums` _which are not equal to_ `val`.

---
## Single Iteration
### Method
The requirements of this problem required we remove each value ```val``` from the array ```nums``` in place. ie. by changing the input data structure rather than making a new one.

I wanted to solve this problem in O(n) by iterating through the list only once. To do this we increment a counter each time we encounter a ```val``` and use that to offset the index of non val values.

### Complexity
Time Complexity - This method is O(n) since it visits each value of the list once
Space Complexity - This method is O(1) since it only stores an offset and operates on the list.

### Code
```py
def removeElement(self, nums: List[int], val: int) -> int:  
    offset = 0  
    for i in range(len(nums)):  
        if nums[i] == val:  
            offset += 1  
        else:  
            nums[i - offset] = nums[i]  
    return len(nums) - offset
```

### Problems in my solution
I made it over complicate with two branches when only one was required. Instead of storing the offset, instead store the active index to get rid of the else clause.

---

### Links:

[Leetcode](https://leetcode.com/problems/remove-element/)
[Github](https://github.com/tharmoth/leetcode)

### Tags:

#array
### Description

> Given an integer array `nums`, find the subarray with the largest sum, and return its sum
---
## Method
### Running Total
The simplest way to solve this problem is by iterating through the array and storing the max seen total and the current total where the current total is either the current number or the previous current total plus the current number.


### Complexity
Time Complexity - O(n) we only need to iterate though the array once
Space Complexity - O(1) Were only storing two integers

### Code
```py
def maxSubArray(self, nums: List[int]) -> int:  
    total_max = -math.inf  
    current = 0  
  
    for num in nums:  
        current = max(current + num, num)  
        total_max = max(current, total_max)  
  
    return total_max
```
### Problems in my solution


---
### Links:

[Leetcode](https://leetcode.com/problems/maximum-subarray/description/)
[Github](https://github.com/tharmoth/leetcode)

### Tags:
#array #search 

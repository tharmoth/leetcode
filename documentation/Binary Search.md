### Description

> Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.
>
>You must write an algorithm with `O(log n)` runtime complexity.

see also [[Koko Eating Bananas]] for a twist on this problem.

---
## Naive Binary Search
### Method

In order to find our target using a naive binary search we want to check the middle between two left and right values and if the middle is not the value we are searching for if it is less than the value we are searching for set the left value to one plus the middle value and if it is greater set it to one plus the middle value. By doing this we cut our search space in half for each iteration of searching.
### Complexity

Time Complexity - O(log n) since each search cuts the space in half the worst case is O(log n)
Space Complexity - O(1)
### Code
```py
def search(self, nums: List[int], target: int) -> int:
	left = 0  
	right = len(nums) - 1  
	while left <= right:  
	    middle = int((left + right) / 2)  
	    if nums[middle] < target:  
	        left = middle + 1  
	    elif nums[middle] > target:  
	        right = middle - 1  
	    else:  
	        return middle  
	  
	return -1
```
### Problems in my solution
It performs rather worse than the other solutions on leetcode suggesting a faster implementation is possible. In fact I researched the problem and there is an implementation that can cut out one of the checks. 

Also, I remembered that I implemented this code in Leetcode 875. [[Koko Eating Bananas]]. Which was the first Leetcode I worked and shall write up now.


---
### Links:

[Leetcode](https://leetcode.com/problems/binary-search/)
[Github](https://github.com/tharmoth/leetcode)
[Wikipedia](https://en.wikipedia.org/wiki/Binary_search_algorithm)

### Tags:
#binary-search #array 

### Description

> Koko loves to eat bananas. There are `n` piles of bananas, the `ith` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.
>
>Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.
>
>Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
>
>Return _the minimum integer_ `k` _such that she can eat all the bananas within_ `h` _hours_.

See also [[Binary Search]]

---
## Method
### Binary Search
We need to narrow down the number of bananas that koko can eat. We know that the slowest she can eat bananas is one per hour and the fastest is the largest pile per hour and that somewhere in that range is the value that we are searching for. This calls for a binary search were we check if the middle value is a valid number and adjust accordingly. 

Twists on a normal binary search in this case are the potential for repeated values and that we are looking for the lowest valid value rather than any given one.

For each iteration we check if the middle value is valid and if it is than we know koko can eat more bananas and if it is not than we know koko needs to eat fewer bananas. When the min number of bananas meets or exceeds the max number of bananas that is the correct value.

### Complexity
Time Complexity - O(log n), This being a binary search we cut the search space in half for each iteration
Space Complexity - O(1)

### Code
```py
def minEatingSpeed(self, piles: List[int], h: int) -> int:  
    left = 1  
    right = max(piles)  
  
    while left < right:  
        middle = int((left + right) / 2)  
        if self.check(piles, h, middle):  
            right = middle  
        else:  
            left = middle + 1  
  
    return left  
  
def check(self, piles: List[int], h: int, num: int) -> int:  
    return sum(math.ceil(pile / num) for pile in piles) <= h
```
### Problems in my solution
Compared to other python solutions my memory usage is rather poor. I'm not entirely sure why  as of yet. Perhaps it's my usage of math.ceil

---
### Links:

[Leetcode](https://leetcode.com/problems/koko-eating-bananas/)
[Wikipedia](https://en.wikipedia.org/wiki/Binary_search_algorithm#Variations)
[Github](https://github.com/tharmoth/leetcode)

### Tags:
#binary-search 

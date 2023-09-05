### Description

>You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in **adjacent** plots.
>
>Given an integer array `flowerbed` containing `0`'s and `1`'s, where `0` means empty and `1` means not empty, and an integer `n`, return `true` _if_ `n` _new flowers can be planted in the_ `flowerbed` _without violating the no-adjacent-flowers rule and_ `false` _otherwise_.

---
## Iteration

### Method

To solve this problem we need to iterate through the array and check if any given spot is a valid location. To do this we need to look ahead one and behind one spot for zeros. Problems to be extra cognizant of are boundary problems as the ends of the array are valid locations, but they are missing one adjacent location.

In my solution I modified the input `flowerbed` array. This is not necessary but is for simplicity. I could also store if the last location contains a flower as to avoid modifying the input array. Though that does make the code a little more complex.
### Complexity

Time Complexity - O(n) We only iterate through the array once
Space Complexity - O(1) We only store the valid spots integer
### Code

```py
def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:  
    valid_spots = 0  
    for i in range(len(flowerbed)):  
        if (flowerbed[i] == 0  
                and (i == 0 or flowerbed[i - 1] == 0)  
                and (i + 1 == len(flowerbed) or flowerbed[i + 1] == 0)):  
            valid_spots += 1  
            flowerbed[i] = 1  
    return n <= valid_spots
```

### Problems in my solution

I could have achieved performance improvements at the expense of complexity by checking for early exit conditions

---
### Links

[Leetcode](https://leetcode.com/problems/can-place-flowers/)
[Github](https://github.com/tharmoth/leetcode)
### Tags:

#array
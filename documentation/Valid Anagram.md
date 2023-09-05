### Description

> Given two strings `s` and `t`, return `true` _if_ `t` _is an anagram of_ `s`_, and_ `false` _otherwise_.
>
>An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

---
## Dictionary Cache
### Method
In order to determine if an anagram is valid I built a dictionary by iterating through both of the strings and for each character incrementing (in s) or decrementing (in t) the value of the corresponding key. Then I search the values for any value that is not zero. 

If there is a non zero value then the two strings are not a valid anagram as one must have had a extra letter the other didn't.
### Complexity

Time Complexity O(2n) - We iterate through the strings once and over the values once

Space Complexity O(n) - We store a dictionary worst case containing all of the chars in both of the strings
### Code
```py
if len(s) != len(t):  
    return False  
  
cache = {}  
for s_char, t_char in zip(s, t):  
    cache[s_char] = cache.get(s_char, 0) + 1  
    cache[t_char] = cache.get(t_char, 0) - 1  
  
return not any(cache.values())
```
### Problems in my solution
We could have reduced space complexity by manipulating the other string but this would have caused the time complexity to go to O(n^2) due to searching the other string but would make it so that more data is not needed to be stored.

---
### Links:

[Leetcode](https://leetcode.com/problems/valid-anagram/)
[Github](https://github.com/tharmoth/leetcode)

### Tags:

#string 
### Description

> An image is represented by an `m x n` integer grid `image` where `image[i][j]` represents the pixel value of the image.
>
>You are also given three integers `sr`, `sc`, and `color`. You should perform a **flood fill** on the image starting from the pixel `image[sr][sc]`.
>
>To perform a **flood fill**, consider the starting pixel, plus any pixels connected **4-directionally** to the starting pixel of the same color as the starting pixel, plus any pixels connected **4-directionally** to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with `color`.
>
>Return _the modified image after performing the flood fill_.


---
## Recursive Search
### Method

For each point check the adjacent points if it is the initial color of the current point and if so recursively flood fill them. Do this for up down left and right.
### Complexity

Time Complexity - O(n) each point must be visited once
Space Complexity - O(n) potentially a pointer to each location could be stored. 
### Code
```py
def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:  
    base_color = image[sr][sc]  
    image[sr][sc] = color  
    for i_r, i_c in zip([sr + 1, sr - 1, sr, sr], [sc, sc, sc - 1, sc + 1]):  
        if (0 <= i_r < len(image)  
                and 0 <= i_c < len(image[0])  
                and image[i_r][i_c] == base_color  
                and image[i_r][i_c] != color):  
            image = self.floodFill(image, i_r, i_c, color)  
  
    return image
```
### Problems in my solution
It seems a little slower than other solutions though still in the same O(n) minor improvements could be made.

---
### Links:

[Leetcode](https://leetcode.com/problems/flood-fill/)
[Github](https://github.com/tharmoth/leetcode)

### Tags:

#array #graph
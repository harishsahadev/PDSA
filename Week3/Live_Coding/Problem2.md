Write a function `backandforth(AList, end1, end2)` to return the maximum number of possible route between node `end1` and node `end2` in the undirected graph without going through the same node again with exception to `end1` and `end2`. The connectivity details between nodes are provided by the adjacency list `AList`.

**Sample Input**
```python
AList = {
 0: [2, 3, 6],
 2: [0, 3, 4],
 3: [4, 2, 0, 1],
 6: [1, 5, 0],
 1: [3, 6, 5],
 4: [2, 3, 5],
 5: [1, 4, 6]
 }
end1 = 0
end2 = 1
```

**Sample Output**
```
3
```

**Graphical Representation**

![Prob 2](https://user-images.githubusercontent.com/94980115/193631796-3675616f-1709-4469-bd6d-69e9ebd5f1da.png)

**Explanation**

The possible paths are [0, 3, 1],  [0, 6, 1] and [0, 2, 4, 5, 1]. Hence the answer is 3.

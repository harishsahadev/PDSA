The express train routes are provided in the adjacency list `AList`, here you have to find the route from `start` to `end` with minimum number of hops possible. Write a function `minimumhops(AList, start, end)` to return the cities to be visited starting from `start` to `end`. Return a list with only `start` if the `end` is not reachable.

**Sample Input**
```python
start = 8
end = 7
AList = {
            0: [8],
            8: [0, 9],
            1: [3, 5, 8],
            3: [1, 2, 7],
            5: [4],
            2: [8, 9],
            9: [1],
            7: [8],
            4: [2, 6],
            6: [9]
    }
```

**Sample returned list**
```python
[8, 9, 1, 3, 7]
```
**Sample output**
```python
5
```
**Graphical representation**

![download](https://user-images.githubusercontent.com/94980115/193631204-1bdb4c50-65c4-4dbf-8dad-18c08eb6a17b.png)

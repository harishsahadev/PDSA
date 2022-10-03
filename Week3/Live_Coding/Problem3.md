A group of workers have to complete a list of tasks, those tasks have dependencies within the task list. But the workers prefer some interesting task and hates to do some boring task. They always do the most interesting one among the available tasks to be done.

Write a function `coolWorkers(AList, preference)` to return the order in which the tasks will be done. `AList` is the adjacency list with the dependencies and `preference` is the tasks sorted in preferred order, in which task in index `0` is the most preferred and index `-1`(last element) be the least preferred.

**Sample Input**

```python
AList = {0: [1, 2, 3], 1: [7], 2: [3, 5], 3: [4, 1, 8], 7: [], 5: [6, 1], 4: [5, 7], 8: [5], 6: [7]}
preference = [1, 3, 2, 6, 8, 5, 4, 0, 7]
```

**Sample Output**

```
[0, 2, 3, 8, 4, 5, 1, 6, 7]
```

**Graphical representation**

![download](https://user-images.githubusercontent.com/94980115/193632103-a1776f7c-f7d4-49a4-8259-45556dfbde44.png)

Given a list `L` of random numbers and another number `pairSum`, find whether there exists two numbers in the list such that their sum is equal to `pairSum`. 

Write a Python function ***findPair(L, pairSum)*** that return `True` if there exist a pair of integers in `L` whose sum is equal to `x`, `False` otherwise.. Try to write a solution which is $O(n~log~n)$ or better.

**Hint:** Try to sort the list first.



For example consider the below list. We need to find if there exists any pair whose sum is equal to 21. 11+10 = 21. So the function should return True.

For the same list if we want to find if there exist any pair whose sum is equal to 2. Clearly there is no such pair so the function should return False.

**Sample Input 1**

```
10 4 11 5 1 8 7
21
```

**Sample Output 1**

```
True
```

**Sample Input 2**

```
10 4 11 5 1 8 7
2
```

**Sample Output 2**

```
False
```

### 

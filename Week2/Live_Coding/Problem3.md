You have a deck of shuffled cards ranging from 0 to 100,000,000. There are 2 sub-ordinate below you and two subordinates below them and it goes on.

- The job of the sub-ordinate is to split the deck of cards that they received and give it to two sub-ordinate of them. If they receive a deck of cards from their subordinates, they merge it in an ascending order and give it their higher level.

- If a subordinate received only two card, then he/she himself/herself arrange in ascending order give it back that to the superior.

- If a subordinate received only one card, then he/she will give back that to the superior.



```
Terminology:

(67) subordinate number 67

[1, 3, 5, 2] -> [1, 2, 3, 5] deck of cards got -> deck of cards returned

--------------------------------

(0) [3, 1, 2, 0, 5] -> [0, 1, 2, 3, 5]
|
|--(1) [3, 1] -> [1, 3]
|
|--(2) [2, 0, 5] -> [0, 2, 5]
    |
    |--(3) [2] -> [2]
    |
    |--(4) [0, 5] -> [0, 5]
```

Your task is to find how many people (including you) are required to sort the cards and print the sorted deck of cards and number of people required as a tuple.

Write the function **def subordinates(L):**

```python
def subordinates(L):
```

**Sample input 1**

```
[194, 69, 103, 150, 151, 44, 103, 98]
```

**Output**

```
([44, 69, 98, 103, 103, 150, 151, 194], 7)
```

**Sample input 2**

```
[10, 33, 45, 67, 92, 100, 5]
```

**Output**

```
([5, 10, 33, 45, 67, 92, 100], 7)
```

### 


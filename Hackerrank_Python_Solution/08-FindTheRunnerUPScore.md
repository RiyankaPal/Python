# Find the Runner-Up Score

## Problem
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given a list of scores. Store them in a list and find the score of the runner-up.

## Input Format
- The first line contains an integer `n`, the number of participants.
- The second line contains an array `A[]` of `n` integers, each separated by a space.

## Constraints
2 <= n <= 10
-100 <= A[i] <= 100

## Output Format
Print the runner-up score.

```
Sample Input:
5
2 3 6 6 5
```
```
Sample Output :
5
```

#### Explanation
Given list is `[2,3,6,6,5]`. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.



## Solution

```python
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    Thisset = sorted(set(arr))
    print(Thisset[-2])

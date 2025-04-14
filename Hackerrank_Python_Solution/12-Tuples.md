# Tuples:

## Solution:

```python
   if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t=tuple(integer_list)
    print(hash(t))
```
## Explanation:
**NOTE:** It will work only on pypy 3 




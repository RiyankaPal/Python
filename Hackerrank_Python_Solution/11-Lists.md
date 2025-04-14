# Python List:

## Solution:

```python

if __name__ == '__main__':
    N = int(input())
    x=[]
    for _ in range(N):
        user_input=input()
        parts=user_input.split()
        command=parts[0]
       
        if command=='insert':
            x.insert(int(parts[1]),int(parts[2]))
        elif command=='print':
            print(x)
        elif command=='remove':
            x.remove(int(parts[1]))
        elif command=='append':
            x.append(int(parts[1]))
        elif command=='sort':
            x.sort()
        elif command=='pop':
            x.pop()
        else :
            x.reverse()
```




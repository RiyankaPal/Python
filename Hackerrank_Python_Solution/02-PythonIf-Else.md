# Python If-Else:

## Solution:

```python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if (n%2!=0):
        print('Weird')
    elif (n%2==0 and n>=2 and n<=5):
        print('Not Weird')
    elif (n%2==0 and n>=6 and n<=20):
        print('Weird')
    else:
        print('Not Weird')
```
## Explanation

- `strip():`
  - input() gets a string from the user.
  - strip() removes leading and trailing whitespace from that string. This includes:
    - Spaces
    - Tabs (\t)
    - Newlines (\n)

* `if __name__ == '__main__':`
  - Run the following block only if this file is being run directly, not imported as a module.


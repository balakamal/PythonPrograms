
from collections import Counter
n = int(input())
if(n >= 1 and n <= 1000):
    b = bin(n)
    b = b[2:]
    c = Counter(b)
    if c.get('1') % 2 == 0:
        print("Even Parity")
    else:
        print("Odd Parity")
else:
    print("Wrong Input")

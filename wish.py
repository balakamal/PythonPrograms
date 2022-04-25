import time
from random import randint

for _ in range(45):
    print('')

s = ''

for i in range(1000):
    count = randint(1, 100)
    while count > 0:
        s += ' '
        count -= 1
    if i % 10 == 0:
        print(s + 'Happy Birthday')
    else:
        print(s + '*')
    s = ''

    time.sleep(0.1)

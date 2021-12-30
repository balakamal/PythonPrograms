days = int(input())
v = [1, 3]
if(days == 1):
    print(1)
elif(days == 2):
    print(3)
else:
    virus = 3
    for i in range(2, days):
        virus += virus*2
        v.append(virus)
        if(i >= 5 and i != days-1):
            virus -= v.pop(0)
            print(virus)
    print(virus)

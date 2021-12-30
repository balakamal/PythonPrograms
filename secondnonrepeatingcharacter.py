s = input()
j = []
if(len(s) > 30):
    print("Wrong Input")
else:
    for i in s:
        k = s.count(i)
        if(k == 1):
            j.append(i)
    if(len(j) < 2):
        print("Invalid string")
    else:
        print(j[1])

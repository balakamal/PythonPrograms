n = input()
if(int(n) <= 1 or int(n) >= 1000000):
    print("Wrong Input")
elif('0' in n and n[0] != '0'):
    print("Valid Number")
else:
    print("Invalid Number")

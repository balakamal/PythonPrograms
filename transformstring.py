
def transformString(S, T):
    if(sorted(S) == sorted(T)):
        print(s[::-1])
        if(s[::-1] == T):
            return 1

    return -1


s = input()
t = input()
print(transformString(s, t))

def SmallestCharacter(s):
    s = [i for i in s]
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    s.sort()
    for i in range(len(s)):
        if(s[i] != alpha[i]):
            return(alpha[i])


print(SmallestCharacter(input()))

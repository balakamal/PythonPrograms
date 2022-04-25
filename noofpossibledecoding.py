class example:
    def decoding(self, input1):
        l = [int(i) for i in input1]
        res = 1
        for i in range(len(l)-1):
            n = l[i]*10+l[i+1]
            if(n < 27):
                res += 1
        return(res)


ex = example()
print(ex.decoding(input()))

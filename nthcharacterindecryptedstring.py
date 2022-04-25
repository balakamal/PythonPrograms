class example:
    def find_element(self, input1, input2):
        res = ''
        for i in range(0, len(input1), 2):
            res += input1[i]*int(input1[i+1])
        return(res[input2-1] if len(res) >= input2 else "-1")


s = input()
n = int(input())
ex = example()
print(ex.find_element(s, n))

import pandas as pd

dt = pd.read_excel(
    'C:/Users/924028/Downloads/II B.TECH II SEM R16 RESULTS NOV-2020.xls', sheet_name=None)


HTNO = 'Htno'

'''
                Preprocessing
================================================
Removed Whitespaces(if any) in Hall ticket number column
'''


def preprecossing():

    for i in list(dt.keys())[:-1]:
        dt[i][HTNO] = dt[i][HTNO].map(lambda x: str(
            x).lstrip().rstrip().replace(' ', ''))
    # print(dt)


'''Finding details of required batch'''
ht_regex = '19X45A03'
data = []


def find_details():  # sourcery skip: convert-to-enumerate
    for i in list(dt.keys())[:-1]:
        row = 0
        for j in dt[i][HTNO]:
            if(ht_regex in j):
                data.append(list(dt[i].iloc[row]))
            row += 1
    '''for i in data:
        print(i)'''


def convert_grade_to_gradepoints():
    grades = {'O': 10, 'S': 9, 'A': 8, 'B': 7,
              'C': 6, 'D': 5, 'F': 0, 'ABSENT': 0}
    for i in data:
        i[3] = grades[i[3]]
    print(data)


'''def calculate_GPA():  # sourcery no-metrics
    i=0
    fi=""
    ci=0.0
    gi=0.0
    sgpa=0.0

    result=[]
    name=""
    l=0
    F=0     

    s=int(input("Enter no.of subjects:"))
    i=0
    ap=0
    list1=[]
    list2=[]
    
    for k in range(0,s):
        if(a[4][i]!=0):
            ci+=a[4][i]    
            gi+=a[4][i]*b[i]
            i+=1
        else:
            i+=1
            F+=1
    if(gi!=0 and ci !=0):
        sgpa=gi/ci
    ci=0
    gi=0
    if(F!=0):
        print(a[0][l],"\t",round(sgpa,2),"& Failed in ",F," Subjects")
    else:
        print(a[0][l],"\t",round(sgpa,2))
        list1.append(a[0][l])
        list2.append(round(sgpa,2))
        ap+=1        
    l+=s
    F=0
    i=0



    sub=[]
    sub1=[]
    for k in range(s):
        sub.append(0)
        sub1.append([])

    for j in range(0,n):
        for k in range(0,s):
            if(a[4][i]==0):
                sub[k]+=1
                sub1[k].append(a[0][i])
                i+=1
            else:
                i+=1
    print("\n\n")
    print("OVERALL PASS percentage: ",round(((ap*100)/n),2),"\n\n\n")
    print("Total number of students ALL PASS: ",ap,"\n\n\n")

    print("TOP 5 MEMBERS")
    x = zip(list1, list2)
    x=tuple(x)
    def Sort_Tuple(x):    
        return(sorted(x, key = lambda x: x[1], reverse=True))
    y=Sort_Tuple(x)
    for k in range(5):
        print(y[k])
    print("\n\n")

    print("Summary\n-------\n\n")
    for k in range(s):
        
        print("SUBJECTS \t \t NO.OF FAILURES \t\t PASS PERCENTAGE\n--------------------------------------------------------------------------")
        print(a[2][k],"\t||\t",sub[k],"\t||\t",round(((n-sub[k])/n)*100,2),"\n")
        print(sub1[k],"\n\n")'''

preprecossing()
find_details()
convert_grade_to_gradepoints()

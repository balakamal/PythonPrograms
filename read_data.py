import pandas as pd
from collections import defaultdict
import json


def preprecossing():  # sourcery skip: convert-to-enumerate

    for i in list(dt.keys())[:-1]:
        '''
                        Preprocessing
        ================================================
        Removing Whitespaces(if any) in Hall ticket number and Subject Code columns
        '''
        dt[i][HTNO] = dt[i][HTNO].map(lambda x: str(
            x).lstrip().rstrip().replace(' ', ''))
        dt[i][SUBCODE] = dt[i][SUBCODE].map(lambda x: str(
            x).lstrip().rstrip().replace(' ', ''))
        '''
                        Finding details of required batch
        ===================================================================================
        Based on the Hall Ticket number expression details of students are extracted and stored those in data variable.
        '''
        row = 0
        for j in dt[i][HTNO]:
            if(ht_regex in j):
                data.append(list(dt[i].iloc[row]))
            row += 1
    '''
            Converting grades to grade points
    ======================================================
    '''
    grades = {'O': 10, 'S': 9, 'A': 8, 'B': 7,
              'C': 6, 'D': 5, 'F': 0, 'ABSENT': 0}
    for i in data:
        i[3] = grades[i[3]]

    # printing data
    for i in data:
        print(i)


def calculate_gpa():

    htno = data[0][0]

    l = []
    failed = defaultdict(list)

    for i in data:
        if htno != i[0]:
            if l:
                total_credits = 0
                credits_X_grades = 0
                subjects = []
                grades = []
                credits = []
                for j in l:
                    subjects.append(j[2])
                    grades.append(j[3])
                    credits.append(int(j[4]))
                    total_credits += j[4]
                    credits_X_grades += j[3]*j[4]

                res[htno] = {'subjects': subjects, 'grades': grades, 'credits': credits, 'sgpa': round(
                    credits_X_grades/total_credits, 2) if grades.count(0) == 0 else 0}

                failed[grades.count(0)].append(htno)

            l = []
            htno = i[0]

        l.append(i)
        res['failed'] = failed
        print(res)
    with open('output.json', 'w') as outfile:
        json.dump(res, outfile, indent=4)


dt = pd.read_excel(
    'C:/Users/924028/Downloads/II B.TECH II SEM R16 RESULTS NOV-2020.xls', sheet_name=None)


HTNO = 'Htno'
SUBCODE = 'Subcode'
ht_regex = '18X41A12'
data = []
res = {}

preprecossing()
calculate_gpa()

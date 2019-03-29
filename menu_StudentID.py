# Author:
# Date:


# Please write your own program here
import sys
import os
import nerdScore_StudentID as nerdscore

menuOptions = {1: 'name', 2: 'Fandom_Score', 3: 'Hobbies_Score', 4: 'NoOfSports', 5: 'CalculateNerdScore', 6: 'PrintRating'}
menuInput = None;
#fandomScore, hobbiesScore,sportssum = None;


class Student:
    def __init__(self, name, Fandom_Score, Hobbies_Score, NoOfSports):
        self.name = name
        self.Fandom_Score = Fandom_Score
        self.Hobbies_Score = Hobbies_Score
        self.NoOfSports = NoOfSports

student = Student(None, None, None, None)
studentList = [];


def name():
    print('inside name')
    try:
        name = str(input('enter student name'))
        student.name = name

    except:
        print('error')
def Fandom_Score():
    print('validating fandom score')
    fandomscorevalidated = False
    while (not fandomscorevalidated):
        try:
            fandom_score = int(input('enter fandom score'))
            if (fandom_score < 0):
                raise TypeError
            else:
                fandomscorevalidated = True
                return fandom_score
        except:
            print('please try again for fandom score')


def Hobbies_Score():
    hobbiesscorevalidated = False
    print('validating Hobbies_Score as a multiple of 4')
    while (not hobbiesscorevalidated):
        try:
            hobbies_score = int(input('enter hobbies score'))
            if (hobbies_score < 0 or (hobbies_score % 4) > 0):
                raise TypeError
            else:
                hobbiesscorevalidated = True
                return hobbies_score
        except:
            print('please try again for hobbies score')


def NoOfSports():
    NoOfSports_validation = False
    print('validating Hobbies_Score as a multiple of 4')
    while (not NoOfSports_validation):
        try:
            noofsports = int(input('enter no of sports score'))
            if (noofsports < 0):
                raise TypeError
            else:
                NoOfSports_validation = True
                return noofsports
                print(student.name)
                # print(student.name + student.NoOfSports + student.Hobbies_Score)
        except:
            print('please try again for no of sports')
def CalculateNerdScore():
    skillScore = 0  # intialize the output list

    # Please write your own program here
    try:
        x = student.Fandom_Score;
        y = student.Hobbies_Score;
        z = student.NoOfSports;

        if( x == None or y == None or z == None):
            raise ValueError;

        skillScore = (((((y * y) * 42) / (z + 1))) ** (1 / 2))*x
        student.Fandom_Score = None
        student.Hobbies_Score = None
        student.NoOfSports = None
        print(skillScore)
        studentList.append(skillScore)
    except:
        print('error calculating result all values not entered')
        skillScore = 0

def nerdRating(studentscore):
    rating = 'undefined'
    if(studentscore < 1):
        return 'NerdLite'
    elif (studentscore<10 ):
        return 'Nerdlinger'
    elif (studentscore<100 ):
        return 'Nerdl'
    elif (studentscore < 500 ):
        return 'Nerdington'
    elif (studentscore <1000):
        return 'Nerdrometa'
    elif (studentscore < 2000):
        return 'Nerd Supreme'



def PrintRating():
    for student in studentList:
        print(str(studentList.index(student)));
        print( str(nerdRating(student)))
        print('student ' + str(studentList.index(student)) + ' nerdClass is: '+ str(nerdRating(student)))




def menu_validation(menuOptions):
    userip = int(input('enter menu option'))
    if (userip > 6 or userip < 1):
        raise IOError

        print(menuOptions[userip])
    if(userip > 4 ):
        globals()[menuOptions[userip]]()
    else:
        setattr(student, menuOptions[userip], globals()[menuOptions[userip]]())
        print(getattr(student, menuOptions[userip]))



while (True):
    # student1 = Student(None, None, None, None)
    print('\n Options in menu\n ');
    for option in menuOptions:
        print(menuOptions[option] + '\n')
    try:
        validatedmenuoption = menu_validation(menuOptions)
    except :

        print('error try again\n\n\n\n')

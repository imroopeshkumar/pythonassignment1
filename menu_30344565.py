# Author:
# Date:


# Please write your own program here
import sys
import os
import nerdScore_30344565 as nerdscore

menuOptions = {1: 'Fandom Score', 2: 'Hobbies Score', 3: 'Sport Items Owned', 4: 'Calculate Nerd Score', 5: 'Print Nerd Rating'} #options to display in menu
menuMethods = {1:'Fandom_Score', 2: 'Hobbies_Score', 3: 'NoOfSports', 4: 'CalculateNerdScore', 5: 'PrintRating'} #options to use to call method using global()
menuInput = None #used to take user input
#fandomScore, hobbiesScore,sportssum = None


class Student: #to store values of students entered
    def __init__(self, name, Fandom_Score, Hobbies_Score, NoOfSports): #to initialize class
        self.name = name
        self.Fandom_Score = Fandom_Score
        self.Hobbies_Score = Hobbies_Score
        self.NoOfSports = NoOfSports

student = Student(None, None, None, None) #create object with empty attributes
studentList = [] #list to store values of students


# def name():
#     print('inside name')
#     try:
#         name = str(input('enter student name'))
#         student.name = name
#
#     except:
#         print('error')
def Fandom_Score(): #to calculate fandom score
    print('\n---validating fandom score---')
    fandomscorevalidated = False #for validation exit if this variable is set
    while (not fandomscorevalidated):
        try:
            fandom_score = int(input('\nenter fandom score')) #take input from user
            if (fandom_score < 0): #validation
                raise ValueError #if <0 raise exception
            else:
                fandomscorevalidated = True #set validation variable
                return fandom_score #return fandom score
        except:
            print('please try again for fandom score') #print error message for wrong value


def Hobbies_Score(): #to calculate hobbies score
    hobbiesscorevalidated = False #validation varibale
    print('\n---validating Hobbies_Score as a multiple of 4---')
    while (not hobbiesscorevalidated):
        try:
            hobbies_score = int(input('\nenter hobbies score as a multiple of 4')) #take input from user
            if (hobbies_score < 0 or (hobbies_score % 4) > 0):
                raise ValueError
            else:
                hobbiesscorevalidated = True
                return hobbies_score
        except:
            print('please try again for hobbies score') #error message


def NoOfSports(): #to read sport items owned
    NoOfSports_validation = False #validation variable
    print('---validating Sport Score---')
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
            print('please try again for no of sports') #print error message
def CalculateNerdScore(): #to calculate nerd score
    skillScore = 0  # intialize the output list

    # Please write your own program here
    try:
        x = student.Fandom_Score;
        y = student.Hobbies_Score;
        z = student.NoOfSports;

        if( x == None or y == None or z == None): #if any value if not entered raise exception
            raise ValueError;

        skillScore = (((((y * y) * 42) / (z + 1))) ** (1 / 2))*x #calculate nerdscore
        student.Fandom_Score = None #reset variables
        student.Hobbies_Score = None
        student.NoOfSports = None
        print(skillScore)
        studentList.append(skillScore)
    except:
        print('error calculating result all values not entered') #print error message
        skillScore = 0

def nerdRating(studentscore): #to show class of nerd
    rating = 'undefined'
    if(studentscore < 1):
        return 'NerdLite'
    elif (studentscore<10 ):
        return 'Nerdling'
    elif (studentscore<100 ):
        return 'Nerdlinge'
    elif (studentscore < 500 ):
        return 'Nerd'
    elif (studentscore <1000):
        return 'Nerdington'
    elif (studentscore < 2000):
        return 'Nerdometa'
    elif(studentscore >= 2000):
        return 'Nerd Supreme'
    else :
        return rating;



def PrintRating():
    if(len(studentList)>0):
        nerdCount_list = [0] * 7  # intialize the output list
        for studentscore in studentList: #to show list with class of nerd
            if (studentscore < 1):
                nerdCount_list[0] += 1
            elif (studentscore < 10):
                nerdCount_list[1] += 1
            elif (studentscore < 100):
                nerdCount_list[2] += 1
            elif (studentscore < 500):
                nerdCount_list[3] += 1
            elif (studentscore < 1000):
                nerdCount_list[4] += 1
            elif (studentscore < 2000):
                nerdCount_list[5] += 1
        print('findclass result is: ')
        print(nerdCount_list)
        for student in studentList:
            # print(str(studentList.index(student)));
            # print( str(nerdRating(student)))
            print('student ' + str(studentList.index(student)) + ' nerdClass is: '+ str(nerdRating(student))) #to show nerd class of each student
    else:
        print('no students found in list') #error message if list is empty




def menu_validation(menuOptions): #to check menu validation
    userip = int(input('enter menu option')) #take menu input
    if (userip > 6 or userip < 1):
        raise ValueError

        print(menuOptions[userip])
    if(userip > 3 ):
        globals()[menuMethods[userip]]() #call method on string

    else:
        setattr(student, menuMethods[userip], globals()[menuMethods[userip]]())#setattribute for object
        print('->Entered value: '+str(getattr(student, menuMethods[userip])))
        print('success')


while (True):
    # student1 = Student(None, None, None, None)
    print('\n Options in menu\n ');
    for option in menuOptions:
        print(str(option) + ')'+ menuOptions[option] + '\n')
    try:
        validatedmenuoption = menu_validation(menuOptions)
    except Exception as e:
        print(e)
        print('error try again enter numeric menu option\n\n\n\n')

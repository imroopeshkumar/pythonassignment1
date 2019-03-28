#Author: 
#Date:


#Please write your own program here
import sys
import os
import nerdScore_StudentID as nerdscore

menuOptions = {1: 'Fandom_Score', 2: 'Hobbies_Score', 3: 'NoOfSports', 4: 'CalculateNerdScore', 5: 'PrintRation', 6: 'name'}
menuInput = None;

class Student:
    def __init__(self, name, Fandom_Score, Hobbies_Score, NoOfSports):
        self.name = name
        self.Fandom_Score = Fandom_Score
        self.name = Hobbies_Score
        self.name = NoOfSports

def Fandom_Score():
    print('validating fandom score')
    fandomscorevalidated = False
    while(not fandomscorevalidated):
        try:
            fandom_score = int(input('enter fandom score'))
            if(fandom_score < 0):
                raise TypeError
            else:
                fandomscorevalidated = True
                return fandom_score
        except:
            print('please try again for fandom score')

def Hobbies_Score():
        hobbiesscorevalidated = False
        print('validating Hobbies_Score as a multiple of 4')
        while(not hobbiesscorevalidated):
            try:
                hobbies_score = int(input('enter hobbies score'))
                if(hobbies_score < 0 or (hobbies_score % 4) > 0):
                    raise TypeError
                else:
                    hobbiesscorevalidated = True
                    return hobbies_score
            except:
                print('please try again for hobbies score')

                





def NoOfSports():
        NoOfSports_validation = False
        print('validating Hobbies_Score as a multiple of 4')
        while(not NoOfSports_validation):
            try:
                noofsports = int(input('enter no of sports score'))
                if(noofsports < 0):
                    raise TypeError
                else:
                    NoOfSports_validation = True
                    return noofsports
                    print(student.name)
                    #print(student.name + student.NoOfSports + student.Hobbies_Score)
            except:
                print('please try again for no of sports')






def CalculateNerdScore():
    try:
        nerdscore.calculateSkillEquation(FandomScore, HobbiesScore, SportsNum)
    except:
        print('error calculating')
        return 0

def PrintRating():
    pass


def name(student):
    print('inside name')
    try:
        name = str(input('enter student name'))
        student.name = name

    except:
        print('error')





def menu_validation(student, menuOptions):
    userip = int(input('enter menu option'))
    if(userip > 6 or userip< 1):
        raise TypeError
    else:
        
        #if(userip == 1):
            #fandom_score = Fandom_Score_validation()
            print(menuOptions[userip])
            if(menuOptions[userip]=='CalculateNerdScore'):
                CalculateNerdScore(getattr(student, menuOptions[1]),getattr(student, menuOptions[2]),getattr(student, menuOptions[3]))
            setattr(student, menuOptions[userip], globals()[menuOptions[userip]]())
            print(getattr(student, menuOptions[userip]))
        #elif(userip == 2):
            #Hobbies_Score_validation()
            #pass
        #elif(userip == 3):
            #NoOfSports_validation()
           # pass
        #elif(userip == 4):
            #CalculateNerdScore()
            #pass
        #elif(userip == 5):
            #PrintRating()
            #pass
        #else:
            #GetName()
            #pass
        
while(True):
    student1 = Student(None, None, None, None)
    for option in menuOptions:
        print(menuOptions[option]+'\n')
    try:
        validatedmenuoption = menu_validation(student1, menuOptions)
    except:
        print('error try again\n\n\n\n')
      



        






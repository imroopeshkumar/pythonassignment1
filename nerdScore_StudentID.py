# Author:
# Date:

# Functionality: cailculate the skill score by the equation
# x, y, z are inputs
def calculateSkillEquation(FandomScore, HobbiesScore, SportsNum):
    skillScore = 0  # intialize the output list

    # Please write your own program here

    x = FandomScore
    y = HobbiesScore
    z = SportsNum;
    try:
        skillScore = (((((y * y) * 42) / (z + 1))) ** (1 / 2))*x
    except:
        print('error calculating result')
        skillScore = 0

    return skillScore


if __name__ == '__main__':

    FandomScore, HobbiesScore, SportsNum = 1, 4, 1  # the output should be 18.33030277982336

    try:
        print(calculateSkillEquation(FandomScore, HobbiesScore, SportsNum))

    except Exception as e:
        print(e)
        raise

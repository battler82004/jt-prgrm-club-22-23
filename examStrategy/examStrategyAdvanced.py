# James Taddei
# Exam Strategy (Bloomsburg '19 #3)
# 9/11/22

# Variable inputs
examScore1 = float(input("Exam score 1: "))
examScore2 = float(input("Exam score 2: "))
examScore3 = float(input("Exam score 3: "))

# Calculations
pointsAlready = examScore1 + examScore2 + examScore3
pointsPossible = pointsAlready + 100

# Determines the highest possible grade and the num of points needed for it
if (pointsPossible >= 360):
    possibleGrade = 'A'
    questionsNeeded = 360 - pointsAlready
elif (pointsPossible >= 320):
    possibleGrade = 'B'
    questionsNeeded = 320 - pointsAlready
elif (pointsPossible >= 280):
    possibleGrade = 'C'
    questionsNeeded = 280 - pointsAlready
elif (pointsPossible >= 240):
    possibleGrade = 'D'
    questionsNeeded = 240 - pointsAlready
else:
    possibleGrade = 'F'

# Final output
if ((possibleGrade == 'F') or (questionsNeeded < 1)):
    print("Skip the fourth exam.")
else:
    print("Answer", questionsNeeded, "questions on the last exam to earn a grade of " + possibleGrade + ".")
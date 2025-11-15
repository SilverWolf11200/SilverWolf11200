import random
import tkinter as tk
from tkinter import simpledialog, messagebox


EasyQuestions = ["7951 - 2894 = ?","What is the area of a rectangle with length 5.8 and width of 3.4?","378/23 (round to nearest hundredth)","89*45","5 + 9 - 4 + 7","253+961-355","Solve for x, (answer lower number , space larger number): 5x = 6a + 2, a = 8","Solve for y: y^2 + 6y -7y = 0","100+200=300+400+590=?"]
MedQuestions = ["Triangle ABC has a base of 5cm, and height of 0.45m, what is the length of the hypotenuse (Rounded to the nearest hundredth?","The first 3 terms of a Arithmetic Sequence is 8,14,20. Find t30.","Give the first 10 numbers in the fibonacci sequence","Does the point (-4,-5) a solution to the following inequality:(f(x) = x^2 - 2x - 3? (T for yes, F for no)","Solve this system of equations: y = x^2 - 1 , y = 2x - 2"]
HardQuestions = ["A Arithmetic Series has the first term of a1 = 5 and last term of a27 = 83. Find the sum of this arithmetic series.","What is the common ratio of a geometric sequence with it's second term of 4 and it's eighth term of 256?","If the first term of a positive infinte geometric sequence is 8, and the fourth term is 1,what does this equal to","The base of a triangle is 5cm and the hypotenuse is 9 cm. What is the angle between the two lines?(rounded to nearest hundredth","How many roots does this equation have: (3x-2)/(2x-1) = 1/(2-x)","How many roots does this equation have: (3x^2 - 5x + 1 = 0)"," Find the Sum of this sequence:t1 = 4, t304 = 2125.","What is the sum of the factors of 4^10?","What is the sum of the factors of 6^11?","A ball drops from 50m high, it bounces 60% each time it touched the ground. What is the sum of the total distance travelled by the ball?","A ball is dropped from 130m high, it bounces 87% each time. What is the sum of the total distance travelled?","If there are 4 arithmetic terms between 3 and 24, what is the common difference?( answer in decimals )"]
EasyAnswers = ["5057","19.72","16.43","4005","17","859" , "10" ,"1590"]
MedAnswers = ["45.28","182","1,1,2,3,5,8,13,21,34,55","F","(-1,0)"]
HardAnswers = ["1188","2","16","56.25","2","2","323608","1398101","72559411","200","1900","4.2"]
Score = 0
Error = "Error detected and system shutdown activated"
RandomQuestion = [EasyQuestions,MedQuestions,HardQuestions]

def ask(title,prompt,intvalue = ""):
    s = simpledialog.askstring(title,prompt,initialvalue=intvalue,parent=root)
    if s is None:
        return ""
    if s.strip().lower()=="quit":
        messagebox.showinfo("Quit","Program closed",parent = root)
        raise SystemExit
    return "" if s is None else s

def _info(title, msg):
    messagebox.showinfo(title, msg, parent=root)




def EQuestionAsker():
    QuestionNumber = random.randint(0,len(EasyQuestions)-1)
    Question,Answer = EasyQuestions.pop(QuestionNumber),EasyAnswers.pop(QuestionNumber)
    Userinput = ask("Easy Question",f"{Question}\n\nEnter a Answer")
    EAnswerChecker(Userinput,Answer)
def MQuestionAsker():
    QuestionNumber = random.randint(0,len(MedQuestions)-1)
    Question,Answer = MedQuestions.pop(QuestionNumber),MedAnswers.pop(QuestionNumber)
    Userinput = ask("Medium Question",f"{Question}\n\nEnter a Answer")
    MAnswerChecker(Userinput,Answer)
def HQuestionAsker():
    QuestionNumber = random.randint(0,len(HardQuestions)-1)
    Question,Answer = HardQuestions.pop(QuestionNumber),HardAnswers.pop(QuestionNumber)
    Userinput = ask("Hard Question",f"{Question}\n\nEnter a Answer")
    HAnswerChecker(Userinput,Answer)
def Gamemodechooser():
    gamemode = ask("Mode Selection Screen:", f"\n\nSelect a Game mode style: \n Category \n Choose \n Random \n Challenge")


    if gamemode == "Category":
        Category()
    elif gamemode == "Choose":
        Choose()
    elif gamemode == "Random":
        Random()
    elif gamemode == "Challenge":
        Challenge()
    else:
        Error1()

def Questiontypepicker():
    Questiontype = ask("Game Difficulty:", f"\n\nSelect you difficulty: \n Easy \n Medium \n Hard")
    return Questiontype
def Error1():
    _info("Error","Syntax Error")
    raise SystemExit

def Category():
    difficultymode = Questiontypepicker()
    global Score
    for x in range (4):
        print(difficultymode)
        if difficultymode == "Easy":
            EQuestionAsker()
        elif difficultymode == "Med":
            MQuestionAsker()
        elif difficultymode == "Hard":
            HQuestionAsker()
        else:
            Error1()
    _info("Final Score", f"{Score}")

    return

def Choose():
    for x in range(4):
        difficultymode = Questiontypepicker()
        print(difficultymode)
        if difficultymode == "Easy":
            EQuestionAsker()
        elif difficultymode == "Med":
            MQuestionAsker()
        elif difficultymode == "Hard":
            HQuestionAsker()
        else:
            Error1()
    _info("Final Score", f"{Score}")


def Random():
    for x in range(8):
        difficulty = random.randint(0,2)
        print(difficulty)
        if difficulty == 0:
            EQuestionAsker()
        elif difficulty == 1:
            MQuestionAsker()
        elif difficulty == 2:
            HQuestionAsker()
        else:
            Error1()
    _info("Final Score", f"{Score}")
def Challenge():
    Oldscore = 0
    difficulty = 0
    global Score
    EQuestionAsker()
    if Score > Oldscore:
        if difficulty + 1 >= 3:
            difficulty = difficulty
        else:
            difficulty += 1
    else:
        if difficulty - 1 <= -1:
            difficulty = difficulty
        else:
            difficulty -= 1
    print(difficulty)

    for x in range (4):
        Oldscore = Score

        if difficulty == 0:
            EQuestionAsker()
        elif difficulty == 1:
            MQuestionAsker()
        elif difficulty == 2:
            HQuestionAsker()

        if Score > Oldscore:
            if difficulty + 1 >= 3:
                difficulty = difficulty
            else:
                difficulty += 1
        else:
            if difficulty - 1 <= -1:
                difficulty = difficulty
            else:
                difficulty -= 1
        print(difficulty)
    _info("Final Score", f"{Score}")



def EAnswerChecker(Userinput,Answer):
    global Score
    if Userinput == Answer:
         Score += 1
         _info("Correct",f"{Score}")
    else:
        _info("Wrong",f"{Score}")

def MAnswerChecker(Userinput,Answer):
    global Score
    if Userinput == Answer:
         Score += 2
         _info("Correct",f"{Score}")
    else:
        _info("Wrong",f"{Score}")

def HAnswerChecker(Userinput,Answer):
    global Score
    if Userinput == Answer:
         Score += 3
         _info("Correct",f"{Score}")
    else:
        Score -= 1
        _info("Wrong",f"{Score}")
root = tk.Tk()
root.geometry("100x100")
root.withdraw()
Gamemodechooser()


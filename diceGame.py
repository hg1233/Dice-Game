

################ Created By https://github.com/hg1233 ###############


# diceGame() related code
import random
from time import sleep
import os
dmin = 1
dmax = 6

#  Player Variables
P1Login = False
P2Login = False
P1Name = ""
P2Name = ""
P1Score = 0
P2Score = 0
P1Username = ""
P1Pass = ""
P2Username = ""
P2Pass = ""

SDP1 = 0
SDP2 = 0

# Dice Variables

P1R1 = 0
P1R2 = 0

P2R1 = 0
P2R2 = 0

#######PRINT CONSOLE LINES###########
def printer(x):                     #
    count = 1                       #
    while count <= x:               #
        print("")                   #
        count += 1                  #
#####################################

def register():
    username = input("Please create a username")
    password = input("Please input your desired password ")
    name = input("Please enter your name:")
    for line in open("accountfile.txt","r").readlines(): # Read the lines
        login_info = line.split() # Split on the space, and store the results in a list of 3 strings
        if username == login_info[0] and password == login_info[1] and name == login_info[2]:
            print("This account already exists.")
            return False
    file1 = open("accountfile.txt","a")
    file1.write(username)
    file1.write(" ")
    file1.write(password)
    file1.write(" ")
    file1.write(name)
    file1.write("\n")
    file1.close()

##############################################

############## SUDDEN DEATH ##################

def suddenDeath():
    global dmin, dmax, SDP1, SDP2
    tempdice1 = 0
    temproll2 = 0
    print("This is sudden death. Whoever gets a higher roll will win the game.")
    print("Player 1:")
    tempdice1 = random.randint(dmin, dmax)
    SDP1 += tempdice1
    sleep(0.35)
    print("First Dice: ",tempdice1)
    temproll2 = random.randint(dmin, dmax)
    SDP1 += temproll2
    sleep(0.65)
    print("Second Dice:",temproll2)
    print("" * 1)
    print("Player 1 has",SDP1,"points.")
    print("" * 3)
    print("Player 2:")
    tempdice1 = random.randint(dmin, dmax)
    SDP2 += tempdice1
    sleep(0.35)
    print("First Dice: ",tempdice1)
    temproll2 = random.randint(dmin, dmax)
    SDP2 += temproll2
    sleep(0.65)
    print("Second Dice:",temproll2)
    print("" * 1)
    print("Player 2 has",SDP2,"points.")
    if SDP1 < SDP2:
        print("Player 2 has won with",SDP2,"points!")
        os.system("pause")
    else:
        print("Player 1 has won with",SDP1,"points!")
        os.system("pause")

##############################################


############# DICE GAME CODE #################

def diceGame():
    global dmin, dmax, P1Score, P2Score
    diceRolls = 1
    tempdice1 = 0
    temproll2 = 0
    while diceRolls <= 5:
        print("Player 1:")
        tempdice1 = random.randint(dmin, dmax)
        P1Score += tempdice1
        sleep(0.35)
        print("First Dice: ",tempdice1)
        temproll2 = random.randint(dmin, dmax)
        P1Score += temproll2
        sleep(0.65)
        print("Second Dice:",temproll2)
        print("" * 1)
        print("Player 1 Score after round",diceRolls,"is:", P1Score)
        print("" * 2)

        tempdice1 = 0
        temproll2 = 0
        sleep(1.5)
        print("Player 2:")
        tempdice1 = random.randint(dmin, dmax)
        P2Score += tempdice1
        sleep(0.35)
        print("First Dice: ",tempdice1)
        temproll2 = random.randint(dmin, dmax)
        P2Score += temproll2
        sleep(0.65)
        print("Second Dice:",temproll2)
        print("" * 1)
        print("Player 2 Score after round",diceRolls,"is:", P2Score)
        print("" * 2)
        sleep(1.5)
        diceRolls += 1        

##############################################

################ Login P1 ####################
        
def login():
    global P1Username, P1Pass, P1Login, P1Name
    P1Username = input("Player 1, Please enter your username ")
    P1Pass = input("Player 1, Please enter your password ")
    P1Name = input("As an extra layer of security, please enter your name: ")
    for line in open("accountfile.txt","r").readlines(): # Read the lines
        login_info = line.split() # Split on the space, and store the results in a list of two strings
        if P1Username == login_info[0] and P1Pass == login_info[1] and P1Name == login_info[2]:
            print("Correct credentials!")
            print("" * 3)
            print("Hello,",P1Name)
            P1Login = True
            return True
    print("Incorrect credentials.")
    return False

###############################################

################## Login P2 ###################

def login2():
    global P2Username
    global P2Pass
    global P2Name
    global P2Login
    P2Username = input("Player 2, Please enter your username: ")
    P2Pass = input("Player 2, Please enter your password: ")
    P2Name = input("As an extra layer of security, please enter your name: ")
    for line in open("accountfile.txt","r").readlines(): # Read the lines
        login_info = line.split() # Split on the space, and store the results in a list of two strings
        if P2Username == login_info[0] and P2Pass == login_info[1] and P2Name == login_info[2]:
            if P2Username == P1Username:
                print("Player 1 is already logged in!")
                return False
            print("Correct credentials!")
            P2Login = True
            printer(3)
            print("Hello,",P2Name)
            return True
    print("Incorrect credentials.")
    return False

#################################################

regCheck = input("Do you need to register an account? (Please enter either Y/N)")
if regCheck == "Y" or regCheck == "y":
    register()

login()
if P1Login == False:
    print("Login Failed.")
else:
    login2()
if P2Login == False:
    print("Login Failed.")
else:
    printer(10)
    diceGame()
    
if P1Score == P2Score:
    print("---- SUDDEN DEATH ----")
    suddenDeath()
else:
    if P1Score < P2Score:
        print(P2Name,"has won with a score of",P2Score)
        os.system("pause")
    else:
        print(P1Name,"has won with a score of",P1Score)
        os.system("pause")

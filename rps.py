import time
import random
print("-------------------------")
print("Made by Manivyas")
print("-------------------------")
loose = "Computer wins"
win = "You win"
lives = 5
score = 0
draw = 0
computer_lives = 7
random.seed(0)
while True:
    print("To begin Please fill the below information")
    username = input("username:  ")
    password = input("password:  ")
    search_file = open("accounts.txt", "r")
    for line in search_file:
        if username and password in search_file:
            print("loading.")
            time.sleep(0.5)
            print("loading.")
            time.sleep(0.5)
            print("Access granted")
            print("------------------------------")
            print("Live Rules")
            print("-------------------------")
            print("You start with 5 lives")
            print("-------------------------")
            print("if you win you get extra life")
            print("if you draw lives remain same")
            print("if you loose you loose a life")
            print("-------------------------------")
            print("to see list of rules type rules")
            print("-------------------------------")
            print("At any point of time type exit to leave")
            print("-------------------------------")
            print("computer has 7 lives")
            print("Good Luck!")
            print("-------------------------------")
            while True:
                rps = input("Rock,Paper,Scissor?  ")
                rps = rps.title()

                computer = ("Rock", "Paper", "Scissor")
                computer = random.choice(computer)
                # rock
                if rps == "Rock" and computer == "Paper":
                    print("the computer choose: ", computer)
                    print("")
                    print(loose)
                    print("")
                    lives -= 1
                if rps == "Rock" and computer == "Scissor":
                    print("the computer choose: ", computer)
                    print("")
                    print(win)
                    print("")
                    score += 1
                # paper
                if rps == "Paper" and computer == "Rock":
                    print("the computer choose: ", computer)
                    print("")
                    print(win)
                    computer_lives -= 1
                    print("")
                    score += 1
                if rps == "Paper" and computer == "Scissor":
                    print("the computer choose: ", computer)
                    print("")
                    print(loose)
                    print("")
                    lives -= 1
                # scissor
                if rps == "Scissor" and computer == "Rock":
                    print("the computer choose: ", computer)
                    print("")
                    print(loose)
                    print("")
                    lives -= 1
                if rps == "Scissor" and computer == "Paper":
                    print("the computer choose: ", computer)
                    print("")
                    print(win)
                    computer_lives -= 1
                    print("")
                    score += 1
                # duplicates
                if rps == "Rock" and computer == "Rock":
                    print("the computer choose: ", computer)
                    print("")
                    print("DRAW")
                    print("")
                    draw += 1
                if rps == "Paper" and computer == "Paper":
                    print("the computer choose: ", computer)
                    print("")
                    print("DRAW")
                    print("")
                    draw += 1
                if rps == "Scissor" and computer == "Scissor":
                    print("the computer choose: ", computer)
                    print("")
                    print("DRAW")
                    print("")
                    draw += 1
                # system
                if rps == "Rules":
                    print("------------------------------------")
                    print("Rules")
                    print("------------------------------------")
                    print("Rock looses against Paper")
                    print("Rock beats Scissor")
                    print("Paper looses against Scissor")
                    print("Paper beats Rocks")
                    print("Scissor looses against Rock")
                    print("Scissor beats paper")
                    print("------------------------------------")
                if rps == "lives".title():
                    print(lives)
                if rps == "score".title():
                    print(score)
                if rps == "draw".title():
                    print(draw)
                # lives
                if lives == 0 or rps == "Test":
                    print("Thanks for playing")
                    print("you have run out of lives")
                    print("You got: ", score, "correct")
                    print("You drew", draw, " times")
                    stop = input("Press enter to exit.")
                    exit()
                if computer_lives == 0:
                    print("Thanks for playing")
                    print("The computer got run out of lives, YOU WON")
                    print("You got: ", score, "correct")
                    print("You drew", draw, "times")
                    stop = input("Press enter to exit.")
                    exit()
                # exit
                if rps == "Exit":
                    exit()
        else:
            print("The username or password is wrong")
            break
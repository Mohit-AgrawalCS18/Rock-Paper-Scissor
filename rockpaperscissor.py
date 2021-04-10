#ROCK-PAPER-SCISSOR GAME PROJECT
import random
import time


def rockpaperScissor(userInput, AIinput):
    userScore = 0
    AIinputScore = 0
    if userInput == AIinput:
        time.sleep(1)
        print(f"Computer_Input: {AIinput}")
        time.sleep(1)
        print("match Draw !!!")
    elif(userInput == "rock"):
        if AIinput == "scissor":
            time.sleep(1)
            print(f"Computer_Input: {AIinput}")
            time.sleep(1)
            print("you win !!!")
            userScore = userScore+1
            print(
                f"your Score: {userScore} and Computer Score: {AIinputScore}")
        else:
            time.sleep(1)
            print(f"Computer_Input: {AIinput}")
            time.sleep(1)
            print("you loss !!!")
            AIinputScore = AIinputScore+1
            print(
                f"your Score: {userScore} and Computer Score: {AIinputScore}")
    elif(userInput == "paper"):
        if AIinput == "rock":
            time.sleep(1)
            print(f"Computer_Input: {AIinput}")
            time.sleep(1)
            print("you win !!!")
            userScore = userScore+1
            print(
                f"your Score: {userScore} and Computer Score: {AIinputScore}")

        else:
            time.sleep(1)
            print(f"Computer_Input: {AIinput}")
            time.sleep(1)
            print("you loss !!!")
            AIinputScore = AIinputScore+1
            print(
                f"your Score: {userScore} and Computer Score: {AIinputScore}")
    elif(userInput == "scissor"):
        if AIinput == "paper":
            time.sleep(1)
            print(f"Computer_Input: {AIinput}")
            time.sleep(1)
            print("you win !!!")
            userScore = userScore+1
            print(
                f"your Score: {userScore} and Computer Score: {AIinputScore}")

        else:
            time.sleep(1)
            print(f"Computer_Input: {AIinput}")
            time.sleep(1)
            print("you loss !!!")
            AIinputScore = AIinputScore+1
            print(
                f"your Score: {userScore} and Computer Score: {AIinputScore}")


if __name__ == '__main__':
    userInput = input("choose any one of them \n1.rock 2.paper 3.scissor: ")
    List = ["rock", "paper", "scissor"]
    AIinput = random.choice(List)
    rockpaperScissor(userInput, AIinput)

""" 
Kashyap Sukshavasi
Jan 16, 2024
Adventure Game Part 2: Riddles of Destiny
Courtney Edwards
"""

#Imports
import random

#Constants
SHIFT = 3

def caesarCipher(text):
    """
    Encrypts or decrypts a text using the Caesar cipher method.

    Parameters:
    text (str): The text to be encrypted or decrypted.
    shift (int): The number of positions to shift each letter.

    Returns:
    str: The transformed text.
    """
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper:
                asciiOffset = ord('A')
            else:
                asciiOffset = ord('a')
            result += chr((ord(char) - asciiOffset + SHIFT) % 26 + asciiOffset)
        else:
            result += char
        
    return result

def startGame(stage):
    """
    Displays the current stage of the game and provides instructions.

    Parameters:
    stage (str): The current stage of the game.
    """
    if stage == "rookieLand":
        print("You find yourself in Rookie Land - The Caesar Cipher Challenge!")
        print("Decrypt the message to proceed.\n")
    elif stage == "choosePath":
        print("You find yourself at the crossroads. Choose your next path:\n")
        print("1. Fortune Teller's Tent - Number Guessing Game")
        print("2. Scholar's Library - Math Challenge")
    elif stage == "mysteryTower":
        print("\nYou've entered the Mystery Tower - The Wordle Challenge!")
    elif stage == "trainingGround":
        print("\nWelcome to the Training Grounds - Rock Paper Scissors Arena!")
    elif stage == "finalLand":
        print("\nCongratulations! You have reached the Final Land!")
        
def rookieLand():
    """
    Handles the Rookie Land stage where the player decrypts a Caesar cipher message.

    Returns:
    str: The next stage after completing the challenge.
    """
    with open("ceasarCipherText.txt", "r") as file:
        words = file.read().splitlines()

    originalText = random.choice(words)
    encryptedText = caesarCipher(originalText)
    print(f"Decrypt this message: {encryptedText}")
    print("Hint: It's a Caesar cipher with shift of 3")
    
    while True:
        answer = input("Your answer: ").upper()
        if answer == originalText.upper():
            print("\nCorrect! You've earned the letter 'H'!")
            return "choosePath"
        else:
            print("Try again!")
            
def fortuneTellersTent():
    """
    Handles the Fortune Teller's Tent stage where the player guesses a number.

    Returns:
    str: The next stage after completing the challenge.
    """
    targetNumber = random.randint(1, 10)
    attempts = 3
    
    print("\nGuess a number between 1 and 10. You have 3 attempts!")
    
    while attempts > 0:
        try:
            guess = int(input(f"Attempts left {attempts}. Your guess: "))
            if guess == targetNumber:
                print("\nCorrect! You've earned the letter 'E'!")
                return "mysteryTower"
            elif guess < targetNumber:
                print("Too low!")
            else:
                print("Too high!")
            attempts -= 1
        except ValueError:
            print("Please enter a valid number!")
            
    print(f"\nOut of attempts! The number was {targetNumber}.")
    return "choosePath"

def scholarsLibrary():
    """
    Handles the Scholar's Library stage where the player solves a math problem.

    Returns:
    str: The next stage after completing the challenge.
    """
    num1 = random.randint(10, 20)
    num2 = random.randint(5, 10)
    
    print(f"\nSolve this math problem:")
    print(f"If you have {num1} books and give away {num2}, how many remain?")
    
    while True:
        try:
            answer = int(input("Your answer: "))
            if answer == (num1 - num2):
                print("\nCorrect! You've earned the letter 'A'!")
                return "trainingGround"
            else:
                print("Try again!")
        except ValueError:
            print("Please enter a valid number!")
            
def mysteryTower():
    """
    Handles the Mystery Tower stage where the player plays a Wordle-like game.

    Returns:
    str: The next stage after completing the challenge.
    """
    with open("words.txt", "r") as file:
        words = [word.strip().upper() for word in file if len(word.strip()) == 5]

    targetWord = random.choice(words)
    attempts = 6
    
    print("\nGuess the 5-letter word. After each guess, you'll see the following feedback:")
    print(f"\033[32mGreen\033[0m for correct letter in the correct position.")
    print(f"\033[33mYellow\033[0m for correct letter in the wrong position.")
    print(f"\033[31mRed\033[0m for incorrect letters.\n")
    
    while attempts > 0:
        guess = input(f"\nAttempts left {attempts}. Your guess: ").upper()
        if len(guess) != 5:
            print("Please enter a 5-letter word!")
            continue
            
        if guess == targetWord:
            print("\nCorrect! You've earned the letter 'R'!")
            return "trainingGround"
        
        feedback = []
        targetLetters = list(targetWord)
        guessLetters = list(guess)
        
        for i in range(5):
            if guessLetters[i] == targetLetters[i]:
                feedback.append(f"\033[32m{guessLetters[i]}\033[0m")
                targetLetters[i] = None
            else:
                feedback.append(None)
        
        for i in range(5):
            if feedback[i] is not None:
                continue
            if guessLetters[i] in targetLetters:
                feedback[i] = f"\033[33m{guessLetters[i]}\033[0m"
                targetLetters[targetLetters.index(guessLetters[i])] = None 
            else:
                feedback[i] = f"\033[31m{guessLetters[i]}\033[0m"
        
        print("Feedback: " + ''.join(feedback))
        attempts -= 1
    
    print(f"\nOut of attempts! The word was {targetWord}")
    return "mysteryTower"

def trainingGround():
    """
    Handles the Training Grounds stage where the player plays Rock Paper Scissors.

    Returns:
    str: The next stage after completing the challenge.
    """
    options = ["rock", "paper", "scissors"]
    winsNeeded = 2
    wins = 0
    
    print("\nWin 2 rounds of Rock Paper Scissors to proceed!")
    
    while wins < winsNeeded:
        computerChoice = random.choice(options)
        playerChoice = input("\nEnter rock, paper, or scissors: ").lower()
        
        if playerChoice not in options:
            print("Invalid choice!")
            continue
            
        print(f"Computer chose: {computerChoice}")
        
        if playerChoice == computerChoice:
            print("It's a tie!")
        elif (
            (playerChoice == "rock" and computerChoice == "scissors") or
            (playerChoice == "paper" and computerChoice == "rock") or
            (playerChoice == "scissors" and computerChoice == "paper")
        ):
            print("You win this round!")
            wins += 1
        else:
            print("Computer wins this round!")
            
        print(f"Wins: {wins}/{winsNeeded}")
    
    print("\nCongratulations! You've earned the letter 'T'!")
    return "finalLand"

def main():
    """
    The main function that controls the flow of the game.
    """
    stage = "rookieLand"
    letters = []
    completedPaths = {
        "fortunePath": False,  
        "scholarPath": False   
    }
    
    while True:
        startGame(stage)
        
        if stage == "rookieLand":
            if "H" not in letters:
                letters.append("H")
            stage = rookieLand()
            
        elif stage == "choosePath":
            if not completedPaths["fortunePath"] and not completedPaths["scholarPath"]:
                choice = input("Enter your choice (1 or 2): ").strip()
                if choice == "1":
                    if "E" not in letters:
                        letters.append("E")
                    stage = fortuneTellersTent()
                elif choice == "2":
                    if "A" not in letters:
                        letters.append("A")
                    stage = scholarsLibrary()
                else:
                    print("\nInvalid choice!")
            else:
                if not completedPaths["fortunePath"]:
                    print("\nProceeding to Fortune Teller's Tent...")
                    if "E" not in letters:
                        letters.append("E")
                    stage = fortuneTellersTent()
                else:
                    print("\nProceeding to Scholar's Library...")
                    if "A" not in letters:
                        letters.append("A")
                    stage = scholarsLibrary()
                
        elif stage == "mysteryTower":
            if "R" not in letters:
                letters.append("R")
            stage = mysteryTower()
            if stage == "trainingGround":
                completedPaths["fortunePath"] = True
            
        elif stage == "trainingGround":
            if not completedPaths["fortunePath"] and "R" in letters:
                completedPaths["fortunePath"] = True
            elif not completedPaths["scholarPath"] and "A" in letters:
                completedPaths["scholarPath"] = True
                
            if "T" not in letters:
                result = trainingGround()
                if result == "finalLand":
                    letters.append("T")
            
            if completedPaths["fortunePath"] and completedPaths["scholarPath"]:
                print("\nYou've completed both paths! Now you can proceed to the Final Land.")
                stage = "finalLand"
            else:
                print("\nYou haven't completed all paths yet!")
                if not completedPaths["fortunePath"]:
                    print("\nRedirecting you to Fortune Teller's Tent to complete that path...")
                    stage = fortuneTellersTent()
                elif not completedPaths["scholarPath"]:
                    print("\nRedirecting you to Scholar's Library to complete that path...")
                    stage = scholarsLibrary()
                
        elif stage == "finalLand":
            print("\nCongratulations! You've collected all letters:", ' '.join(letters))
            print("Can you unscramble them to find the hidden word?")
            while True:
                answer = input("Enter the word: ").upper()
                if answer == "HEART":
                    print("\nCORRECT! You've completed your journey through the Riddles of Destiny!")
                    return
                else:
                    print("Try again! Rearrange the letters:", ' '.join(letters))
            
if __name__ == "__main__":
    print("\n" + "="*50)
    print("Welcome to the Riddles of Destiny!")
    print("="*50 + "\n")
    main()
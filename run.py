# Developer: Nuala King
# Date of release: 15th April 2022
# Subject: Code Institute Portfolio Project 3 - Python
# Program Name: "Archiquiz"

def clear_terminal():
    # Clears terminal.
    """
    Clears terminal
    """
    os.system('clear')

def game_over():
    # Prints "Game Over" text and exits game.
    """
    Prints "Game Over" text and exits game.
    """
    print("\nThank you for playing!")
    print("""\u001b[32m           
 _____                        _____ 
|  __ \                      |  _  |               
| |  \/ __ _ _ __ ___   ___  | | | |_   _____ _ __ 
| | __ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|
| |_\ \ (_| | | | | | |  __/ \ \_/ /\ V /  __/ |   
| |_\ \ (_| | | | | | |  __/ \ \_/ /\ V /  __/ |
 \____/\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|
\u001b[0m""")
    
    time.sleep(3)
    print("Click the blue button at the top to replay the game!")
    print()
    sys.exit()

# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M
dt_string = now.strftime("%d/%m/%Y %H:%M")


def run_instructions():
    """
    Prints the instructions for the game
    """
    print("this game will test your knowledge and")
    print("questions are based around Architectural History.")
    print()
    print('''\u001b[32m===========================================\u001b[0m''')
    print("1. All you need to do is press a, b or c for your answer.")
    print("2. The program will tell you if you are correct or incorrect.")
    print("3. The program will add up your scores.")
    print("4. The program tells you your score at the end.")
    print("5. The game is also timed.")
    print("6. You will be able to save your score to the leaderboard.")
    print('''\u001b[32m===========================================\u001b[0m''')
    print()

print('''\u001b[32m
__________________ $$
__________________ $$
_________________ $$$$
_________________ $$$$
__________________ $$
__________________ $$
__________________ $$
__________________ $$
__________________ $$
__________________ $$
_________________ $$$$
_________________ $$$$
_________________ $$$$
_________________ $$$$
_________________ $$$$
_________________ $$$$
_________________ $$$$
_________________ $$$$
_________________ $$$$
_________________ $$$$
_________________ $$$$
________________ $$$$$$
________________ $$$$$$
________________ $$$$$$
________________ $$$$$$
________________ $$$$$$
_______________ $$$$$$$$
_______________ $$$$$$$$
_______________ $$$$$$$$
_______________ $$$$$$$$
______________ $$$$$$$$$$
______________ $$$$$$$$$$
____________ $$$$$$$$$$$$$$
____________ $$$$$$$$$$$$$$
_____________ $$$$$$$$$$$$
_____________ $$$$$$$$$$$$
____________ $$$$$$$$$$$$$$
____________ $$$$$_____$$$$
___________ $$$$$______$$$$$
___________ $$$$$_______$$$$
__________ $$$$$$_______$$$$$
_________ $$$$$$________$$$$$
______ $$$$$$$$$_$_$_$_$_$$$$$$$
______ $$$$$$$$$$$$$$$$$$$$$$$$$
______ $$$$$$$$$$$$$$$$$$$$$$$$$
______ $$$$$$$$$$$$$$$$$$$$$$$$$
______ $$$$$$$$$$$$$$$$$$$$$$$$$$
_____ $$$$$$$$$$$$$$$$$$$$$$$$$$​$$
____$$$$$$$$$$ __________$$$$$$$$$$
___$$$$$$$$ ________________$$$$$$$$
__$$$$$$$$ __________________$$$$$$$$
_$$$$$$$$ ____________________$$$$$$​$$
$$$$$$$$_______________________$$$$​$$$$
\u001b[0m''')

print("Welcome to Archiquiz!...\n")
print('''\u001b[32m===============================================\u001b[0m''')
name = input("Please enter your name:\n")
time.sleep(1)
clear_terminal()
print('''\u001b[32m===============================================\u001b[0m''')
if any(c.isalpha() for c in name):
    print("Thank you for stopping by, " + name)
else:
    print("Thank you for stopping by, Guest")
print('''\u001b[32m===============================================\u001b[0m''')

class Question:
    """
    Questions instance, gets the question
    and the answer
    """
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
     "Which of these is amongst the most iconic and definitive elements of the Gothic Revival style??\n \
    (a)\
     (b)\
     (c)",
]

def run_quiz(questions):
     score = 0
     random.shuffle(questions)
     for question in questions:
          answer = input(question.prompt).lower()
          if answer == question.answer:
               score += 1
               time.sleep(1)
               print("Well done, you are correct!")
          else:
               time.sleep(1)
               print("Sorry, you are incorrect!")

     print("You got", score, "out of", len(questions))
     time.sleep(3)
    tic = time.perf_counter()
    score = 0
    random.shuffle(questions)
    for question in questions:
        answer = input(question.prompt).lower()
        if answer not in {'a', 'b', 'c', 'd'}:
            print('INVALID INPUT!!! Use \'a,\' \'b,\' or \'c\' for your response')
        elif answer == question.answer:
            score += 1
            time.sleep(1)
            print("Well done, you are correct!")
        else:
            time.sleep(1)
            print("Sorry, you are incorrect!\n")

    toc = time.perf_counter()
    print("You got", score, "out of", len(questions))
    time.sleep(1)
    print(f"You completed the quiz in {toc - tic:0.4f} seconds")
    time.sleep(2)
    else:
        time.sleep(1)
        print("Ok, thank you for playing, " + name)
        time.sleep(1)
        print("Exiting the game...")
        game_over()

def start_game():
    """
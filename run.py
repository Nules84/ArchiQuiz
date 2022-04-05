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
    print("""
 _____                        _____               
 _____                        _____ 
|  __ \                      |  _  |               
| |  \/ __ _ _ __ ___   ___  | | | |_   _____ _ __ 
| | __ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|
| |_\ \ (_| | | | | | |  __/ \ \_/ /\ V /  __/ |   
| |_\ \ (_| | | | | | |  __/ \ \_/ /\ V /  __/ |
 \____/\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|
""")
    
    time.sleep(3)
    sys.exit()

# datetime object containing current date and time
now = datetime.now()
print(now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

score = 0

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

print("Hello!  Welcome to ArchiQuiz!...\n")

print("===================================================")

class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
     "Which of these is amongst the most iconic and definitive elements of the Gothic Revival style??\n \
@@ -166,20 +207,38 @@ def __init__(self, prompt, answer):
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
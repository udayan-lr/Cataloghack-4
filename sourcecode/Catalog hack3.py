import random

def level_one(attempts=3):
    print("Level 1: Textual Password")
    password = "mypassword123"
    for attempt in range(attempts):
        user_input = input("Enter the Level 1 password: ")
        if user_input == password:
            print("Level 1 Passed!\n")
            return True
        else:
            print(f"Incorrect Level 1 password. Attempts left: {attempts - attempt - 1}\n")
    print("Access Denied. Too many failed attempts at Level 1.\n")
    return False

def level_two(attempts=3):
    print("Level 2: PIN Code")
    pin_code = "7890"
    for attempt in range(attempts):
        user_input = input("Enter the Level 2 PIN code: ")
        if user_input == pin_code:
            print("Level 2 Passed!\n")
            return True
        else:
            print(f"Incorrect Level 2 PIN code. Attempts left: {attempts - attempt - 1}\n")
    print("Access Denied. Too many failed attempts at Level 2.\n")
    return False

def level_three(attempts=3):
    print("Level 3: Secret Question")
    questions = [
        {"question": "What is your favorite color?", "answer": "blue"},
        {"question": "What is your pet's name?", "answer": "buddy"},
        {"question": "What is your mother's maiden name?", "answer": "smith"},
    ]
    selected_question = random.choice(questions)

    for attempt in range(attempts):
        user_input = input(f"{selected_question['question']} ")
        if user_input.lower() == selected_question['answer']:
            print("Level 3 Passed!\n")
            return True
        else:
            print(f"Incorrect answer. Attempts left: {attempts - attempt - 1}\n")
    print("Access Denied. Too many failed attempts at Level 3.\n")
    return False

def three_level_password_system():
    print("Welcome to the Enhanced Three-Level Password System\n")
    
    if level_one():
        if level_two():
            if level_three():
                print("Access Granted! You have passed all levels.\n")
            else:
                print("Access Denied at Level 3.")
        else:
            print("Access Denied at Level 2.")
    else:
        print("Access Denied at Level 1.")

three_level_password_system()

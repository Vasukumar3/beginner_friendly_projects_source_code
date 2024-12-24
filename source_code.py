# Number Guessing Game
"""
Title: Number Guessing Game
Description: This game generates a random number between 1 and 100. The player has a maximum of 3 attempts to guess the number correctly. 
After each incorrect guess, the program provides feedback whether the guess is too low or too high. If the player uses all attempts without guessing correctly, the correct number is revealed.
"""
import random

def number_guessing_game():
    """
    Function: number_guessing_game
    Description: Implements the number guessing game logic. The function selects a random number and allows the user to guess it within a limited number of attempts.
    """
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 3

    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100.")

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {number}.")

number_guessing_game()

# Simple Calculator
"""
Title: Simple Calculator
Description: A calculator program that performs basic arithmetic operations: addition, subtraction, multiplication, and division. The user inputs two numbers and an operator, and the result of the operation is displayed. The program continues until the user decides to exit.
"""
def calculator():
    """
    Function: calculator
    Description: Implements a simple calculator with support for basic arithmetic operations.
    """
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    while True:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter the operator: ")
        num2 = float(input("Enter the second number: "))

        if operator == '+':
            print(f"Result: {num1 + num2}")
        elif operator == '-':
            print(f"Result: {num1 - num2}")
        elif operator == '*':
            print(f"Result: {num1 * num2}")
        elif operator == '/':
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Cannot divide by zero.")
        else:
            print("Invalid operator.")

        if input("Do you want to calculate again? (yes/no): ").lower() != 'yes':
            break

calculator()

# To-Do List
"""
Title: To-Do List
Description: A program that allows users to manage their tasks. Users can add new tasks, view existing ones, and remove completed tasks. The program continues running until the user chooses to exit.
"""
def to_do_list():
    """
    Function: to_do_list
    Description: Provides a simple menu to add, view, and delete tasks from a list.
    """
    tasks = []

    while True:
        print("\nTo-Do List Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            tasks.append(task)
            print("Task added.")
        elif choice == '2':
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        elif choice == '3':
            task_no = int(input("Enter the task number to remove: "))
            if 1 <= task_no <= len(tasks):
                removed = tasks.pop(task_no - 1)
                print(f"Removed task: {removed}")
            else:
                print("Invalid task number.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

to_do_list()

# Simple Quiz App
"""
Title: Simple Quiz App
Description: A quiz application with predefined questions. Users can answer the questions, and the app provides feedback and calculates the final score.
"""
def quiz_app():
    """
    Function: quiz_app
    Description: Runs a quiz with multiple-choice questions and tracks the user's score.
    """
    questions = {
        "What is the capital of France?": "Paris",
        "What is 2 + 2?": "4",
        "Who wrote 'Hamlet'?": "Shakespeare",
        "What is the square root of 16?": "4",
    }

    score = 0

    print("Welcome to the Quiz App!")
    for question, answer in questions.items():
        user_answer = input(question + " ")
        if user_answer.strip().lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {answer}.")

    print(f"\nYou scored {score}/{len(questions)}.")

quiz_app()

# ATM Simulation
"""
Title: ATM Simulation
Description: A program that simulates basic ATM functionalities such as checking balance, depositing money, and withdrawing money. The user can perform multiple transactions until they choose to exit.
"""
def atm_simulation():
    """
    Function: atm_simulation
    Description: Simulates an ATM with options for balance inquiry, deposit, and withdrawal.
    """
    balance = 1000

    print("Welcome to the ATM!")

    while True:
        print("\nATM Menu")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print(f"Your balance is: {balance}")
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: "))
            if amount > 0:
                balance += amount
                print(f"Deposited {amount}. New balance is {balance}.")
            else:
                print("Invalid amount.")
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: "))
            if 0 < amount <= balance:
                balance -= amount
                print(f"Withdrew {amount}. Remaining balance is {balance}.")
            else:
                print("Invalid amount or insufficient balance.")
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice.")

atm_simulation()

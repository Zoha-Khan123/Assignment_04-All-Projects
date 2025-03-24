# ===================== 00_joke_bot =====================
JOKE = "Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
PROMPT = "What do you want? " 
SORRY = "Sorry I only tell jokes."

def joke_bot():
    user_input = input(PROMPT).strip().lower()
    print(user_input)

    if "joke" in user_input:
        print(JOKE)
    else:
        print(SORRY)

# joke_bot()



# ===================== 01_double_it =====================
def double_it():
    user_input = int(input("Enter a number "))

    while user_input < 100:
        print(f"{user_input} double is {user_input * 2}")
        user_input *= 2

# double_it()



# ===================== 02_liftoff ======================
import time
def liftoff():
    for i in range(1,11):
        time.sleep(i)
        print(i)

# liftoff()



# ===================== 03_guess_my_number ======================
import random
def guess_my_number():
    print("Guess My Number")
    print("I am thinking of a number between 1 and 100 ")
    random_number = random.randint(1,101)

    
    while True:
        user_guess = input("Enter a guess. (Press Enter to stop) ")
        
        if user_guess == "":
            print("Good Bye ")
            break
        
        try:
            user_guess = int(user_guess)
            if user_guess < 0 or user_guess > 100:
                print("Please enter a number between 1 to 100")
            if user_guess < random_number:
                print("Your guess is too low")
            elif user_guess > random_number:
                print("Your guess is too high")
            elif user_guess == random_number:
                print(f"Congrats! The number was: {random_number}")
                break
        except ValueError:
            print("Please enter a valid number")

# guess_my_number()



# ===================== 04_random_numbers ======================
def random_numbers():
   for i in range(10):
    ten_random_numbers = random.randint(1,100)
    print(ten_random_numbers)

# random_numbers()
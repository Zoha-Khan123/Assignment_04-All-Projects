import random

# ============================  Question NO 00 ================================
def guess_number():
  print("Question No 00 \nGuess my number\n")
  secret_number = random.randint(1,100)
  print("I am thinking of a number between 0 and 99...")


  while True:
      try:
        user_guess = int(input("What is your guess? "))
        if user_guess < secret_number:
          print("Your guess is too low.")
        elif user_guess > secret_number:
          print("Your guess is too high.")
        else:
          print(f"Congrats! You Find Your Number.The Number Is {secret_number}")
          break
      except ValueError:
        print("Invalid input. Please enter a valid number.")


# guess_number()



# ============================  Question NO 01 ================================
def fibonacci(n):
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_range():
    print("Question No 01 \nFibonacci\n")
    for i in range(10):
        print(fibonacci(i))

# fibonacci_range()


# ============================  Question NO 02 ================================
def first_twenty_even_numbers():
  print("Question No 02 \nPrint Events\n")
  for i in range(0,40):
    if i % 2 == 0:
      print(i)

# first_twenty_even_numbers()



# ============================  Question NO 03 ================================
def wholesome_machine():
    print("Question No 03 \nWholesome Machine\n")
    AFFIRMATION = "I am capable of doing anything I put my mind to."
    while True:
        user_input = input("Please type the following affirmation: I am capable of doing anything I put my mind to.\n")
        if user_input == AFFIRMATION:
            print("That's right! :)")
            break
        else:
            print("That was not the affirmation.")

# wholesome_machine()



# ============================  Question NO 04 ================================
import time

def liftoff():
  print("Question No 04 \nLift Off\n")
  i = 0
  while i <= 10:
    time.sleep(1)
    print(i)
    i += 1

# liftoff()



# ============================  Question NO 05 ================================
def double_it():
  print("Question No 05 \nDouble It\n")

  total = 0

  while True:
    try:
      user_number = int(input("Enter a number. When the number is greater than 100 loop will be break "))
      double = user_number * 2
      total += double
      print(f"{user_number} doubles is {double}")

      if total > 100:
        print(f"We stop at {total} because that value is greater than 100. ")
        break

    except:
      print("Invalid Input")

# double_it()



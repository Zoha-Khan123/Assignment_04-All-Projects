
# ============================  Question NO 01 ================================
def print_events():
  print("Question No 01 \nPrint Events")

  user_input = int(input("How many numbers you want to find even numbers "))
  i = 0
  store_even_numbers = []
  while i < user_input:
    i += 1

    if (i % 2 == 0):
      store_even_numbers.append(i)
  print(store_even_numbers)

# print_events()




# ============================  Question NO 02 ================================
def international_voting_age():
  print("Question No 02 \nInternational Voting Age")

  PETURKSBOUIPO_AGE = 16
  STANLAU_AGE  = 25
  MAYENGUA_AGE = 48

  age = int(input("How old are you ? "))

  if age >= MAYENGUA_AGE:
      print(f"You can vote in MAYENGUA where the voting age is {MAYENGUA_AGE}")
  elif age >= STANLAU_AGE:
      print(f"You can vote in STANLAU where the voting age is {STANLAU_AGE}")
  elif age >= PETURKSBOUIPO_AGE:
      print(f"You can vote in PETURKSBOUIPO where the voting age is {PETURKSBOUIPO_AGE}")
  else:
      print("You cannot vote anywhere.")

# international_voting_age()



# ============================  Question NO 03 ================================
def leap_year():
    print("Question No 03 \nLeap Year")
    year = int(input("Please input a year "))

    if year % 4 == 0:
      if year % 100 == 0:
        if year % 400 == 0:
          print("That is a leap year")
        else:
          print("That is not a leap year")
      else:
        print("That is a leap year")
    else:
      print("That is not a leap year")

# leap_year()



# ============================  Question NO 04 ================================
def tall_enough_to_ride():
  print("Question No 04 \nTall Enough To Ride")
  minimum_height = 50

  while True:
    user_input = input("How tall are you ? (Press Enter to stop) ")
    if user_input == "":
      print("Good Bye ")
      break

    try:
      user_height = int(user_input)
      if user_height >= minimum_height:
        print("You're tall enough to ride! ")
      else:
        print("You're not tall enough to ride, but maybe next year! ")
    except ValueError:
      print("Please enter a valid number ")


# tall_enough_to_ride()



# ============================  Question NO 05 ================================
import random
def random_number():
  print("Question No 05 \nRandom Numbers")
  store_random_numbers = []
  i = 1
  while i <= 10:
    random_numbers = random.randint(1, 101)
    store_random_numbers.append(random_numbers)
    i += 1
  print(f"Print 10 Random Numbers: \n{store_random_numbers}")

# random_number()



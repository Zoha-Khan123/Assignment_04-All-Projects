# ============================  Question NO 01 ================================
import random
import math

gobal_variable = 20  # Access everywhere

def roll_dice():
 dice1 = math.floor(random.randint(1,6))
 dice2 = math.floor(random.randint(1,6))
 total = dice1 + dice2
 print(total)

#  Extra work for checking local variable vs global variable
 local_variable = 50 # Access only inside the function
 print(f"Inside the roll_dice function {gobal_variable}")
 print(f"Only access in inside the function {local_variable}")

def dice():
  roll_dice()
  roll_dice()
  roll_dice()

  #  Extra work for checking local variable vs global variable
  print(f"Inside the main function {gobal_variable}")
  # print(f"Not access in another function {local_variable}")  This will give error

# dice()



# ============================  Question NO 02 ================================
def calculate_mass():
    
  mass = int(input("Enter the mass in kilogram "))
  C = 299792458

  # Formula of Energy
  E = mass * C**2
  print(f"{E:.2e} joules of energy!")

# calculate_mass()



# ============================  Question NO 03 ================================
def feet_to_inches():

    feet = float(input("Enter feet into inches "))
    one_foot = 12

    # Formula of Feet
    feet_into_inches = one_foot * feet
    print(f"{feet_into_inches}")


# feet_to_inches()



# ============================  Question NO 04 ================================
def pythagorean_theorem():
    AB = float(input("Enter the length of AB "))
    AC = float(input("Enter the length of AC "))

    # Formula of Pythagoras theorem
    BC = math.sqrt(AB**2 + AC**2)
    print(f"The length of BC (the hypotenuse) is: {BC:.2f}")



# pythagorean_theorem()



# ============================  Question NO 05 ================================
def reaminder_division():
  num1 = int(input("Please enter an integer to be divided:"))
  num2 = int(input("Please enter a second integer to be divided:"))

  # Division
  remainder = num1 % num2
  quotient = num1 // num2
  print(f"The result of this division is {quotient} with a remainder of {remainder}")

# reaminder_division()



# ============================  Question NO 06 ================================
def roll_dice():
  first_dice = random.randint(1,6)
  second_dice = random.randint(1,6)
  total_of_dice = first_dice + second_dice

  print(f"Roll of first dice {first_dice}")
  print(f"Roll of second {second_dice}")
  print(f"Total of both dice {total_of_dice}")

# roll_dice()



# ============================  Question NO 07 ================================
def seconds_in_year():
   total_days_in_year = 365
   total_hours_in_day = 24
   total_mins_in_hour = 60
   total_sec_in_mins = 60
   total_seconds_in_year = total_days_in_year * total_hours_in_day * total_mins_in_hour * total_sec_in_mins
   print(f"There are total {total_seconds_in_year} seconds in a year")

# seconds_in_year()



# ============================  Question NO 08 ================================
def tiny_mad_lib():
  sentence_start = "Code in Place is fun. I learned to program and used Python to make my"
  noun = input("Please type a noun and press enter.")
  adjective = input("Please type an adjective and press enter.")
  verb = input("Please type a verb and press enter.")
  print(f"{sentence_start} {noun} {adjective} {verb}")

# tiny_mad_lib()



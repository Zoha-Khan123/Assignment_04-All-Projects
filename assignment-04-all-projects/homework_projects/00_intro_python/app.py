
# ============================  Question NO 01 ================================
def add_two_number():

    print(f"Question NO 01 \nAdd Two Numbers")
    num1:str = input("Enter first number: ")
    num1_change_into_number:int = int(num1)
    num2:str = input("Enter second number: ")
    num2_change_into_number:int = int(num2)
    add_two_number:int = num1_change_into_number + num2_change_into_number
    print(f"The total of {num1_change_into_number} and {num2_change_into_number} is {add_two_number} .")

# add_two_number()

# ============================  Question NO 02 ================================

def aggrement_bot():

    print(f"Question NO 02 \nAggrement Bot")
    favourite_animal:str = input("What's your favorite animal? ")
    print(f"My favorite animal is also {favourite_animal}!")

# aggrement_bot()



# ============================  Question NO 03 ================================

def temperature():

    print(f"Question NO 03 \nFahrenheit to Celsius")
    temperature_in_fahrenheit:str = input("Enter temperature in Fahrenheit: ")
    temperature_change_into_number:int = int(temperature_in_fahrenheit)
    temperature_change_into_float:float = float(temperature_change_into_number)
    calculation_change_into_celsius = (temperature_change_into_number - 32) * 5.0/9.0
    print(f"Temperature: {temperature_change_into_float}.F = {calculation_change_into_celsius}.C ")


# temperature()

# ============================  Question NO 04 ================================
def find_age():

    print(f"Question NO 04 \nHow old are they")
    anton : int = 21
    beth : int = 6 + anton
    chen : int = 20 + beth
    drew : int = chen + anton
    ethan : int = chen


    print("Anton is " + str(anton))
    print("Beth is " + str(beth))
    print("Chen is " + str(chen))
    print("Drew is " + str(drew))
    print("Ethan is " + str(ethan))

# find_age()

# ============================  Question NO 05 ================================
def triangle_perimeter():

    print(f"Question NO 05 \nPerimeter Of Triangle")
    side1 : float = float(input("What is the length of side1? "))
    side2 : float = float(input("What is the length of side2? "))
    side3 : float = float(input("What is the length of side3? "))

    perimeter_of_triangle : str = side1 + side2 + side3
    print(f"The perimeter of triangle is {perimeter_of_triangle} ")
 
# triangle_perimeter()


# ============================  Question NO 06 ================================
def square():

    print(f"Question NO 06 \nSquare Number")
    square_number : float = float(input("Type a number to see it's square "))
    print(f"{str(square_number)} squared is {str(square_number ** 2)}")

# square()
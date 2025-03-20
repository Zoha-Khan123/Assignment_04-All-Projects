# ============================  Question NO 00 ================================
adult_age = 18
def is_adult(age):
  if age >= adult_age:
    return True

  return False

def choosing_return():
  print("Question No 00 \nChoosing Return\n")
  age = int(input("How old is this person?: "))
  print(is_adult(age))

# choosing_return()


# ============================  Question NO 01 ================================
def greet(name):
  print("Question no 01 \nGreeting\n") 
  print(f"Hello {name}")

def greetings():
  name = input("What's your name? ")
  greet(name)

# greetings()



# ============================  Question NO 02 ================================
def in_range(n,low,high):
  print("Question no 02 \nRange\n")
  if n >= low and n<=high:
    return True
  return False
# print(in_range(2,10,30))


# ============================  Question NO 03 ================================
def fruits():
  print("Question no 03 \nFruits in Stock\n")
  fruit = input("Enter a fruit: ")
  stock = num_in_stock(fruit)
  if stock == 0:
    print("This fruit is not in stock.")
  else:
    print("This fruit is in stock. Here is how many")
    print(stock)


def num_in_stock(fruit):
  if fruit == "apple":
    return 2
  elif fruit == "banana":
    return 5
  elif fruit == "orange":
    return 10
  else:
    return 0

# fruits()


# ============================  Question NO 04 ================================
def get_user_data():
  name = input("Enter your first name ")
  last_name = input("Enter your last name ")
  email = input("Enter your email ")
  return name,last_name,email

def multiple_returns():
  print("Question no 04 \nMultiple Returns\n")
  data = get_user_data()
  print("Data entered successfully",data)

# multiple_returns()


# ============================  Question NO 05 ================================
def subtract_seven(num):
  subtract = 7
  calculate = (num - subtract)
  return calculate

def after_subtracting():
  print("Question no 05 \nSubtract Seven\n")
  sub = subtract_seven(8)
  print(f"This should be {sub}")

# after_subtracting()



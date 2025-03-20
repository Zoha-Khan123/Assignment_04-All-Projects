
# ============================  Question NO 00 ================================
def count_nums():
  print("Question No 00 \nCount Nums")
  store_number = []

  while True:
    user_input = input("Enter a number ? (Press Enter to stop) ")
    if user_input == "":
      print("Good Bye ")
      break

    try:
      user_number = int(user_input)
      store_number.append(user_number)
    except ValueError:
      print("Please enter a valid number ")

  print("\nNumber Frequencies:")
  for num in sorted(set(store_number)):
    print(f"{num} appears {store_number.count(num)} times ")

  return store_number

# count_nums()



# ============================  Question NO 01 ================================
def phonebook():
  print("Question No 01 \nPhonebook")

  contact_list = {}

  # Take user name
  while True:
    user_name = input("Enter your name , (Press Enter to Exit) ")
    if user_name == "":
      print("Good bye")
      break

  # Take user number
    while True:
      user_number = input("Enter your mobile no: ")
      if len(user_number) == 11:
        user_number = int(user_number)
        contact_list[user_name] = user_number
        print("Contact added successfully")
        break
      else:
        print("Please enter a valid number")

#  Show Contact Numbers
  if len(contact_list) > 0:
    print("\nContact List:")
    for idx , (name , number) in enumerate(contact_list.items()):
      print(f"{idx}- {name} : {number}")
  else:
    print("No contacts found")
  def search_numbers():
    print("\nSearch Contact Numbers")
    search = input(f"\nEnter name to search your number ")
    if search in contact_list:
      print(f"\n✅ {search.capitalize()}'s Number: {contact_list[search]}")
    else:
      print("Number not found")
  search_numbers()

  return contact_list

# phonebook()



# ============================  Question NO 02 ================================
def pop_up_shop():
    print("Question No 02 \nPop Up Shop")
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}

    total = 0
    while True:
        for fruit , price in fruits.items():
          quantity = input(f"How many {fruit} do you want? (Enter stop for break) ")

          if quantity == "stop":
            print(f"Your total amount so far is ${total:.2f}")
            print("Good Bye")
            return

          if not quantity.isdigit():
            print("Please enter a valid number")
            continue
          quantity = int(quantity)
          total += (quantity * price)

        print(f"your total amount is ${total}")
        break

# pop_up_shop()



# ============================  Question NO 03 ================================
from hashlib import sha256

def hash_password(password_to_check):
  return sha256(password_to_check.encode()).hexdigest()


def login(email,store_login,password_to_check):
  if store_login[email] == hash_password(password_to_check):
    print("Login successful")
  else:
    print("Login failed")

def user_data():
   print("Question No 03 \nPowerful Passwords")
   stored_logins = {
        "alice@coffee.com": hash_password("password"),
        "bob@coffee.com": hash_password("espresso"),
    }
    # Test logins
   login("alice@coffee.com",stored_logins,"password")
   login("alice@coffee.com", stored_logins, "word")
   login("bob@coffee.com", stored_logins, "espresso")
   login("bob@coffee.com", stored_logins, "latte")


# user_data()



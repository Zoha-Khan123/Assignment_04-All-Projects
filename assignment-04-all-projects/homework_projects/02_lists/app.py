# ============================  Question NO 01 ================================
list_of_numbers = [1,2,3,4,5]

def add_number(list):
  total = 0
  for i in list_of_numbers:
    total += i
  print(f"Sum of all numbers is {total}")

# add_number(list_of_numbers)



# ============================  Question NO 02 ================================
list_of_numbers = [1,2,3,4,5]

def double_list(list):
  doubled_numbers = []
  for i in list_of_numbers:
     doubled_numbers.append(i + i)
  print(doubled_numbers)

# double_list(list_of_numbers)



# ============================  Question NO 04 ================================
def add_three_copy():
  store_mess = []
  mess = input("Enter a message to copy: ")
  print(f"Before list {store_mess} ")

  i = 1
  while i < 4:
    store_mess.append(mess)
    i += 1
  print(f"After list {store_mess}")

# add_three_copy()



# ============================  Question NO 05 ================================
def get_first_element():
    store_list = []
    i = ""

    while True:
        i = input("Please enter an element of the list or type 'stop' to exit: ")

        if i == "":
            print("You cannot enter an empty input. ")
            continue

        if i.lower() == "stop":
            break

        store_list.append(i)


        if store_list:
            first_index = store_list[0]

    print(f"List is here: {store_list}")
    first_index = store_list[0]
    print(f"The first element of list is {first_index}")

# get_first_element()



# ============================  Question NO 06 ================================
def get_last_element():
    store_list = []
    i = ""

    while True:
        i = input("Please enter an element of the list or type 'stop' to exit: ")

        if i == "":
            print("You cannot enter an empty input. ")
            continue

        if i.lower() == "stop":
            break

        store_list.append(i)


        if store_list:
            last_index = store_list[0]

    print(f"List is here: {store_list}")
    last_index = store_list[-1]
    print(f"The last element of list is {last_index}")

# get_last_element()





# ============================  Question NO 07 ================================
def get_list():
    store_list = []
    i = ""

    while True:
        i = input("Please enter an element of the list or type 'stop' to exit: ")

        if i == "":
            print("You cannot enter an empty input. ")
            continue

        if i.lower() == "stop":
            break

        store_list.append(i)


    print(f"List is here: {store_list}")

# get_list()




# ============================  Question NO 08 ================================
def shorten_list():
    store_list = []
    i = ""
    max_length = 3

    while True:
        i = input("Please enter an element of the list or type 'stop' to exit: ")

        if i == "":
            print("You cannot enter an empty input. ")
            continue

        if i.lower() == "stop":
            break

        store_list.append(i)

        while len(store_list) > max_length:
            remove_last = store_list.pop()
            print(f"This is removed {remove_last}")


    print(f"List is here: {store_list}")

# shorten_list()
# ================== Problem No 01 =====================

def list_practice():
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    print("List:",fruit_list)
    fruit_length = len(fruit_list)
    print(f"Length of a List: {fruit_length}")
    fruit_list.append("mango")
    print(f"Updated List: ",fruit_list)

# list_practice()


# ================= Problem No 02 =====================



# ============== Accessing Elements: ===================

def accessing_elements(elements_list):
        access_element = input("Which element would you like to access? Please enter the index number: ")
        
        try:
            number = int(access_element)
            print(f"Here is your element {elements_list[number]}")
        except IndexError as e:
            print(f"Index Error: {e}")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


# ============ # Modifying Elements ===================

def modifying_elements(elements_list):
    access_element = input(f"Which element you want to access in the list and modifying it ")

    try:
        number = int(access_element)
        print(f"Here is your element {elements_list[number]}")
    except IndexError as e:
            print(f"Index Error: {e}")
    except ValueError:
            print("Invalid input! Please enter a valid integer.")
    else:
        modifying_elements = input("Write new element which modify the index no you choose ")
        elements_list[number] = modifying_elements
        print(f"Here is your modifying list {elements_list}")
         



# ============ # Modifying Elements ===================

def slicing_elements(elements_list):
    start_index = input(f"Write start index ")
    end_index = input(f"Write end index ")

    try:
        start_number = int(start_index)
        a = elements_list[start_number]
        end_number = int(end_index)
        b = elements_list[end_number]
        slicing = elements_list[start_number:end_number]
        print(f"Here is a new list containing the elements from the start index up to the end index. {slicing}")
    except IndexError as e:
            print(f"Index Error: {e}")
    except ValueError:
            print("Invalid input! Please enter a valid integer.")
    



# ==================== Index Game ========================

def index_game():
    elements_list = ["Zoha",20,True,20.5,1j]
    print(f"Here is a list {elements_list}")
    print("Choose an operation: access, modify, slice")
    operation = input("Enter operation: ").lower()
    if operation == "access":
        accessing_elements(elements_list)
    elif operation == "modify":
        modifying_elements(elements_list)
    elif operation == "slice":
        slicing_elements(elements_list)
    else:
        print("Invalid Operation")

index_game()
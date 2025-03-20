# ============================  Question NO 00 ================================
def average_number(first_num, second_num):
  print("Question no 00 \nCalculate Average\n")
  average = (first_num + second_num)/2
  print(average)

# average_number(0,10)


# ============================  Question NO 01 ================================
def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            return 
        print(curr_num)

def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")

# if __name__ == "__main__":
    # main()



# ============================  Question NO 02 ================================
def count_even():
    print("Question no 02 \nCount Even")
    store_even = []
    while True:
        try:
            user_input = input("Enter a number or press 'enter' to exit: ")
            if user_input == "":
                break
            number = int(user_input)
            if(number % 2 == 0):
                store_even.append(number)
                total_even = len(store_even)
        except:
            print("Please enter a valid number ")
    print(f"Total even number is {total_even}")


# count_even()


# ============================  Question NO 04 ================================
def double_num():
    print("Question no 04 \nDouble Number")
    while True:
        try:
            user_num = input(f"Give me a number, and I'll magically double it! or press 'enter' to exit ")
            if user_num == "":
                print("Exit loop bye")
                break
            else:
                number = int(user_num)
                double = number * 2
                print(f"The double of {number} is {double}")
        except:
            print("Please enter a valid number")


# double_num()


# ============================  Question NO 05 ================================
def get_name():
    print("Question no 05 \nGet Name\n")
    name = "Zoha Khan"
    return name

def greet_user():
    user_name = get_name()
    print(f"Hello! {user_name}")

# greet_user()


# ============================  Question NO 06 ================================
def is_odd_or_even():
    print("Question no 06 \nOdd or Even")
    for i in range(10):
        if(i % 2 == 0):
            print(f"{i} even")
        else:
            print(f"{i} odd")

# is_odd_or_even()


# ============================  Question NO 07 ================================
def divisor(num):
 print("Question no 07 \nDivisor")
 for i in range(num):
    divior = i + 1
    if num % divior == 0:
        print(divior)

# divisor(12)


# ============================  Question NO 08 ================================
def print_multiple():
    print("Question no 08 \nPrint Multiple")
    message = input("Please type a message: ")
    repeat_no = int(input("Enter a number of times to repeat your message: "))

    repeat = "\n".join([message] * repeat_no)
    print(repeat)

# print_multiple()


# ============================  Question NO 09 ================================
def sentence_generator():
    print("Question no 09 \nSentence Generator")
    word = input("Please type a noun, verb, or adjective: ")
    print("Is this a noun, verb, or adjective?")
    try:
        part_of_speech = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
        print(word,part_of_speech)

        if part_of_speech == 0:
            print(f"The {word} was placed carefully on the shelf.")
        elif part_of_speech == 1:
            print(f"Every morning, I love to {word} before starting my day.")
        elif part_of_speech == 2:
            print(f"The weather outside is absolutely {word} today!")
        else:
            print("Part of speech must be 0, 1, or 2! Can't make a sentence.")
    except ValueError:
        print("Invalid input! Please enter 0, 1, or 2.")

# sentence_generator()


# ============================  Question NO 10 ================================

def print_ones_digit(num):
 print("Question no 10 \nPrint Ones Digit")
 last_digit = num % 10
 print(last_digit)

# print_ones_digit(25887878659)
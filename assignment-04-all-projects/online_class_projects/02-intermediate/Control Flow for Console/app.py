import random


def high_low_game():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')


    NUM_ROUNDS = 5
    i = 1
    score = 0
    
    while i <= NUM_ROUNDS:

        # Round Start
        print(f"Round {i}")

        # User Random Number
        user_number = random.randint(1,100)
        print(f"Your number is {user_number}")
        print("Do you think your number is higher or lower than the computer's?:")

        # Check userinput is h or l 
        while True:
            user_guess = input("Please enter (h) for higher or (l) for lower ").lower()
            if user_guess == "h" or user_guess == "l":
                break
            else:
                print("❌ Invalid input! Please enter only 'h' or 'l'.")


        # Computer Random Number
        computer_number = random.randint(1,100)
        print(f"{computer_number}")


        # Rules of win and loss
        if(user_number > computer_number and user_guess == "h" or user_number < computer_number and user_guess == "l"):
            print(f"🎯 You were right! The computer's number was {computer_number}.")
            score += 1
            print(f"Your score is now {score}")
            print('--------------------------------\n')
        else: 
            print(f"❌ Aww, that's incorrect. The computer's number was {computer_number}.")
            print(f"Your score is now {score}")
            print('--------------------------------\n')
    

        # Next Round Start
        i += 1

    # Final Score
    print(f"Your final score is {score}")
        
    # Ranking for win and loss
    if score == NUM_ROUNDS:
        print("✅ Perfect Score: 🎉 Incredible! You guessed everything right! 🏆\n")
    elif score < NUM_ROUNDS:
        print("🟡 Partial Score: 👍 Good job! Keep practicing! 🚀\n")
    else:
        print("❌ Zero Score: 😅 Tough luck! Try again! 🔄\n")

    print('------------ THE END -------------\n\n')


if __name__ == "__main__":
    high_low_game()






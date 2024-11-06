import random

def get_computer_choice():
    return random.choice(['🤚', '✋'])

#def get_user_choice():
    #while True:
        #user_choice = input("Enter your choice (🤚 or ✋): ")
        #if user_choice in ['🤚', '✋']:
            #return user_choice
        #print("Invalid choice. Please enter either 🤚 or ✋.")

def play_round(x):
    user_choice = x
    computer1_choice = get_computer_choice()
    computer2_choice = get_computer_choice()

    print(f"Computer 1's choice: {computer1_choice}")
    print(f"Computer 2's choice: {computer2_choice}")
    print(f"User's choice: {user_choice}")

    user_score = int(user_choice == computer1_choice) + int(user_choice == computer2_choice)
    computer1_score = int(computer1_choice == user_choice) + int(computer1_choice == computer2_choice)
    computer2_score = int(computer2_choice == user_choice) + int(computer2_choice == computer1_choice)

    return user_score, computer1_score, computer2_score

def main(x):
    rounds = 5
    user_total = 0
    computer1_total = 0
    computer2_total = 0

    for _ in range(rounds):
        print("\nNew Round")
        user_score, computer1_score, computer2_score = play_round(x)
        user_total += user_score
        computer1_total += computer1_score
        computer2_total += computer2_score

    print("\nFinal Scores:")
    print(f"User: {user_total}")
    print(f"Computer 1: {computer1_total}")
    print(f"Computer 2: {computer2_total}")

    if user_total > computer1_total and user_total > computer2_total:
        print("You are the winner!")
    elif computer1_total > user_total and computer1_total > computer2_total:
        print("Computer 1 is the winner!")
    elif computer2_total > user_total and computer2_total > computer1_total:
        print("Computer 2 is the winner!")
    else:
        if user_total == computer1_total:
            print("User and Computer 1 are equal!")
        if user_total == computer2_total:
            print("User and Computer 2 are equal!")
        if computer1_total == computer2_total:
            print("Computer 1 and Computer 2 are equal!")

if __name__ == "__main__":
    main()

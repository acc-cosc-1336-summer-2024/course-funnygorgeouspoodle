from src.homework.d_repetition.repetition import get_factorial, sum_odd_numbers 

def menu():
    print("1-Factorial") 
    print("2-Sum odd numbers") 
    print("3-Exit")

def user_controlled_loop():
    choice = "1"
    while(choice != 3):
        menu()
        choice = input("Enter the desired choice (1,2,3): ")
        handle_menu_choice(choice)
quit_program = input("Do you want to exit? (y/n): ").lower()

def handle_menu_choice(choice):
        if (choice == "1"):
            num = int(input("Please enter a number to calculate factorial between (1-9): ")) 
            if 1 <= num <= 9:
                print(f" The factorial of {num} is: {get_factorial(num)}")
            else:
                print("Invalid input. Please enter number between  1 and 9.")
        elif (choice == "2"):
            num = int(input("Please enter a number to calculate sum of odd numbers between (1-99):  "))
            if 1 <= num <= 99:
                print(f"The sum of odd numbers up to {num} is: {sum_odd_numbers(num)}")
            else:
                print("Invalid input. Please enter number between  1 and 90.")

        elif (choice == "3"):
            if quit_program == "y":
                break


            




   

from termcolor import colored
import random

def get_nums():
    """
    Prompt user to input a series of nums, then return them sorted in ascending order

    Returns:
        list: A sorted list of numbers
    """
    
    choice = input(colored("\nWelcome! Would you like to provide your own array of numbers? Y for yes, N for no\n", "light_cyan"))

    if choice == "Y":
        while True:
            try:
                user_input = input(colored("Enter numbers separated by spaces. Press enter when done:\n", "light_cyan"))

                if not user_input:
                    print(colored("Input cannot be empty. Please enter at least one integer.", "red"))
                    continue

                nums = list(map(int, user_input.split()))                
                sorted_nums = sorted(nums)
                print(colored(f"Thank you!\nSorted nums: {sorted_nums}", "green"))
                return sorted_nums
            except ValueError:
                print(colored("Invalid input. Please enter a series of integers separated by spaces.", "red"))
    
    elif choice == "N":
        while True:
            try:
                print(colored("No problem! I can generate some random numbers for you.", "light_cyan"))
                nums_size = int(input(colored("How many numbers should i pick? (0 - 100)\n", "light_cyan")))
                min_val = int(input(colored("Minimum numerical value?\n", "light_cyan")))
                max_val = int(input(colored("Maximum numerical value?\n", "light_cyan")))

                if nums_size <= 0 or nums_size > 100:
                    print(colored("Size must be a positive number < 100. Try again!", "red"))
                    continue
                if min_val > max_val:
                    print(colored("Minimum value cannot be greater than maximum value.", "red"))
                    continue

                nums = [random.randint(min_val, max_val) for _ in range(nums_size)]
                sorted_nums = sorted(nums)
                print(colored(f"Thank you!\nSorted nums: {sorted_nums}", "green"))
                return sorted_nums
            except ValueError:
                print(colored("Invalid input. Please enter integers only.", "red"))



def get_menu_choice():
    user_nums = get_nums()

    while True:
        try:
            print(colored("\n-- MENU --"))
            print(colored("1\tPerform BFS"))
            print(colored("2\tPerform DFS"))
            print(colored("3\tRestart"))
            print(colored("4\tQuit"))

            choice = input(colored("What action would you like to perform?\n")).strip()

            if choice == "1":
                print(colored("Performing BFS...", "magenta"))
            elif choice == "2":
                print(colored("Performing DFS...", "magenta"))
            elif choice == "3":
                user_nums = get_nums()
            elif choice == "4":
                print(colored("Quitting. Goodbye!", "magenta"))
                break
            else:
                print(colored("Invalid choice. Please select 1, 2, or 3.", "red"))
                continue

        except ValueError:
            print(colored("Invalid input. Please enter a valid number.", "red"))
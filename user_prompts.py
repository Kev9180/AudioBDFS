from termcolor import colored

def get_nums():
    """
    Prompt user to input a series of nums, then return them sorted (asc)

    Returns:
        list: A sorted list of numbers
    """

    while True:
        try:
            user_input = input("Enter numbers separated by spaces. Press enter when done:\n")

            if not user_input:
                print(colored("Input cannot be empty. Please enter at least one integer.", "red"))
                continue

            nums = list(map(int, user_input.split()))                
            sorted_nums = sorted(nums)
            print(colored(f"Sorted nums: {sorted_nums}", "green"))
            return sorted_nums
        except ValueError:
            print(colored("Invalid input. Please enter a series of integers separated by spaces.", "red"))

def get_menu_choice():
    while True:
        try:
            print("\n-- MENU --")
            print("1\tPerform BFS")
            print("2\tPerform DFS")
            print("3\tUpdate nums")
            print("4\tQuit")

            choice = input("What action would you like to perform?\n").strip()

            if choice == "1":
                print(colored("Performing BFS...", "cyan"))
            elif choice == "2":
                print(colored("Performing DFS...", "cyan"))
            elif choice == "3":
                print(colored("Getting new nums...", "cyan"))
            elif choice == "4":
                print(colored("Quitting. Goodbye!", "magenta"))
                break
            else:
                print(colored("Invalid choice. Please select 1, 2, or 3.", "red"))
                continue

        except ValueError:
            print(colored("Invalid input. Please enter a valid number.", "red"))
# Display funtion program
#Author: Frank R. Leotta III
#Date created: 2/14/2024

#Discription: This program will present a menu and allow them to see the differnt functions that were created by myself.

#status: working on it

#do next: work on choice, left it incorrect for now




def main():
    print("Welcome to the Math Function Program")
    continue_options = ("y", "n", "yes", "no" "Yes", "No", "Y", "N")
    continue_choice = input("Would you like to see the menu? (y/n): ")
    while continue_choice != "n" or continue_choice != "y":
        continue_choice = input("Would you like to see the menu? (y/n): ")
        if continue_choice == "n"or continue_choice == "y":
            break #also could use continue, or have switch






if __name__ == "__main__":
    main()
        # if main == main:
        #     print("The code that would fit at $PLACEHOLDER$ is:")
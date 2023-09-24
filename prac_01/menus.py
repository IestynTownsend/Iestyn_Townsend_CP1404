"""User Enters their name"""
user_name = input("Enter name: ")

"""Setting what is to be displayed to show the user what options are valid"""
options = """H - Hello
G - Goodbye
Q - Quit"""

"""Displaying those options along with an indicator to show the user where to type their response"""
print(options)
choice = input(">>> ").upper()

"""if, elif, else loop to say either hello, goodbye or quit the program depending on what the user response was"""
while choice != "Q":
    if choice == "H":
        print("Hello", user_name)
    elif choice == "G":
        print("Goodbye", user_name)
    else:
        """For incase the user selects an invalid option"""
        print("Please select a valid option")
    print(options)
    choice = input(">>> ").upper()
print("Program Closed")

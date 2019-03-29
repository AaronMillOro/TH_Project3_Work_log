"""
Python Web Development Techdegree
Project 3 - Work log
--------------------------------
"""
from tools import Clean, MenuSearch
from task import Task


MAIN_MENU = ("""
*******   WORK LOG   *******\n
What would you like to do?\n
a) Add an entry
b) Search existing entries
c) Quit program\n
> """)


# Main menu with options
def main_menu():
    Clean()
    while True:
        choice = input(MAIN_MENU)
        Clean()
        if choice.lower() == "a":
            test = Task()
            test.show_task()

        elif choice.lower() == "b":
            MenuSearch()
            #print("search ADD item")
        elif choice.lower() == "c":
            print("See you next time!")
            break
        else:
            print("'{}' is an invalid option! Please try again".format(choice))


if __name__ == "__main__":
    main_menu()

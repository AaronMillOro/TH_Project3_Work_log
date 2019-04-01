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


def main_menu():
    Clean()
    while True:
        choice = input(MAIN_MENU)
        Clean()
        if choice.lower() == "a":
            item = Task()
            item.in_out_task()
        elif choice.lower() == "b":
            MenuSearch()
        elif choice.lower() == "c":
            print("See you next time!")
            break
        else:
            print("'{}' invalid option! Please try again".format(choice))


if __name__ == "__main__":
    main_menu()

import os

MENU_SEARCH = ("""
*******   WORK LOG   *******\n
Do you want to search by:\n
a) Exact date
b) Time spent
c) Exact search
d) Regex pattern
e) Return tu main menu\n
> """)


class MenuSearch:

    def __init__(self):
        while True:
            decision = input(MENU_SEARCH)
            Clean()
            if decision.lower() == "a":
                print("Enter exact date to find (DD/MM/YYYY): ")
                pass
            elif decision.lower() == "b":
                print("Enter exact time spent (rounded minutes): ")
                pass
            elif decision.lower() == "c":
                print("Enter the keyword to search: ")
                pass
            elif decision.lower() == "d":
                print("Enter a regex pattern: ")
                pass
            elif decision.lower() == "e":
                break
            else:
                print("'{}' is an invalid option! Try again".format(decision))


class Clean:

    def __init__(self):
        os.system('cls' if os.name == 'nt' else 'clear')

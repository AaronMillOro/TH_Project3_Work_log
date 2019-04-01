import csv
import datetime
import os

from search import search_date, search_time, search_string, search_regex

MENU_SEARCH = ("""
*******   WORK LOG   *******\n
Do you want to search by:\n
a) Exact date
b) Time spent
c) Exact search
d) Regex pattern
e) Return to main menu\n
> """)


class MenuSearch:

    def __init__(self):
        while True:
            decision = input(MENU_SEARCH)
            presence_log = os.path.isfile("log_file.csv")
            if presence_log == True:
                Clean()
                # Read file to iterate
                task_log = open("log_file.csv")
                task_log = csv.DictReader(open('log_file.csv'), delimiter="\t")
                task_log = [task for task in task_log]

                if decision.lower() == "a":
                    Clean()
                    search_date(task_log)
                    Clean()
                elif decision.lower() == "b":
                    Clean()
                    search_time(task_log)
                    Clean()
                elif decision.lower() == "c":
                    Clean()
                    search_string(task_log)
                    Clean()
                elif decision.lower() == "d":
                    Clean()
                    search_regex(task_log)
                    Clean()
                elif decision.lower() == "e":
                    break
                else:
                    print("'{}' Invalid option! Try again".format(decision))
            else:
                Clean()
                print("Please add first a task")
                break


class Clean:

    def __init__(self):
        os.system("cls" if os.name == "nt" else "clear")

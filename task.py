import csv
import datetime
import os


from tools import Clean


class Task:

    def __init__(self):
        # Verify correct date input
        while True:
            task_date = input("Date of task.\nPlease use DD/MM/YYYY format: ")
            try:
                task_date = datetime.datetime.strptime(task_date, "%d/%m/%Y")
                if task_date > datetime.datetime.now():
                    print("That date hasn't happen yet. Please try again")
                    continue
                else:
                    break
            except ValueError:
                print("That's not a valid format. Please try again")
        self.task_date = task_date
        # clear screen and check that a string title is added
        Clean()
        while True:
            title = input("Title of task: ")
            if not title.strip():
                print("Empty String! Please write task's title")
            else:
                break
        self.title = title
        # Task time check as integer
        Clean()
        while True:
            time_minutes = input("Time spent (rounded minutes): ")
            try:
                time_minutes = int(time_minutes)
                if time_minutes < 0:
                    zero_validation = time_minutes / 0
                break
            except ValueError:
                print("Please enter a valid number")
            except ZeroDivisionError:
                print("Please enter a positive number")
        self.time_minutes = time_minutes
        # input notes  freestyle
        Clean()
        notes = input("Notes (optional): ")
        self.notes = notes
        Clean()
        leave = input("The entry was added. Press anything to continue\n")
        Clean()

    def in_out_task(self):
        presence_file = os.path.isfile("log_file.csv")
        # if previous log_file is present read file to a list
        if presence_file == True:
            csv_file = open("log_file.csv")
            csv_file = csv.DictReader(open('log_file.csv'),
            delimiter="\t")
            tasks_info = [task for task in csv_file]
            tasks_info.append(self.__dict__)
            # store new information
            with open("log_file.csv", "w", encoding='utf8', newline='') as out:
                w = csv.DictWriter(out, delimiter="\t",
                    fieldnames=self.__dict__.keys())
                w.writeheader()
                for task in tasks_info:
                    w.writerow(task)
        # if not present create the csv file
        else:
            with open("log_file.csv", "w", encoding='utf8') as out:
                w = csv.DictWriter(out, delimiter="\t",
                    fieldnames=self.__dict__.keys())
                w.writeheader()
                w.writerow(self.__dict__)

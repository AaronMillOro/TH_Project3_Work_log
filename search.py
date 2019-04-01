import datetime
import re


def search_date(dict):
    while True:
        date_search = input("Date to search (DD/MM/YYYY): ")
        try:
            date_search = datetime.datetime.strptime(date_search, "%d/%m/%Y")
            break
        except ValueError:
            print("Not a valid format. Please try again")
    # convert to string to make it comparable to records
    date_search = str(date_search)
    i = 0
    subset = []
    print("Records with that date:")
    for item in dict:
        t_date_dict = item.get("task_date")
        if date_search == t_date_dict:
            i += 1
            subset.append(item)
            print(i, ")", t_date_dict, item.get("title"))
    if i == 0:
        exit = input("No match found.\nPress any key to return")
    else:
        while True:
            try:
                view_info = abs(int(input("\nSelect a number:\n")))
                zero_validation = 1 / view_info
                # show task information
                for key, value in subset[view_info - 1].items():
                    print(key, ":", value)
                exit = input("\nPress anything to return. ")
                break
            except ValueError:
                print("Enter a number of task.")
            except IndexError:
                print("Enter a number between 1-", i)
            except ZeroDivisionError:
                print("Enter a number between 1-", i)


def search_time(dict):
    while True:
        timing = input("Time spent (rounded minutes): ")
        try:
            timing = int(timing)
            if timing < 0:
                zero_validation = timing / 0
            break
        except ValueError:
            print("Please enter a valid number")
        except ZeroDivisionError:
            print("Please enter a positive number")
    timing = str(timing)
    i = 0
    subset = []
    print("Records with that time spent:")
    for item in dict:
        time_dict = item.get("time_minutes")
        if timing == time_dict:
            i += 1
            subset.append(item)
            print(i, ") Task: ", item.get("title"), "-", time_dict, " minutes")
    if i == 0:
        exit = input("No match found.\nPress any key to return")
    else:
        while True:
            try:
                view_info = abs(int(input("\nSelect a number:\n")))
                zero_validation = 1 / view_info
                for key, value in subset[view_info - 1].items():
                    print(key, ":", value)
                exit = input("\nPress anything to return. ")
                break
            except ValueError:
                print("Enter a number between 1-", i)
            except IndexError:
                print("Enter a number between 1-", i)
            except ZeroDivisionError:
                print("Enter a number between 1-", i)


def search_string(dict):
    while True:
        keyword = input("Keyword to search: ")
        if not keyword.strip():
            print("Empty field! Add a keyword")
        else:
            break
    keyword = keyword.lower()
    i = 0
    subset = []
    print("Tasks containing (part of) the keyword in notes or title:")
    for item in dict:
        notes_dict = item.get("notes")
        title_dict = item.get("title")
        if keyword in notes_dict.lower() or keyword in title_dict.lower():
            i += 1
            subset.append(item)
            print(i, ")", item.get("title"))
    if i == 0:
        exit = input("No match found.\nPress any key to return")
    else:
        while True:
            try:
                view_info = abs(int(input("\nSelect a number:\n")))
                zero_validation = 1 / view_info
                for key, value in subset[view_info - 1].items():
                    print(key, ":", value)
                exit = input("\nPress anything to return. ")
                break
            except ValueError:
                print("Enter a number between 1-", i)
            except IndexError:
                print("Enter a number between 1-", i)
            except ZeroDivisionError:
                print("Enter a number between 1-", i)


def search_regex(dict):
    while True:
        regex = input("Enter Regex pattern to match: ")
        if not regex.strip():
            print("Empty field! Try again")
        else:
            break
    # Compile string
    match = re.compile(regex, re.I)
    i = 0
    subset = []
    print("Tasks containing the regex pattern in notes or title:")
    for item in dict:
        notes_dict = item.get("notes")
        title_dict = item.get("title")
        if match.search(notes_dict) or match.search(title_dict):
            i += 1
            subset.append(item)
            print(i, ")", item.get("title"))
    if i == 0:
        exit = input("No match found.\nPress any key to return")
    else:
        while True:
            try:
                view_info = abs(int(input("\nSelect a number:\n")))
                zero_validation = 1 / view_info
                for key, value in subset[view_info - 1].items():
                    print(key, ":", value)
                exit = input("\nPress anything to return. ")
                break
            except ValueError:
                print("Enter a number between 1-", i)
            except IndexError:
                print("Enter a number between 1-", i)
            except ZeroDivisionError:
                print("Enter a number between 1-", i)

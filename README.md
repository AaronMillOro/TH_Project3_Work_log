# WORK LOG
This terminal application is part of the **Treehouse Python Techdegree**. The script registers the work tasks on a certain day and allows to get access to previously registered entries. 
## Project details
* The user is prompted with a main menu to choose whether to add a new entry or search previous entries. The first time of use a *CSV* file is generated contaning the task(s) details. Here an example of *[log_file.csv](https://github.com/AaronMillOro/TH_Project3_Work_log/log_file.csv)*
* By choosing to enter a new work log, the user can provide:
    * The task name and date time
    * A number of minutes spent working on it
    * Additional notes can be recorded (optional)
* By choosing to find a previous entry, the user can select to find by:
    * **Exact date** 
    * **Time spent** 
    * **Keyword** to be found in task names or notes
    * **Regex** pattern present in task names or notes
* When displaying the entries, the entries are displayed in a readable format with the date, task name, time spent, and notes information.
* Basic coding style complies with PEP 8.
* The script catch exceptions and report errors to the user.
To run the application type:
```python
python3 work_log.py
```
Enjoy :shipit:

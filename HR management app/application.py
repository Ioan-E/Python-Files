import csv
import pandas as pd
from datetime import datetime


with open('Python Files/For GIT/HR management app (pandas)/october_database.csv', 'rt') as october_file:
    csv_reader = csv.reader(october_file)
    headcount = 0
    for row in csv_reader:
        _headcount = row[11]
        try:
            _headcount = int(_headcount)
        except ValueError:
            _headcount = 0
        headcount += _headcount

now = datetime.now()
last_month = (now.month - 1) if now.month > 1 else 12
last_month_text = "January February March April May June July August September October November December".split()[last_month-1]

headcount_count = (f'\nThe headcount for {last_month_text} in the Company is {headcount} active employees.\n')


october_data = pd.read_csv('Python Files/For GIT/HR management app (pandas)/october_database.csv')
show_active_vie = f'''\n\n The active VIE for the month of {last_month_text} are: 
                        \n\n {(october_data.loc[(october_data["Contract type"] == "VIE") & (october_data['Contract status'] == 'Employed')])}'''
count_active_vie = f''' \n The active VIE for the month of {last_month_text} is number of ID's: \n\n {(october_data.loc[(october_data['Contract type'] == 'VIE') & (october_data['Contract status'] == 'Employed')]).count()}'''
show_active_interns = f'''\n\n The active interns for the month of {last_month_text} are: \n\n {(october_data.loc[(october_data["Contract type"] == "Intern") & (october_data['Contract status'] == 'Employed')])}'''
count_active_interns = f''' \n The active interns for the month of {last_month_text} is number of ID's: \n\n {(october_data.loc[(october_data['Contract type'] == 'Intern') & (october_data['Contract status'] == 'Employed')]).count()}'''
show_active_consultants = f'''\n\n The active interns for the month of {last_month_text} are: \n\n {(october_data.loc[(october_data["Contract type"] == "Freelancer contract") & (october_data['Contract status'] == 'Employed')])}'''
count_active_consultants = f''' \n The active interns for the month of {last_month_text} is the number of ID's: \n\n {(october_data.loc[(october_data['Contract type'] == 'Freelancer contract') & (october_data['Contract status'] == 'Employed')]).count()}'''

class Departments(object):
    def __init__ (self, department):
        self.department = department

    def __str__(self):
        return f'Department name: {self.department}.'

    def __repr__(self):
        return repr("Company has the following department: " + self.department + ".")

class Managers():
    def __init__ (self, managers):
        self.managers = managers

    def __str__(self):
        return f'Manager name: {self.managers}'

    def __repr__(self):
        return repr("Company has the following manager: " + self.managers + " .")

class ManagersStartYear(Managers):
    def __init__(self,managers,year):
        super().__init__(managers)
        self.year = year

    def __str__(self):
        return '{self.managers} has started in {self.year}. '.format(self=self)

manager_start_year = ManagersStartYear('Anil S.', 2019)

class SeniorityYear: 
    def __init__(self, year): 
        self.year = year
        
    def __gt__(self, other): 
        if(self.year>other.year): 
            return True
        else: 
            return False

Company_presence_countries_dict= {
    1: "Australia",
    2: "Brazil",
    3: "Canada",
    4: "France",
    5: "Hong Kong",
    6: "India",
    7: "Italy", 
    8: "Japan",
    9: "Philippines", 
    10: "Romania", 
    11: "Russia", 
    12: "Singapore", 
    13: "Sweden", 
    14: "United Kingdom",
    15: "United States"
}

def country_decorator(fnc):
    def wrapper():
        print (u'\U0001f310'+' \u2192')
        fnc()
    return wrapper

@country_decorator
def country_list():
    print ("Company has offices in the following locations: ")
    for nr, country in Company_presence_countries_dict.items():
        print("{} {}".format(nr, country))





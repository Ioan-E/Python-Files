from application import headcount, headcount_count, show_active_vie, count_active_vie, show_active_interns, count_active_interns, show_active_consultants, count_active_consultants, Departments, Managers, ManagersStartYear, manager_start_year, SeniorityYear, country_list

print(headcount)

print(headcount_count)

print(show_active_vie)

print(count_active_vie)

print(show_active_interns)

print(count_active_interns)

print(show_active_consultants)

print(count_active_consultants)

departments = [
    Departments('Legal'),
    Departments('Infrastructure'),
    Departments('G&A'),
    Departments('Professional Services'),
    Departments('Customer Succes'),
    Departments ('Global Markets'),
    Departments ('Product Strategy'),
    Departments ('Marketing')
]

for department in departments:
    print(department)  

managers = [
    Managers ('Anil S.'),
    Managers ('Linda M'),
    Managers ('Karoline R.'),
    Managers ('Rob M.'),
    Managers ('Edouard R.'),
    Managers ('Peter T.'),
    Managers ('Ofir G.'),
    Managers ('Joshua M.'),
    Managers ('Antoine M.'),
]
for manager in managers:
    print(manager)

manager_start_year = ManagersStartYear('Anil S.', 2019)
print (manager_start_year)

employee_seniority_1 = SeniorityYear(2019) 
employee_seniority_2 = SeniorityYear(2020) 

if(employee_seniority_1>employee_seniority_2): 
    print("First seniority year is greater than second seniority year") 
else: 
    print("Second seniority year is greater than first seniority year")

country_list()
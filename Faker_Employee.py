#Importing Libraries

from faker import Faker
import random
from datetime import datetime, timedelta
import pandas as pd

#Creating Faker Object
fake = Faker()


# Seed for reproducibility
random.seed(42)

#Creating list
ids = list(); fname = list(); lname = list(); dep = list(); income = list(); join = list()
emails = list()
address_employee= list()

df = pd.read_csv('faker_employee.csv')

# Generate 500 entries
for i in range(1, 1000001):
    employee_id = i
    ids.append(employee_id)
    first_name = fake.first_name()
    fname.append(first_name)
    last_name = fake.last_name()
    lname.append(last_name)
    department = random.choice(["Human Resources",
"Finance",
"Marketing",
"Sales",
"IT",
"Customer Service",
"Operations",
"R&D",
"Legal",
"Administration",
"Logistics",
"QA",
"Product Management",
"PR",
"Facilities Management",
"Business Development",
"Compliance",
"Training and Development",
"Corporate Communications",
"Strategic Planning"])
    dep.append(department)
    salary = random.randint(50000, 80000)
    income.append(salary)
    joining_date = fake.date_between(start_date='-3y', end_date='today').strftime('%Y-%m-%d')
    join.append(joining_date)
    email_id = fake.email()
    emails.append(email_id)
    address = fake.address()
    address_employee.append(address)


    # print(f"{employee_id} | {first_name} | {last_name} | {department} | {salary} | {joining_date}")

# df[["Employee ID","First Name","Last Name","Department","Salary","Joining Date"]] = ids,fname,lname,dep,income,join
df["Employee ID"] = ids
df["First Name"]= fname
df["Last Name"]= lname
df["Department"]= dep
df["Salary"]= income
df["Joining Date"]= join
df["Email ID"]=emails
df["Address"]=address_employee

df.to_csv('faker_employee.csv',index=False)
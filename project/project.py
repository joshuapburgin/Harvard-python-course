import csv
import re
from validator_collection import validators, checkers, errors
import pandas as pd
from pymongo import MongoClient, ASCENDING
from bson.objectid import ObjectId
from openai import OpenAI
import os
from dotenv import load_dotenv


#takes in company attributes, validates them and then returns
class Company:

    #the constructor takes in the company attributes that also includes an employee array, it also initialises an ideal customer profile score that shows if the company is a good fit as a customer based on a few attributes
    def __init__(self, companyID, name, website=None, industry=None):
        self.companyID=int(companyID)
        self.name=name
        self.website=website
        self.industry= industry
        self.employee=[]

    def conver_to_dict(self):
        return {
            "companyID": self.companyID,
            "name": self.name,
            "website": self.website,
            "industry": self.industry,
        }

    #getter for company ID
    @property
    def companyID(self):
        return self._companyID
    #setter for company ID
    @companyID.setter
    def companyID(self, companyID):
        self._companyID=companyID

    #getter for name
    @property
    def name(self):
        return self._name
    #setter for name
    @name.setter
    def name(self, name):
        self._name=name

    #getter for website
    @property
    def website(self):
        return self._website
    #setter for website
    @website.setter
    def website(self, website):
        self._website=website

    #getter for industry
    @property
    def industry(self):
        return self._industry
    #setter for industry

    @industry.setter
    def industry(self, industry):
        self._industry=industry

    #adds one employee to a specific company but user cant choose the company so far built in with code
    def add_employee(self, employee):
        self.employee.append(employee)

    #string handling of object when printed or displayed
    def __str__(self):
        employee_info = '\n'.join(str(emp) for emp in self.employee)
        return f"Company: {self.name}\nIndustry: {self.industry}\nEmployees:\n{employee_info}"



#takes in employee attributes, validates and then returns them
class Employee:

    #receives employee attributes and initialises them
    def __init__(self, employeeID, companyID, name, email, linkedin=None, job_title=None):
        self.employeeID=employeeID
        self.companyID=companyID
        self.name=name
        self.email=email
        self.linkedin=linkedin
        self.job_title=job_title

    #method that takes the employee object and converts it into a dictionary that can be used later in a NoSQL database
    def conver_to_dict(self):
        return {
            "employeeID": self.employeeID,
            "companyID": self.companyID,
            "name": self.name,
            "email": self.email,
            "linkedin": self.linkedin,
            "job_title": self.job_title
        }


    #method for outputting object as a string whenever it is printed
    def __str__(self):
        return f"{self.name} works as a {self.job_title}"

    #getter for employeeID
    @property
    def employeeID(self):
        return self._employeeID
    #setter for employeeID
    @employeeID.setter
    def employeeID(self, employeeID):
        self._employeeID=employeeID

    #getter for companyID
    @property
    def companyID(self):
        return self._companyID
    #setter for companyID
    @companyID.setter
    def companyID(self, companyID):
        self._companyID=companyID

    #getter for name
    @property
    def name(self):
        return self._name
    #setter for name
    @name.setter
    def name(self, name):
        self._name=name

    #getter for email
    @property
    def email(self):
        return self._email
    #setter for name, checks if email is in the correct format
    @email.setter
    def email(self, email):
        nemail=email.lower().strip()
        if email_boolean:=checkers.is_email(nemail):
            self._email=email
        else:
            raise ValueError("Email not in correct format")

    #getter for linkedin
    @property
    def linkedin(self):
        return self._linkedin
    #setter for linkedin, checkk linkedin link is in correct format
    @linkedin.setter
    def linkedin(self, linkedin):
        pattern= r"(https:\/\/www.)?linkedin.com\/in\/*"

        if match:= re.search(pattern, linkedin):
            self._linkedin=linkedin
        else:
            raise ValueError("Linkedin link not in correct format")

    #getter for job title
    @property
    def job_title(self):
        return self._job_title
    #setter for the job title
    @job_title.setter
    def job_title(self, job_title):
        self._job_title=job_title


#reads in file that contains only company information, creates a list of objects of those attributes that were split line by line and CSV file
def reading_company_file():
    many_companies=[]
    with open("company_data.txt") as file:
        reader= csv.DictReader(file)
        for one_company in reader:

            company=Company(one_company['companyID'], one_company['name'].lower().strip(), one_company['website'].lower().strip(), one_company['industry'].lower().strip())
            many_companies.append(company)
            #print(f"Debug: Company - {company.name}, Industry - {company.industry}")  # Debug information
    # for one in many_companies:
    #     print(one)


    return many_companies

#orders the company objects in alphabetical order by the name of the company
def sorting_customer_objects(many_companies):

    sorted_companies= sorted(many_companies, key= lambda customer: customer.name)
    # for one_company in sorted_companies:
    #     print(one_company)
    return sorted_companies

#method asks user for their preference for number of employees and makes sure input is an integer
def input_from_user(number_of_employees):
    try:
        # number_of_employees= int(input("Enter the amount of employees are looking for in your ideal customer profile: "))
        if number_of_employees<1:
            raise ValueError
        return number_of_employees
    except ValueError:
        print("Enter a positive whole number greater than 0 not a string")

#takes in a list of company objects and based on the users preferences assigns a score based on how suitable the company is for the user so far based on the industry and will be expanded
def add_ideal_customer_profile_score(many_companies):
    desired_industry= "technology" #input("What is your desired industry: ")
    desired_employee_count= 5 #input("What is your amount of employees that work for your ideal customer profile: ")

    enriched_data_companies={}


    for one_company in many_companies:
        ideal_customer_score=0

        if one_company.industry==desired_industry and one_company!=None:
            ideal_customer_score=1

        enriched_data_companies[one_company]={"companyID": one_company.companyID, "ideal_customer_score":ideal_customer_score}

    for one_company, info in enriched_data_companies.items():
        print(f"Company: {one_company.name}")
        # print(f"Industry: {one_company.industry}")
        # print(f"Employees: {'None' if not one_company.employee else ', '.join([emp.name for emp in one_company.employee])}")
        print(f"ID: {info['companyID']}, \nScore: {info['ideal_customer_score']}\n")


#reads the employee csv file using pandas and instantiates a employee object that takes in the employee csv file as data
def reading_employee_file():
    many_employees=[]
    dataframe= pd.read_csv("employee_data.txt")

    for index, one_employee in dataframe.iterrows():
        employee=Employee(one_employee['employeeID'],one_employee['companyID'],one_employee['name'],one_employee['email'],one_employee['linkedin'],one_employee['job_title'])
        many_employees.append(employee)

    return many_employees
    # for one in many_employees:
    #     print(one)

# Ensure index on 'companyID' for both companies and employees collections
def ensure_indexes(db):
    try:
        # Clear any existing indexes that might conflict
        db.companies.drop_indexes()
        db.employees.drop_indexes()

        db.companies.create_index([("companyID", ASCENDING)], unique=True)
        db.employees.create_index([("companyID", ASCENDING)], unique=False)
        print("Indexes created on 'companyID' for both companies and employees collections.")
    except Exception as e:
        print(f"failed to create indexes: {str(e)}")

#Employee: takes in list that were read from the text files and sends them off to MongoDB to be stored in unstructred format
def employee_using_mongoDB(many_employees):
    client= MongoClient("localhost",27017)
    db=client.lead_gen_DB
    employees=db.employees

    #removing old data
    db.employees.drop()

    employees_dictionary= [one_employee.conver_to_dict() for one_employee in many_employees]
    employees.insert_many(employees_dictionary)

#Company: takes in list that were read from the text files and sends them off to MongoDB to be stored in unstructred format
def company_using_mongoDB(many_companies):
    client=MongoClient("localhost",27017)
    db=client.lead_gen_DB
    companies=db.companies

    #removing old data
    db.companies.drop()

    #insert new document into collection
    companies_dictionary= [one_company.conver_to_dict() for one_company in many_companies]
    companies.insert_many(companies_dictionary)

def merge_databases_mongoDB():
    client=MongoClient("localhost",27017)
    db=client.lead_gen_DB

     # Ensure indexes are created to improve the performance of the $lookup operation
    ensure_indexes(db)

    companies = db.companies
    employees = db.employees
    leads=db.leads

    # companies_dictionary= [one_company.conver_to_dict() for one_company in many_companies]
    # employees_dictionary= [one_employee.conver_to_dict() for one_employee in many_employees]

    #removing old data
    db.leads.drop()
    db.create_collection("leads")

    #inserting documents into collection
    # leads.insert_many(companies_dictionary)
    # leads.insert_many(employees_dictionary)



    # Aggregation pipeline to merge employees into their respective companies
    pipeline = [
        {
            "$lookup": {
                "from": "employees",
                "localField": "companyID",
                "foreignField": "companyID",
                "as": "employeeList"
            }
        },
        {
            "$addFields": {
                "employeeCount": {"$size": "$employeeList"}  # Adds a field to count employees
            }
        },
        {
            "$match": {
                "employeeCount": {"$gt": 0}  # Filters out companies with no employees matched
            }
        },
        {
            "$merge": {
                "into": "companies",  # Merges back into companies for simplicity in this test
                "on": "companyID",
                "whenMatched": "replace",
                "whenNotMatched": "insert"
            }
        }
    ]
    try:
        # Execute the aggregation pipeline
        db.companies.aggregate(pipeline)

        # Optional: Print results to verify
        print("Companies and employees have been merged into companies collection")
    except Exception as e:
        print(f"Aggregation failed: {str(e)}")

#takes a string as input and partitions the sentence into 2 variables
def input_openai(sentence):
    # number_of_employees=0
    # industry=""
    number_of_employees = None
    industry = None

    load_dotenv()

    client = OpenAI()



    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role" : "system", "content":'You are an expert at extracting specfic information from a sentence. you are going to receive a sentence that contains a number which is going to be capture into a variable called "number_of_employees" and you are going to receive information which is the industry of the company you need to capture this industry into a variable called industry . Do not surround the industry with inverted commas'},
            {"role" : "user", "content": sentence}
        ]
    )
    response=completion.choices[0].message.content



    lines = response.split('\n')


    # print(response)

    for line in lines:
        if "number_of_employees" in line:
            number_of_employees = int(line.split('=')[1].strip())
        elif "industry" in line:
            industry = line.split('=')[1].strip().lower()

    print(f"Number of employees chosen: {number_of_employees}")
    print(f"Industry chosen: {industry}")

    return number_of_employees,industry

#takes in preferences and shows mongodb company database with those specific filters
def targeted_company(number_of_employees,industry):
    client=MongoClient("localhost",27017)
    db=client.lead_gen_DB
    companies=db.companies

    # Aggregation pipeline
    pipeline = [
        {
            "$lookup": {
                "from": "employees",
                "localField": "companyID",
                "foreignField": "companyID",
                "as": "employeeList"
            }
        },

        {
            "$match": {
                "industry": industry,
                "employeeCount": {"$gte": number_of_employees}  # Adjust condition as needed
            }
        }
    ]

    # Execute the aggregation pipeline
    chosen_companies = list(companies.aggregate(pipeline))

    if chosen_companies:
        output = ""
        for one_company in chosen_companies:
            output += f"Company: {one_company['name']}\n"
            for employee in one_company['employeeList']:
                output += f"\tEmployee Name: {employee['name']}\tEmail: {employee['email'].strip()}\n"
        return output.strip()
    else:
        return "There are no companies with those attributes."


#main function where other functions are called
def main():


    # sorting_customer_objects(many_companies)
    # add_ideal_customer_profile_score(many_companies)

    #reading in files into each object
    many_companies=reading_company_file()
    many_employees=reading_employee_file()

    #sending data into NoSQL databases in MongoDB
    company_using_mongoDB(many_companies)
    employee_using_mongoDB(many_employees)
    merge_databases_mongoDB()

    #Getting preferences from user
    number_employees, industry= input_openai(input("Please enter the industry and number of employees you are looking for in a company: "))
    # input_openai("retail and 5 employees")
    # input_from_user()

    #searching for chosen companies
    # targeted_company(1,"technology")
    output= targeted_company(number_employees, industry)

    print(output)


    # employee1 = Employee("Joshua Burgin", "joshob@gmail.com", "https://www.linkedin.com/in/joshua-burgin-a77081243/","Sales Development Representative")
    # company= Company("Comet", "https://www.comet.com/site/", "Technology")

    # company.add_employee(employee1)
    # print(company)




if __name__ == "__main__":
    main()

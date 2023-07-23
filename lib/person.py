#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="guido", job="Purchasing"):
        self.name = name
        self.job = job

    def get_name(self):
        return self._name
        
    def set_name(self, name):
        if isinstance(name, str) and (1 <= len(name) <= 25):
            self._name = name.title()
        else:
            print ("Name must be string between 1 and 25 characters.")
    
    name = property(get_name, set_name)

    def get_job(self):
        return self._job
    
    def set_job(self, job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")
        
    job = property(get_job, set_job)
    
# The code first defines a list of approved jobs called APPROVED_JOBS. The list contains 12 job titles.

#The name property has two methods: get_name() and set_name(). The get_name() method simply returns the value of the _name attribute. The set_name() method takes a name argument and sets the value of the _name attribute to the value of the argument. The set_name() method also validates the value of the name argument, ensuring that it is a string between 1 and 25 characters long.

#The job property has two methods: get_job() and set_job(). The get_job() method simply returns the value of the _job attribute. The set_job() method takes a job argument and sets the value of the _job attribute to the value of the argument. The set_job() method also validates the value of the job argument, ensuring that it is one of the approved jobs in the APPROVED_JOBS list.

#The code then creates a new Person object and sets the name property to "guido" and the job property to "Purchasing". The code then prints the value of the name property and the job property.
# importing libraries to help with program

import random
import time

# Functions for using text files

def storedata(end_day):                                 # end_day variable to be used at end of program
    try:
        with open("daily_operations.txt","w",encoding = "UTF-8") as store:
            operations = store.write(str(end_day))
    except FileNotFoundError:                           # store variable used as retains the data for next run of the program
        print("Cannot find the file")


def update(cycle):                                      # cycle as used in maintenance cycle
    try:
        with open("daily_operations.txt", "a",encoding = "UTF-8") as maintain:
            main = maintain.write(str(cycle))
    except FileNotFoundError:                           # maintain used this used in maintenace cycle
        print("Cannot find the file")


def opendata():
    try:
        with open("daily_operations.txt","r",encoding = "UTF-8") as start:
            new = start.read()
            print(new)
    except FileNotFoundError:                           # new and start used as variables as it"s used first thing in the program
        print("Cannot find the file")


# function to start the program

def begin_production():
    
    start = str(input("Begin production Y/N? "))        # start used as it starts whole process
    user = ["u", "s", "e", "r",]                        # user used as it lists all the usernames of the system 
    correct = ["yes", "y"]                              # correct variable as list contains only accepted inputs
    if start in correct:
        verification = str(input("Please enter your username: "))       # verification used as it allows authorised users in
        if verification.lower() in user:
            opendata()
            print("#######")
            time.sleep(3)
            print("Beginning production")
            time.sleep(3)
            production(verification)
        else:
            print("Username not recognised, closing terminal")
    else:
        print("Production cycle cancelled")
        

# function for the main part of task to make a conveyor

def production(verification, max_hours = 8):            # verification used as it pertains to user credentials
   
    randomset = {1,2,3,4,5}                             # randomset used as this set needs to recreate the production of a conveyor belt
    total_hours = 0                                     # total_hours used because it has to track through whole program
    max_product = 100                                   # max_product used because this sets the limit of product
    hourly_product = 0                                  # hourly_product used because it tracks the product produced every hour
    total_product = 0                                   # total_product used as tracks all product not just hourly, won"t get reset
    hours = 0                                           # hours variable simulates if an hour had passed
    maintenance_product = 0                             # this variable was called this because this tracks just between maintenance and will reset

    for hours in range(max_hours-1):
        for minutes in range(61):
            hourly_product += random.randrange(0, len(randomset))
            if hourly_product >= max_product:
                break
        total_product+=hourly_product
        maintenance_product+=hourly_product            
        total_hours+=1
        hourly_product = 0
        cycle = (f"\nService required {hours+1}hrs reached\nTotal products since last maintenance by {verification}: {maintenance_product}")
        if hours == 2:
            maintenance(cycle,maintenance_product)
            del maintenance_product
            maintenance_product = 0
        elif hours == 5:
            maintenance(cycle,maintenance_product)
            del maintenance_product
            maintenance_product = 0

    end_day = (f"The total hours the system ran yesterday: {total_hours+1}\nTotal products produced yesterday: {total_product}")

    storedata(end_day)

    print(f"Day ended")
    print(f"Total products produced today by {verification}: {total_product}")
    time.sleep(10)
    quit()



# function to perform the "maintenance" cycle

def maintenance(cycle, maintenance_product):
    
    print(cycle)
    time.sleep(10)


begin_production()
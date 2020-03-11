#import hotel
from hotel import *

a = Hotel()

def main():
    while(1):
        try:
            print("1. Add a Hotel. ")
            print("2. Room with Items. ")
            print("3. Customer room budget. ")
            print("4. Show the total cost. ")
            print("5. Exit. ""\n")
            b = int(input("Enter the choice: ""\n"))
            if(b==1):
                a.gethotelname()
            elif(b==2):
                a.room_with_items()
            elif(b==3):
                cust_budget = int(input("Enter customer budget in USD($): ""\n"))
                if cust_budget >= 300:
                    a.customer_budget_room(cust_budget)
                else:
                    print("No rooms available in the USD($)", cust_budget ,"given customer budget.\n")
            elif(b==4):
                a.display()
            elif(b==5):
                quit()
            else:
                ("Please enter the valid option.""\n")
        except(ValueError):
            print("Please enter the valid option.""\n")
main()
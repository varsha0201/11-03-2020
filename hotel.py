import random
class Hotel:
    def __init__(self, hotel_name='', room='', s=0, rt='', rno=random.randint(101,501), t=0, item1=''):
        
        self.hotel_name = hotel_name
        self.room = room
        self.s = s
        self.rt = rt
        self.rno = rno
        self.t = t
        self.item1 = item1
        self.grandtotal = 0
        self.room_1 = "Option 1. Room type A--> USD($) 600 PN/-\n"
        self.room_2 = "Option 2. Room type B--> USD($) 500 PN/-\n"
        self.room_3 = "Option 3. Room type C--> USD($) 400 PN/-\n"
        self.room_4 = "Option 4. Room type D--> USD($) 300 PN/-\n"


    def gethotelname(self):
        self.hotel_name = input("\nEnter the Hotel name:")
        print("Your room no:",self.rno,"\n")


    def roomrent(self):
        print("Please select from the below room options.")
        print(self.room_1+"\n"+self.room_2+"\n"+self.room_3+"\n"+self.room_4)


        x = int(input("Please, Enter your option:"))
        n = int(input("For How many nights did you stay:"))
        try:
            if(x==1):
                print("You have opted room type A")
                self.s = 600*n
            
            elif(x==2):
                print("You have opted room type B")
                self.s = 500*n
            
            elif(x==3):
                print("You have opted room type C")
                self.s = 400*n

            elif (x==4):
                print("You have opted room type D")
                self.s = 300*n

            else:
                print("Please choose a room:")
        except(ValueError):
            print("Please choose a room:")

        
        print("Your room rent is = USD($)",self.s,"\n")



    def room_with_items(self):
        print("You can custumize the items with room selection:""\n")
        print("************* Provide items with rooms ***********************""\n")
        print("1. TV --> 10$""\n""2. couch --> 15$""\n""3. table--> 5$""\n""4. A/C --> 15$""\n""5. Bed--> 20$""\n""6.Exit")
        while(1):
            try:
                i = int(input("Enter your choice:"))
                if (i==1):
                    f=int(input("Enter the quantity:"))
                    self.t=self.t+10*f

                elif (i==2):
                    f=int(input("Enter the quantity:"))
                    self.t = self.t+15*f
                
                elif (i==3):
                    f=int(input("Enter the quantity:"))
                    self.t = self.t+5*f

                elif(i==4):
                    f = int(input("Enter the quantity:"))
                    self.t = self.t+15*f
                
                elif(i==5):
                    f = int(input("Enter the quantity:"))
                    print(f)
                    self.t = self.t+20*f
                elif(i==6):
                    break;
                else:
                    print("Invalid option.")
            except(ValueError):
                print("Invalid option.")
        print("Total Items Cost = USD($)",self.t,"\n")
        


    def display(self):
        print("************** Hotel Bill **************")
        print("Details")
        print("Hotel name:", self.hotel_name)
        print("Room no.", self.rno)
        print("Room rent Details:", self.s)
        print("Room Item bill is:", self.t)

        self.rt=self.s+self.t
        self.grandtotal = self.rt
        print ("Your grandtotal bill is:",self.grandtotal,"\n")
        self.rno+=1

    def customer_budget_room(self, cust_budget):
        try:
            customer_budget = cust_budget
            if(customer_budget >= 300 and customer_budget < 400):
                print("Following are the rooms available in given customer budget:""\n")
                print(self.room_4)
                self.roomrent()
            elif(customer_budget >= 400 and customer_budget < 500):
                print("Following are the rooms available in given customer budget:""\n")
                print(self.room_3)
                print(self.room_4)
                self.roomrent()
            elif(customer_budget >= 500 and customer_budget <600):
                print("Following are the rooms available in given customer budget:""\n")
                print(self.room_2)
                print(self.room_3)
                print(self.room_4)
                self.roomrent()
            elif(customer_budget >= 600):
                print("Following are the rooms available in given customer budget:""\n")
                print(self.room_1)
                print(self.room_2)
                print(self.room_3)
                print(self.room_4)
                self.roomrent()
            else:
                print("All the rooms are available in customer budget.""\n")    
        except(ValueError):
             print("All the rooms are available in customer budget.""\n")  






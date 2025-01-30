#Improvements I can make: Create new list for every truck.
# Maybe make new file to compare data and remove data from one if they have same data?
# Remove need to pop bloat data (This can be done through individualizing the inputs instead of using terms[x] to cycle through prompts)
import sys
from datetime import datetime
import time
class Trucks():
    def __init__(self):
        self.init = print("hello world")

    def update(self): #for fun
            
        while True:
            time.sleep(1)
            self.time = datetime.now()
            print(self.time)
            self.file.write(str(f"{self.time}\n"))
            self.file.close()
            
    def datainput(self): 
        x = 0
        self.List = []

        while True: #To create loop :D
            x +=1 # Used as means of providing a value to x so that self.terms[x] can be cycled through
            self.terms = {1:"Carrier: ", 2:"Truck Number: ", 3:"Trailer Number: ", 4:"Truck Exited: "}
            self.exiting = input("Press Q if Trailer is Leaving and E if trailer is entering or P to pop Bloated, or D for additional Data: ").lower() #An I/O system I use to divide I/O for trailers
            
            self.time = datetime.now()# Gay porn
            print(self.List)

#Fix Quitting
            if self.exiting == "q":
                self.ParsedData = (str(self.List).replace("'","").replace("[","").replace("]",""))                   
                self.removedtruck = input(f"What Truck Left?{self.List}: ")
                with open("data2.txt", "a+") as self.file: #Allows you to open file without having to worry about closing the file
                    self.file.write(str(f"{self.terms[4]} {self.ParsedData} left at: {self.time}]\n"))

                if self.removedtruck in self.List: #Checks to see if Truck Number Matches any number in the list. If Yes, it will remove that number from the list.
                    self.List.remove(self.removedtruck)
                    print(self.removedtruck, ": Has been removed")
                    difftrail = input("Does the driver have a new Trailer?: ")
                    if difftrail.lower() == "y":
                        newtrail = input("Input New Trailer: ")
                        self.List.append(newtrail)
                        with open("data2.txt", "a+") as file:
                            file.write("New Trailer: ")
                            file.write(str(newtrail))
                            file.write(f" Driver {self.ParsedData} left in new Trailer at {self.time}\n")
                            newtrailinput = input("Is this a load? YES/N: ").upper
                            if newtrailinput == 'YES':
                                self.U2 = input("Input Trailer Number: ").upper()
                                self.U3 = input("Input Load Type: ").upper()
                                self.U4 = input("Input Seal, or 0 if no seal: ").upper()
                                self.U5 = input ("PO Number: ")
                                self.nList.append(self.U1)
                                self.nList.append(self.U2)
                                self.nList.append(self.U3)
                                self.nList.append(self.U4)
                                self.nList.append(self.U5)
                                with open("data2","a+") as file:
                                    file.write("This is the updated information for the leaving Driver: ")
                                    file.write(f"{self.nList} left at {self.time}\n")
                                    self.nList == []
                            if newtrailinput == "NO":
                                
                                continue

                    if difftrail.lower() == "n" or "no":
                        continue
                print(self.List,": Currently Active Trailers") 


            if self.exiting == "e":
                        for x in range(1,2): #Cycles through all terms in dict for easier text assignment for inputs.
                            self.data = input(f"Enter Truck Number: ") # Passes info to Data, data passes to List for appendaging.
                            self.List.append(self.data)
                        self.ParsedData = (str(self.List).replace("'","").replace("[","").replace("]","").replace(",", " ")) # Cleans the data so it looks nicer in output
                        print(self.ParsedData[2])

            if self.exiting == "p":
                        try:
                            self.List.pop(0)
                            print("Item has been popped!")
                        except:
                            print("No More items to pop!")
                            continue
            if self.exiting == "d":
                    self.nList = []
                    self.U1 = input("Input Carrier: ").upper()
                    self.U2 = input("Input Trailer Number: ").upper()
                    self.U3 = input("Input Load Type: ").upper()
                    self.U4 = input("Input Seal, or 0 if no seal: ").upper()
                    self.U5 = input ("PO Number: ")
                    if self.data in self.List:
                        self.nList.append(self.data)
                        self.nList.append(self.U1)
                        self.nList.append(self.U2)
                        self.nList.append(self.U3)
                        self.nList.append(self.U4)
                        self.nList.append(self.U5)

                        self.parsedata2 = (str(self.nList).replace("'","").replace("[","").replace("]","")," ")
                        with open("data2.txt", "a+") as self.file:    
                            self.file.write(str(f"[Truck: {self.parsedata2} Entered at: {self.time}\n"))  

                        with open("data2.txt", "a+") as file:
                            file.write(str(self.parsedata2))
                        self.nList == []
                    print(str(self.parsedata2))

                    if self.data not in self.nList:
                        print("There's currently no new data!")
                        self.nList == []

    
while True:
    TruckData = Trucks()
    TruckData.datainput()
#----------
#Program Name: Week 8 Portfolio Project
#Author: Adene Shigute
#Date: April 4, 2021
#Program Objective: Compile Vehicles as Inventory for Dealership
#--------------------------------------------------------------------------
#Pseudocode: 1. Request number choice for inventory
#            2. Validate questions
#               a. Respected questions must be answered
#            3. Main Method
#               a. Initialize requested number
#               b. Accept number
#               c. Display inventory questions
#               d. Display respected ending statement
#-------------------------------------------------------------------------
#Program Inputs: Enter chosen number for compiling inventory
#Program Outputs: Vehicle inventory for dealership
#-------------------------------------------------------------------------
print ("Vehicle Inventory for Dealership")

#automobile class
class automobile:
   #constructor
   def __init__(self, make="", model="", color="", year=0, mileage=0):
      self.make = make
      self.model = model
      self.color = color
      self.year = year
      self.mileage = mileage

   #setter methods
   def set_make(self, make):
      self.make = make
   def set_model(self, model):
      self.model = model
   def set_color(self, color):
      self.color = color
   def set_year(self, year):
      self.year = year
   def set_mileage(self, mileage):
      self.mileage = mileage

   #getter methods
   def get_make(self):
      return self.make
   def get_model(self):
      return self.model
   def get_color(self):
      return self.color
   def get_year(self):
      return self.year
   def get_mileage(self):
      return self.mileage
#end of automobile class
      
#method to add a new vehicle to the inventory
def add_vehicle(v_list):
  make = input("Enter make: ")
  model = input("Enter model: ")
  color = input("Enter color: ")
  year = int(input("Enter year: "))
  mileage = int(input("Enter mileage: "))
  v = automobile(make, model, color, year, mileage)
  v_list.append(v)
  print("Added successfully")


#method to remove a vehicle from the inventory
def remove_vehicle(v_list):
  index = int(input("Enter the index number of vehicle to be removed: "))
  if index >= 0 and index < len(v_list):
    make = v_list[index].get_make()
    model = v_list[index].get_model()
    v_list.pop(index)
    print(make, model, "Has been removed from the inventory")
  else:
    print("Invalid index")

#method to update a vehicle info in the inventory
def update_vehicle(v_list):
  index = int(input("Enter the index number of the vehicle to be updated: "))
  if index >= 0 and index < len(v_list):
    make = input("Enter new make: ")
    model = input("Enter new model: ")
    color = input("Enter new color: ")
    year = int(input("Enter new year: "))
    mileage = int(input("Enter new mileage: "))
    v_list[index].set_make(make)
    v_list[index].set_model(model)
    v_list[index].set_color(color)
    v_list[index].set_year(year)
    v_list[index].set_mileage(mileage)
    print("Updated successfully")
  else:
    print("Invalid index")

#method to print all vehicle details in proper formatted order
def display_vehicles(v_list):
  print('{:10} {:10} {:10} {:10} {:10} {:10}'.format('Index#', 'MAKE', 'MODEL', 'COLOR', 'YEAR', 'MILEAGE'))
  for i in range(len(v_list)):
    v = v_list[i]
    print('{:10} {:10} {:10} {:10} {:10} {:10}'.format(str(i), v.get_make(), v.get_model(), v.get_color(),str(v.get_year()), str(v.get_mileage())))
v_list = []  # initial list

#looping infinitely
while True:
  #showing menu
  print("1. Add vehicle")
  print("2. Delete vehicle")
  print("3. Update vehicle")
  print("4. Display vehicles")
  print("5. Finish")
  #getting choice
  ch = int(input("Please enter your number choice to continue: "))
  #performing actions based on choice
  if ch == 1:
    add_vehicle(v_list)
  elif ch == 2:
    remove_vehicle(v_list)
  elif ch == 3:
    update_vehicle(v_list)
  elif ch == 4:
    display_vehicles(v_list)
  elif ch == 5:
    #end of the program
    break;
  else:
    print("Invalid choice")

print("End of Program")



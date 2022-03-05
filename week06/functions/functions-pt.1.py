# Write a function that prints out a menu of commands we can perform, ie add,
# View and quit. The function should return what the user chose.
# Author: Ben Janning



def displayMenu():
 print("What would you like to do?")
 print("\t(a) Add new student")
 print("\t(v) View students")
 print("\t(q) Quit")
 choice = input("Type one letter (a/v/q):").strip()
 return choice
#test the function
choice = displayMenu()
print("you chose {}".format(choice))



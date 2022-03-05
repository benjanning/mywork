# With the program we made last week, create a new menu item called save. When
# the user selects the doSave() function should be called (the do save can do
# nothing but printout doSave for the moment

#Author: Ben Janning

def doLoad () :
    return readDict () 

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()
    return choice
def doAdd():
 # we fill this in later
    print("in adding")
def doView():
 # we fill this in later
    print("in viewing")

#main program
choice = displayMenu()
while(choice != 'q'):
 # we could do this with lamda functions
 # I am keeping this basic for the moment
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice !='q':
        print("\n\nplease select either a,v or q")
    choice=displayMenu() 

writeDict (students)
print ("students saved")
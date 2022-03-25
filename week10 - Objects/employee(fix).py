
# Author: Ben Janning

# Write a class called Employee (in employee.py), that has one attribute called
# timesheets ( set to an empty list) and an __init__ function that takes in a first and
# last name.

class Employee:
    timesheets = []
    
    def __init__ (self, first, last) :
        self.first = first
        self.last = last
        
# write a __str__ function that returns the full name

def __str__ (self) :
    return self.first + ' ' + self.last

    
# write a testcase.

if __name__ == '__main__':
    test = Employee ('some', 'one')
    print (test)
    assert ('some' , 'one' == str(test))
    
# Create a Function in Code
# Write a function in the class Employee called logminutes(project, minutes), the
# function will create a Timesheetentry with the project and minutes and the time
# being now (it probably should be now minus minutes), and append it to the list

from timesheetentry import *
import datetime as dt

def logminutes (self, project, minutes) :
    now = dt.datetime.now
    timesheetentry = Timesheetentry (project, now, minutes)
    self.timesheets.append (timesheetentry)
    

# Write a function called gettotaltime() that will return the total minutes of all the
# timesheetentrys

def gettotaltime (self) :
    total_minutes = 0
    for ts in self.timesheets:
        total_minutes += ts.duration
    return total_minutes

# Write a test case for this.
if __name__ == '__main__':
    test = Employee ('some', 'one')
    print (test)
    assert ( 'some', 'one' == str (test))
    test.logminutes ('pl', 30)
    test.logminutes ('pl', 60)
    mins = test.gettotaltime ()
    print (mins)
    assert ( mins == 90 )
    
    print ('all good')

# Program that Read in the student’s name, 
# Reads in the module names and grades,
# Author: Ben Janning

students = []
def readModules():
    return []
def doAdd(students):
    currentStudent = {}
    currentStudent["name"]=input("enter name :")
    currentStudent["modules"]= readModules()
    students.append(currentStudent)

#test
doAdd(students)
doAdd(students)
print (students)
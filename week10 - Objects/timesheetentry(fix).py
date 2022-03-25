# Labs for Objects - Week 10. Using Class,  __init__ function.
# Author: Ben Janning

class Timesheetentry:
    
    def __init__ (self, project, start, duration):
        self.project = project
        self.start = start
        self.duration = duration
        
    # Write a __str__ function for this class that returns the project and the duration
    
    def __str__ (self) :
        return self.project + ' : ' + str(self.duration)
    
    # Write a test case for this class that creates an instance and prints it out
    
    import datetime as dt 
    
    # class code
    
    if __name__ == '__main__' :
        ts = dt.datetime (2021, 3, 19, 16, 20)
        test = Timesheetentry ('test', ts , 60)
        print (test)
        
    
                        
    
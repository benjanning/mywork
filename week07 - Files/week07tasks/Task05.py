# Write a function that will read in a dict object from file. 
# Author: Ben Janning

import json
filename = "testdict.json"

def readDict ():
# this will throw an error if the file does not exist
# it should readly just throw an empty dict
# we can do this later

    with open (filename) as f :
        return json.load (f)

# test the function

somedict = readDict ()

print (somedict)
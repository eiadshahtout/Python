#Deletes a file you specify!
import os

file = input("What's the filename to delete? ")
location = input("Where is it located? ")

path = os.path.join(location,file)
os.remove(path)

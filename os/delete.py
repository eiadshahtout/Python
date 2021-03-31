import os

file = "deleteme.txt"
location = "/Users/mshahtout/Documents/Programming"

path = os.path.join(location,file)

os.remove(path)
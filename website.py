current_users = ["a","b","c","d","e"]
new_users = ["a","b","y","x","z"]

for user in new_users:
    if user in current_users:
        print("Enter a new username please")
    else:
        print("The username is avaliable!")
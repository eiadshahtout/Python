usernames = ["Eiad","Yousef","Admin"]

if usernames:
    for username in usernames:
        if username == "Admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in")
else:
    print("We need to find some users")
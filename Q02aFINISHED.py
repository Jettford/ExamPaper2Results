# Q02a

# Initialise variables

# Print prompts, take and check input from user

username = "bard423" # test username
password = "nX2934?" # test password

while True:
    inputUsername = input("What is your username?") # enter username and password
    inputPassword = input("What is your password?")
    
    if inputUsername == username and inputPassword == password: # check login
        break
    else:
        print("Incorrect username or password")
        continue
        
# end of execution
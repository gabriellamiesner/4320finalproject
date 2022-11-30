def validate_user(username, password):  # Username and password are passed in from the user's entries in routes.py
    file = open("passcodes.txt", "r")
    file_data = file.readlines()    # Pull user data from the file
    file.close()
    valid_user = False
    for line in file_data:
        user_info = line.split(",") # Create list with username and password for the line. Index 0 is username, index 1 is password.
        # Evaluate if the user credentials provided fit one of the saved admin logins
        if username == user_info[0] and password.strip() == user_info[1].strip():   # Strip function is placed here because it didn't work when implemented on previous line 
            valid_user = True
            break
    return valid_user
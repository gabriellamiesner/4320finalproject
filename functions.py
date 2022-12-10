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

def generate_seating_chart():
    seat_chart = initialize_seat_chart()

    file = open("reservations.txt", "r")
    file_data = file.readlines()    # Pull user data from the file
    file.close()
    
    reserved_seats = []
    # for line in file_data:
    #     reservation_record = line.split((","))
    #     seat_row = int(seat_record[1])
    #     seat_col = int(seat_record[2])
    #     seat_record = [seat_row, seat_col]
    #     reserved_seats.append(seat_record)
    # for row in range(11):
    #     seats_in_row = []
    #     reserved = False
    #     for col in range(3):

    return seat_chart

def initialize_seat_chart():
    seat_chart = []
    for row in range(11):
        seat_chart.append(['O', 'O', 'O', 'O'])
    return seat_chart

# def format_seat_chart(seat_chart):
#     seat_string = ""
#     for row in seat_chart:
#         seat_string += str(row) + '\n'
#     return seat_string
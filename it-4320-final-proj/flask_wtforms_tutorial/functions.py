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
    for line in file_data:
        reservation_record = line.split((","))
        seat_row = int(reservation_record[1])
        seat_col = int(reservation_record[2])
        seat_chart[seat_row][seat_col] = 'X'

    return seat_chart

def initialize_seat_chart():
    seat_chart = []
    for row in range(11):
        seat_chart.append(['O', 'O', 'O', 'O'])
    return seat_chart

# From project instructions
def get_cost_matrix():
    cost_matrix = [[100, 75, 50, 100] for row in range(12)]
    return cost_matrix

def calculate_total_flight_sales():
    cost_matrix = get_cost_matrix()
    seating_chart = generate_seating_chart()
    total_cost = 0
    row_index = 0
    for row in seating_chart:
        col_index = 0
        for col in row:
            if seating_chart[row_index][col_index] == 'X':
                total_cost += cost_matrix[row_index][col_index]
            col_index += 1
        row_index += 1
    return total_cost

def generate_reservation_code(fname):
    reservation_code = ""
    code_string = 'INFOTC1040'
    num_of_letters = 0
    if len(fname) >= len(code_string):
        num_of_letters = len(fname)
    else:
        num_of_letters = len(code_string)
    for letter in range(num_of_letters - 1):
        try:
            reservation_code += fname[letter] + code_string[letter]
            fname = fname[1:]
            code_string = code_string[1:]
        except:
            continue
    reservation_code += fname + code_string
    return reservation_code

def save_reservation(fname, lname, row, seat):
    reservation_code = generate_reservation_code(fname)
    file = open("reservations.txt", "a")
    reservation = f"{fname}, {int(row) - 1}, {int(seat) - 1}, {reservation_code}"
    file.write('\n' + reservation)
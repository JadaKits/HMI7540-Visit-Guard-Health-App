# ==========================================
# Case Management Appointment System
# Name: NICOLE PABLO FLORES
# ==========================================

case_managers = [
    "Case Manager Brown",
    "Case Manager Davis",
    "Case Manager Wilson"
]

# available appointment times
time_slots = [
    "9AM",
    "10AM",
    "11AM",
    "1PM",
    "2PM",
    "3PM"
]


# -------------------------------
# Validating the name
#and it will contain only letters
# minimum 3 characters for the name
# loops until valid input from user
# -------------------------------
def get_name():

    while True:

        name = input(
            "\nPlease enter your full name: "
        ).strip()

        # remove spaces for checking
        check_name = name.replace(" ", "")

        # minimum length
        if len(check_name) < 3:
            print(
                "Name must contain at least "
                "3 letters."
            )
            continue

        # letters only
        if not check_name.isalpha():
            print(
                "Name can only contain letters."
            )
            continue

        return name.title()


# -------------------------------
# DOB VALIDATION
# accepts both types of formats :
#11221999 AND  11/22/1999
# loops until there is a valid entry 
# -------------------------------
def get_dob():

    while True:

        dob = input(
            "Enter DOB "
            "(MMDDYYYY or MM/DD/YYYY): "
        ).strip()

        # remove slashes
        clean_dob = dob.replace("/", "")

        # must equal 8 digits
        if len(clean_dob) != 8:
            print(
                "DOB must contain 8 numbers."
            )
            continue

        # numbers only for DOB
        if not clean_dob.isdigit():
            print(
                "DOB must contain only numbers."
            )
            continue

        month = int(clean_dob[0:2])
        day = int(clean_dob[2:4])
        year = int(clean_dob[4:8])

        # validating month
        if month < 1 or month > 12:
            print("Invalid month.")
            continue

        # validate day
        if day < 1 or day > 31:
            print("Invalid day.")
            continue

        # validate year
        if year < 1900 or year > 2026:
            print("Invalid year.")
            continue

        # format DOB
        formatted_dob = (
            clean_dob[0:2] + "/" +
            clean_dob[2:4] + "/" +
            clean_dob[4:8]
        )

        return formatted_dob


# -------------------------------
# Getting patient  to enter in data
# -------------------------------
def get_patient():

    name = get_name()

    dob = get_dob()

    return name, dob


# -------------------------------
# Choosing the case manager
# -------------------------------
def choose_case_manager():

    print("\nAvailable Case Managers:")

    for i in range(len(case_managers)):
        print(i + 1, "-", case_managers[i])

    while True:

        choice = input(
            "Select a case manager "
            "by number: "
        ).strip()

        if choice.isdigit():

            choice = int(choice)

            if (
                1 <= choice <=
                len(case_managers)
            ):
                return case_managers[
                    choice - 1
                ]

        print("Invalid selection.")


# -------------------------------
# Time slot it is selecting
# will also prevent double booking
# removes booked times once selected
# -------------------------------
def choose_time():

    global time_slots

    while True:

        # if no times left
        if time_slots == []:
            print(
                "No appointments available."
            )
            return None

        print(
            "\nAvailable Time Slots:",
            time_slots
        )

        choice = input(
            "Choose a time exactly "
            "as shown: "
        ).strip().upper()

        # valid choice
        if choice in time_slots:

            # REMOVE BOOKED SLOT
            time_slots.remove(choice)

            return choice

        print(
            "That time is not available."
        )


# -------------------------------
# Randomized conformation codes
# no imports used
# -------------------------------
def generate_code(
    name,
    dob,
    time
):

    text = name + dob + time

    number_string = ""

    # convert letters to ASCII values
    for char in text:
        number_string += str(ord(char))

    # reverse numbers
    reversed_numbers = (
        number_string[::-1]
    )

    # take every other character
    mixed = reversed_numbers[::2]

    # final confirmation code
    code = "CM-" + mixed[:6]

    return code


# -------------------------------
# Saves appointment to file
# -------------------------------
def save_appointment(
    name,
    dob,
    manager,
    time,
    code
):

    try:

        file = open(
            "appointments.txt",
            "a"
        )

        file.write(
            name + "," +
            dob + "," +
            manager + "," +
            time + "," +
            code + "\n"
        )

        file.close()

    except:
        print(
            "Error saving appointment."
        )


# -------------------------------
# Confirming appointment
# -------------------------------
def confirm(
    name,
    dob,
    manager,
    time
):

    global time_slots

    print(
        "\nPlease confirm "
        "your appointment:"
    )

    print("Name:", name)
    print("DOB:", dob)
    print("Case Manager:", manager)
    print("Time:", time)

    while True:

        answer = input(
            "\nIs this information "
            "correct? (yes/no): "
        ).lower()

        # CONFIRMED
        if answer == "yes":

            code = generate_code(
                name,
                dob,
                time
            )

            print(
                "\nThank you,",
                name + "!"
            )

            print(
                "Your appointment has "
                "been booked with",
                manager
            )

            print(
                "Appointment Time:",
                time
            )

            print(
                "Confirmation Number:",
                code
            )

            save_appointment(
                name,
                dob,
                manager,
                time,
                code
            )

            break

        # CANCELLED
        elif answer == "no":

            # put time back if cancelled
            time_slots.append(time)

            print(
                "Appointment cancelled."
            )

            break

        else:
            print(
                "Please enter yes or no."
            )


# -------------------------------
# MAIN PROGRAM LOOP
# -------------------------------
print(
    "Welcome NICOLE PABLO FLORES "
    "- Case Management "
    "Appointment System"
)

while True:

    # patient info
    name, dob = get_patient()

    # choose manager
    manager = choose_case_manager()

    # choose time
    time = choose_time()

    if time is None:
        break

    # confirm booking
    confirm(
        name,
        dob,
        manager,
        time
    )

    # continue loop
    while True:

        again = input(
            "\nWould you like to "
            "book another appointment? "
            "(yes/no): "
        ).lower()

        if again == "yes":
            break

        elif again == "no":
            print("Thank you for scheduling with us today!")
            quit()

        else:
            print(
                "Please enter yes or no."
            )


# ========================================================
# VisitGuard Health
# Case Management Appointment System
# ========================================================

case_managers = [
    "Case Manager Brown",
    "Case Manager Davis",
    "Case Manager Wilson"
]

# preset appointments
appointments = [
    "05/15/2026 - 8AM",
    "05/15/2026 - 11AM",
    "05/15/2026 - 4PM",
]


# -------------------------------
# NAME VALIDATION
# -------------------------------
def get_name():

    while True:

        name = input(
            "\nEnter full name: "
        ).strip()

        # remove spaces
        check_name = name.replace(
            " ",
            ""
        )

        # minimum length
        if len(check_name) < 3:

            print(
                "Name must contain "
                "at least 3 letters."
            )

            continue

        # letters only
        if not check_name.isalpha():

            print(
                "Name can only "
                "contain letters."
            )

            continue

        return name.title()


# -------------------------------
# DOB VALIDATION
# accepts:
# MMDDYYYY
# MM/DD/YYYY
# -------------------------------
def get_dob():

    while True:

        dob = input(
            "Enter DOB "
            "(MM/DD/YYYY): "
        ).strip()

        # remove slashes
        clean_dob = dob.replace(
            "/",
            ""
        )

        # must equal 8 digits
        if len(clean_dob) != 8:

            print(
                "DOB must contain "
                "8 numbers."
            )

            continue

        # numbers only
        if not clean_dob.isdigit():

            print(
                "DOB must contain "
                "only numbers."
            )

            continue

        month = int(clean_dob[0:2])
        day = int(clean_dob[2:4])
        year = int(clean_dob[4:8])

        # validate month
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
# CHOOSE CASE MANAGER
# -------------------------------
def choose_case_manager():

    print("\nAvailable Case Managers:")

    for i in range(
        len(case_managers)
    ):

        print(
            i + 1,
            "-",
            case_managers[i]
        )

    while True:

        choice = input(
            "Select manager number: "
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
# CHOOSE APPOINTMENT
# prevents double booking
# remembers appointments
# -------------------------------
def choose_appointment():

    booked_appointments = []

    # read booked appointments
    try:

        file = open(
            "appointments.txt",
            "r"
        )

        for line in file:

            data = line.strip().split(",")

            # appointment stored at index 3
            booked_appointments.append(
                data[3]
            )

        file.close()

    except:
        pass

    available_appointments = []

    # remove booked appointments
    for appt in appointments:

        if appt not in booked_appointments:

            available_appointments.append(
                appt
            )

    # no appointments left
    if available_appointments == []:

        print(
            "No appointments available."
        )

        return None

    print(
        "\nAvailable Appointments:"
    )

    for i in range(
        len(available_appointments)
    ):

        print(
            i + 1,
            "-",
            available_appointments[i]
        )

    while True:

        choice = input(
            "Select appointment number: "
        ).strip()

        if choice.isdigit():

            choice = int(choice)

            if (
                1 <= choice <=
                len(available_appointments)
            ):

                return available_appointments[
                    choice - 1
                ]

        print("Invalid selection.")


# -------------------------------
# GENERATE CONFIRMATION CODE
# -------------------------------
def generate_code(
    name,
    dob,
    appointment
):

    text = (
        name +
        dob +
        appointment
    )

    number_string = ""

    # convert characters to ASCII
    for char in text:

        number_string += str(
            ord(char)
        )

    # reverse numbers
    reversed_numbers = (
        number_string[::-1]
    )

    # take every other character
    mixed = reversed_numbers[::2]

    # final code
    code = "CM-" + mixed[:6]

    return code


# -------------------------------
# SAVE APPOINTMENT
# -------------------------------
def save_appointment(
    name,
    dob,
    manager,
    appointment,
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
            appointment + "," +
            code + "\n"
        )

        file.close()

    except:

        print(
            "Now saving appointment."
        )


# -------------------------------
# CONFIRM APPOINTMENT
# -------------------------------
def confirm(
    name,
    dob,
    manager,
    appointment
):

    print(
        "\nAppointment Summary"
    )

    print("Name:", name)
    print("DOB:", dob)
    print("Case Manager:", manager)
    print(
        "Appointment:",
        appointment
    )

    while True:

        answer = input(
            "\nConfirm appointment? "
            "(yes/no): "
        ).lower()

        # confirmed
        if answer == "yes":

            code = generate_code(
                name,
                dob,
                appointment
            )

            save_appointment(
                name,
                dob,
                manager,
                appointment,
                code
            )

            print(
                "\nAppointment booked!"
            )

            print(
                "Confirmation Number:",
                code
            )

            print(
                "\nThank you for choosing "
                "VisitGuard Health!"
            )

            quit()

        # cancelled
        elif answer == "no":

            print(
                "Appointment cancelled."
            )

            quit()

        else:

            print(
                "Please enter yes or no."
            )


# ========================================================
# MAIN PROGRAM
# ========================================================

print(
    "Welcome to "
    "VisitGuard Health"
)

while True:

    # patient info
    name = get_name()

    dob = get_dob()

    # choose manager
    manager = choose_case_manager()

    # choose appointment
    appointment = choose_appointment()

    if appointment is None:

        break

    # confirm appointment
    confirm(
        name,
        dob,
        manager,
        appointment
    )

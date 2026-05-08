
# ========================================================
# VisitGuard Health
# Appointment Scheduling System
# ========================================================

case_managers = [
    "Case Manager Brown",
    "Case Manager Davis",
    "Case Manager Wilson"
]

# preset appointment dates ( we can switch if needed)
appointment_dates = [
    "05/15/2026",
    "05/16/2026",
    "05/17/2026"
]

# preset appointment times
time_slots = [
    "9AM",
    "10AM",
    "11AM",
    "1PM",
    "2PM",
    "3PM"
]


# -------------------------------
# Name validiation
# it needs more than 3 letters 
# its only alpha 
# -------------------------------
def get_name():

    while True:

        name = input(
            "\nEnter full name: "
        ).strip()

        check_name = name.replace(
            " ",
            ""
        )

        if len(check_name) < 3:

            print(
                "Name must contain "
                "at least 3 letters."
            )

            continue

        if not check_name.isalpha():

            print(
                "Name can only "
                "contain letters."
            )

            continue

        return name.title()


# -------------------------------
# DOB that accepts both formats
# -------------------------------
def get_dob():

    while True:

        dob = input(
            "Enter DOB "
            "(MM/DD/YYYY): "
        ).strip()

        clean_dob = dob.replace(
            "/",
            ""
        )

        if len(clean_dob) != 8:

            print(
                "DOB must contain "
                "8 numbers."
            )

            continue

        if not clean_dob.isdigit():

            print(
                "DOB must contain "
                "only numbers."
            )

            continue

        month = int(clean_dob[0:2])
        day = int(clean_dob[2:4])
        year = int(clean_dob[4:8])

        if month < 1 or month > 12:

            print("Invalid month.")

            continue

        if day < 1 or day > 31:

            print("Invalid day.")

            continue

        if year < 1900 or year > 2026:

            print("Invalid year.")

            continue

        formatted_dob = (
            clean_dob[0:2] + "/" +
            clean_dob[2:4] + "/" +
            clean_dob[4:8]
        )

        return formatted_dob


# -------------------------------
# Case manager picking
# -------------------------------
def choose_case_manager():

    print("\nCase Managers:")

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
# Choosing day
# -------------------------------
def choose_date():

    print("\nAvailable Dates:")

    for i in range(
        len(appointment_dates)
    ):

        print(
            i + 1,
            "-",
            appointment_dates[i]
        )

    while True:

        choice = input(
            "Select date number: "
        ).strip()

        if choice.isdigit():

            choice = int(choice)

            if (
                1 <= choice <=
                len(appointment_dates)
            ):

                return appointment_dates[
                    choice - 1
                ]

        print("Invalid selection.")


# -------------------------------
# Choosing time
# 
# -------------------------------
def choose_time(date):

    booked_times = []

    # read booked appointments
    try:

        file = open(
            "appointments.txt",
            "r"
        )

        for line in file:

            data = line.strip().split(",")

            booked_date = data[3]
            booked_time = data[4]

            if booked_date == date:

                booked_times.append(
                    booked_time
                )

        file.close()

    except:
        pass

    available_times = []

    for time in time_slots:

        if time not in booked_times:

            available_times.append(
                time
            )

    # no times left
    if available_times == []:

        print(
            "No appointments available "
            "for this date."
        )

        return None

    print("\nAvailable Times:")

    for i in range(
        len(available_times)
    ):

        print(
            i + 1,
            "-",
            available_times[i]
        )

    while True:

        choice = input(
            "Select time number: "
        ).strip()

        if choice.isdigit():

            choice = int(choice)

            if (
                1 <= choice <=
                len(available_times)
            ):

                return available_times[
                    choice - 1
                ]

        print("Invalid selection.")


# -------------------------------
# confirming code
# -------------------------------
def generate_code(
    name,
    dob,
    time
):

    text = name + dob + time

    number_string = ""

    for char in text:

        number_string += str(
            ord(char)
        )

    reversed_numbers = (
        number_string[::-1]
    )

    mixed = reversed_numbers[::2]

    code = "CM-" + mixed[:6]

    return code


# -------------------------------
# Saving appt
# -------------------------------
def save_appointment(
    name,
    dob,
    manager,
    date,
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
            date + "," +
            time + "," +
            code + "\n"
        )

        file.close()

    except:

        print(
            " Now saving appointment."
        )


# -------------------------------
# Confiming appt
# -------------------------------
def confirm(
    name,
    dob,
    manager,
    date,
    time
):

    print(
        "\nAppointment Summary"
    )

    print("Name:", name)
    print("DOB:", dob)
    print("Case Manager:", manager)
    print("Date:", date)
    print("Time:", time)

    while True:

        answer = input(
            "\nConfirm appointment? "
            "(yes/no): "
        ).lower()

        if answer == "yes":

            code = generate_code(
                name,
                dob,
                time
            )

            save_appointment(
                name,
                dob,
                manager,
                date,
                time,
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

    # manager
    manager = choose_case_manager()

    # appointment date
    date = choose_date()

    # appointment time
    time = choose_time(date)

    if time is None:

        break

    # confirmation
    confirm(
        name,
        dob,
        manager,
        date,
        time
    )

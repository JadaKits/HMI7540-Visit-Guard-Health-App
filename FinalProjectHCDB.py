import os

# Save file in a safe writable location (user home folder)
FILE_PATH = os.path.expanduser("~/appointments.txt")


# ========================================================
# VisitGuard Health
# SCHEDULING APPOINTMENT SYSTEM
# ========================================================

case_managers = [
    "Case Manager Brown",
    "Case Manager Davis",
    "Case Manager Wilson"
]

appointments = [
    "05/15/2026 - 9AM",
    "05/15/2026 - 10AM",
    "05/15/2026 - 11AM",
]


# -------------------------------
# NAME VALIDATION FOR PERSON
# HAS TO BE MORE THAN 3 LETTERS
#ONLY LETTERS
# -------------------------------
def get_name():

    while True:

        name = input("\nEnter full name: ").strip()
        check_name = name.replace(" ", "")

        if len(check_name) < 3:
            print("Name must be at least 3 letters.")
            continue

        if not check_name.isalpha():
            print("Name can only contain letters.")
            continue

        return name.title()


# -------------------------------
# DOB VALIDATION PICKS EITHER 11111999 \ 11/11/1999
# -------------------------------
def get_dob():

    while True:

        dob = input("Enter DOB (MM/DD/YYYY or MMDDYYYY): ").strip()
        clean = dob.replace("/", "")

        if len(clean) != 8 or not clean.isdigit():
            print("Invalid DOB format.")
            continue

        month = int(clean[0:2])
        day = int(clean[2:4])
        year = int(clean[4:8])

        if month < 1 or month > 12:
            print("Invalid month.")
            continue

        if day < 1 or day > 31:
            print("Invalid day.")
            continue

        if year < 1900 or year > 2026:
            print("Invalid year.")
            continue

        return f"{clean[0:2]}/{clean[2:4]}/{clean[4:8]}"


# -------------------------------
# CASE MANAGER  CHOOSING WHICH ONE
# -------------------------------
def choose_case_manager():

    print("\nAvailable Case Managers:")

    for i, cm in enumerate(case_managers):
        print(i + 1, "-", cm)

    while True:

        choice = input("Select manager number: ").strip()

        if choice.isdigit():
            choice = int(choice)

            if 1 <= choice <= len(case_managers):
                return case_managers[choice - 1]

        print("Invalid selection.")


# -------------------------------
# APPOINTMENTS FOR THE PATIENTS    
# -------------------------------
def choose_appointment():

    booked = []

    # safely read file
    if os.path.exists(FILE_PATH):

        with open(FILE_PATH, "r") as file:
            for line in file:
                parts = line.strip().split(",")

                if len(parts) >= 4:
                    booked.append(parts[3])

    available = [a for a in appointments if a not in booked]

    if not available:
        print("No appointments available.")
        return None

    print("\nAvailable Appointments:")

    for i, appt in enumerate(available):
        print(i + 1, "-", appt)

    while True:

        choice = input("Select appointment number: ").strip()

        if choice.isdigit():

            choice = int(choice)

            if 1 <= choice <= len(available):
                return available[choice - 1]

        print("Invalid selection.")


# -------------------------------
# CONFIRMATION CODE FOR THE CLIENT
# -------------------------------
def generate_code(name, dob, appointment):

    text = name + dob + appointment
    numbers = ""

    for c in text:
        numbers += str(ord(c))

    reversed_nums = numbers[::-1]
    mixed = reversed_nums[::2]

    return "CM-" + mixed[:6]


# -------------------------------
# SAVE APPOINTMENT FOR CLIENT
# -------------------------------
def save_appointment(name, dob, manager, appointment, code):

    with open(FILE_PATH, "a") as file:
        file.write(
            name + "," +
            dob + "," +
            manager + "," +
            appointment + "," +
            code + "\n"
        )


# -------------------------------
# CONFIRMATION OF THE APPT
# -------------------------------
def confirm(name, dob, manager, appointment):

    print("\nAppointment Summary")
    print("Name:", name)
    print("DOB:", dob)
    print("Case Manager:", manager)
    print("Appointment:", appointment)

    while True:

        answer = input("\nConfirm appointment? (yes/no): ").lower()

        if answer == "yes":

            code = generate_code(name, dob, appointment)
            save_appointment(name, dob, manager, appointment, code)

            print("\nAppointment booked!")
            print("Confirmation Number:", code)

            quit()

        elif answer == "no":

            print("Cancelled.")
            quit()

        else:
            print("Enter yes or no.")


# -------------------------------
# MAIN
# -------------------------------
print("Welcome to VisitGuard Health")

while True:

    name = get_name()
    dob = get_dob()
    manager = choose_case_manager()
    appointment = choose_appointment()

    if appointment is None:
        break

    confirm(name, dob, manager, appointment)

# Hospital Management System

## Project Overview

The **Hospital Management System** is a beginner-friendly, menu-driven Python project developed to manage different types of hospital records. The system provides separate modules for patients, doctors, appointments, medicines, rooms, payments, staff, emergency cases, and other hospital-related information.

The project demonstrates basic Python programming concepts such as **functions, loops, conditional statements, lists, modules, user input, and CRUD operations**.

## Features

- Appointment Management
- Blood Bank Management
- Security Camera Management
- Canteen Management
- Cleaning Staff Management
- Death Record Management
- Doctor Management
- Emergency Management
- Guard Management
- Insurance Management
- Intern Management
- Medicine Stock Management
- Patient Management
- Room Management
- Payment Management

### CRUD Operations

The management modules provide basic operations such as:

- **Insert** – Add a new record
- **View** – Display existing records
- **Update** – Modify an existing record
- **Delete** – Remove an existing record

## Technologies / Tools Used

- **Python**
- **Visual Studio Code (VS Code)**
- Python Lists
- Python Functions
- Conditional Statements
- Loops
- Modules
- Console / Terminal

**No external Python packages are required.**

## Project Structure

```text
class Project/
│
├── 1.MAIN_PAGE.py
├── appointment_info.py
├── bloodbank_info.py
├── camera_info.py
├── canteen_info.py
├── cleaningstaff_info.py
├── death_record_info.py
├── doctor_info.py
├── emergency.py
├── guard_info.py
├── insurance_info.py
├── interns_info.py
├── medicine_stock.py
├── pateint_info.py
├── payment_info.py
└── rooms_info.py
```

`1.MAIN_PAGE.py` is the main program from which the different hospital management modules can be accessed.

## Installation and Run Instructions

### Step 1: Install Python

Install **Python 3** on your computer if it is not already installed.

### Step 2: Download / Extract the Project

Download the project and extract the ZIP file.

### Step 3: Open in VS Code

Open the extracted **class Project** folder in Visual Studio Code.

### Step 4: Open Terminal

In VS Code, select:

**Terminal → New Terminal**

### Step 5: Run the Project

Run the following command:

```bash
python "1.MAIN_PAGE.py"
```

If `python` does not work, try:

```bash
python3 "1.MAIN_PAGE.py"
```

## How to Use

After running the program, the main dashboard displays different hospital management options.

Example:

```text
1. Appointment
2. Blood Bank
3. Security Camera
4. Canteen
5. Cleaning Staff
6. Death Record
7. Doctor
8. Emergency
9. Guard
10. Insurance
11. Interns
12. Medicine Stock
13. Patient
14. Rooms
15. Payment
```

Select the required option by entering its number.

Inside a module, select the required operation such as **Insert, View, Update, or Delete** and follow the instructions displayed on the screen.

## Testing Instructions

The project can be tested using the following steps.

### Test 1: Insert Record

1. Open any management module.
2. Select the Insert option.
3. Enter valid information.
4. Check that the record is added successfully.

### Test 2: View Record

1. Select the View option.
2. Check whether the inserted record is displayed correctly.

### Test 3: Update Record

1. Select the Update option.
2. Enter the ID of an existing record.
3. Enter the new information.
4. View the record again and verify the changes.

### Test 4: Delete Record

1. Select the Delete option.
2. Enter the ID of an existing record.
3. Check that the record is removed.

### Test 5: Invalid ID

Enter an ID that does not exist while updating or deleting a record. The program should indicate that the record was not found.

### Test 6: Navigation

Open different modules from the main dashboard and return to the dashboard to verify that navigation works correctly.

## Screenshots

Screenshots can be added to this section for the final submission.

Recommended screenshots:

1. Main Dashboard
2. Patient Management
3. Doctor Management
4. Appointment Management
5. Medicine Stock Management
6. Room Management
7. Payment Management
8. Insert / View / Update / Delete operation

## Limitations

- Records are stored temporarily in Python lists.
- Data is lost when the program is closed.
- The project is currently console-based.
- There is no permanent database connection in this version.
- Advanced authentication is not included.

## Future Improvements

The project can be improved by adding:

- MySQL or another database
- Permanent data storage
- Login and authentication
- Graphical User Interface (GUI)
- Search functionality
- Better input validation
- Automatic billing
- Report generation
- Improved error handling

## Author

**Varinder Aggarwal**

**Branch:** Computer Science and Engineering (CSE-CORE)

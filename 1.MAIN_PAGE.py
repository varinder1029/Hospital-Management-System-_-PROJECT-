print("=" * 70)
print("              WELCOME TO HOSPITAL MANAGEMENT SYSTEM")
print("=" * 70)
print("This is a simple hospital management system that allows you to manage various aspects of a hospital ")
print("✦ Appointments")
print("✦ Blood Bank")
print("✦ Security Cameras")
print("✦ Canteen")
print("✦ Cleaning Staff")
print("✦ Death Records")
print("✦ Doctors")
print("✦ Emergency Cases")
print("✦ Guards")
print("✦ Insurance Records")
print("✦ Interns")
print("✦ Medicine Stock")
print("✦ Patients")
print("✦ Rooms")
print("✦ Payments")
from appointment_info import *
from bloodbank_info import *
from camera_info import *
from canteen_info import *
from cleaningstaff_info import *
from death_record_info import *
from doctor_info import *
from emergency import *
from guard_info import *
from insurance_info import *
from interns_info import *
from medicine_stock import *
from pateint_info import *
from rooms_info import *
from payment_info import *
while True:
    print("=" * 70)
    print("           DASHBOARD - HOSPITAL MANAGEMENT SYSTEM")
    print("=" * 70)
    print("  1. Appointment       6. Death Record       11. Interns")
    print("  2. Blood Bank        7. Doctor             12. Medicine Stock")
    print("  3. Security Camera   8. Emergency          13. Patient")
    print("  4. Canteen           9. Guard              14. Rooms")
    print("  5. Cleaning Staff    10.Insurance          15. Payment")
    print("=" * 70)
    choice = int(input("\nEnter your choice (1-15): ")) 
    if choice == 1:
        appointment_info()
    elif choice == 2:
        bloodbank_info()
    elif choice == 3:
        camera_info()
    elif choice == 4:
        canteen_info()
    elif choice == 5:
        cleaningstaff_info()
    elif choice == 6:
        death_record_info()
    elif choice == 7:
        doctor_info()
    elif choice == 8:
        emergency_info()
    elif choice == 9:
        guard_info()
    elif choice == 10:
        insurance_info()
    elif choice == 11:
        interns_info()
    elif choice == 12:
        medicine_stock()
    elif choice == 13:
        patient_info()
    elif choice == 14:
        rooms_info()
    elif choice == 15:
        payment_info()
    else:
        print("Invalid choice. Please enter a number between 1 and 15.")
    print("\nDo you want to go back to the Dashboard?")
    answer = input("Enter Yes or No: ")
    if answer.lower() == "no":
        print("=" * 70)
        print("\nThank you for using Hospital Management System. Goodbye!")
        print("Developed by: Varinder Aggarwal")
        print()
        print("=" * 70)
        break
    elif answer.lower() == "yes":
        continue
    else:
        print("\nSORRY,DID NOT CATCH THAT,EXITING ANYWAY.")
        break
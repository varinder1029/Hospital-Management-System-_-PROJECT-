doctors = []
def doctor_info():
    while True:
        print("\n----- DOCTOR MANAGEMENT -----")
        print("1. Insert Data")
        print("2. View Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            doctor_id = int(input("Enter Doctor ID: "))
            name = input("Enter Doctor Name: ")
            specialization = input("Enter Specialization: ")
            experience = int(input("Enter Experience in Years: "))
            consultation_fee = int(input("Enter Consultation Fee: "))
            data = [doctor_id, name, specialization, experience, consultation_fee]
            doctors.append(data)
            print("Doctor saved.")
        elif choice == 2:
            if len(doctors) == 0:
                print("No doctors on file yet.")
            else:
                for data in doctors:
                    print("\nDoctor ID:", data[0])
                    print("Doctor Name:", data[1])
                    print("Specialization:", data[2])
                    print("Experience in Years:", data[3])
                    print("Consultation Fee:", data[4])
        elif choice == 3:
            doctor_id = int(input("Enter Doctor ID to update: "))
            found = False
            for data in doctors:
                if data[0] == doctor_id:
                    data[1] = input("Enter New Doctor Name: ")
                    data[2] = input("Enter New Specialization: ")
                    data[3] = int(input("Enter New Experience in Years: "))
                    data[4] = int(input("Enter New Consultation Fee: "))
                    print("Doctor details updated.")
                    found = True
                    break
            if not found:
                print("No doctor with that ID.")
        elif choice == 4:
            doctor_id = int(input("Enter Doctor ID to delete: "))
            found = False
            for data in doctors:
                if data[0] == doctor_id:
                    doctors.remove(data)
                    print("Doctor removed from records.")
                    found = True
                    break
            if not found:
                print("No doctor with that ID.")
        elif choice == 5:
            break
        else:
            print("Invalid choice.")

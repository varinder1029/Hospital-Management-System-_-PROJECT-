insurance_records = []
def insurance_info():
    while True:
        print("\n----- INSURANCE MANAGEMENT -----")
        print("1. Insert Data")
        print("2. View Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. Back")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number.")
            continue
        if choice == 1:
            insurance_id = int(input("Enter Insurance ID: "))
            patient_id = int(input("Enter Patient ID: "))
            company = input("Enter Insurance Company: ")
            policy_number = int(input("Enter Policy Number: "))
            amount = int(input("Enter Insurance Amount: "))
            pay = [insurance_id, patient_id, company, policy_number, amount]
            insurance_records.append(pay)
            print("Insurance details saved.")
        elif choice == 2:
            if len(insurance_records) == 0:
                print("No insurance records yet.")
            else:
                for pay in insurance_records:
                    print("\nInsurance ID:", pay[0])
                    print("Patient ID:", pay[1])
                    print("Insurance Company:", pay[2])
                    print("Policy Number:", pay[3])
                    print("Insurance Amount:", pay[4])
        elif choice == 3:
            insurance_id = int(input("Enter Insurance ID to update: "))
            found = False
            for pay in insurance_records:
                if pay[0] == insurance_id:
                    pay[1] = int(input("Enter New Patient ID: "))
                    pay[2] = input("Enter New Insurance Company: ")
                    pay[3] = int(input("Enter New Policy Number: "))
                    pay[4] = int(input("Enter New Insurance Amount: "))
                    print("Insurance details updated.")
                    found = True
                    break
            if not found:
                    print("Couldn't find that insurance record.")
        elif choice == 4:
            insurance_id = int(input("Enter Insurance ID to delete: "))
            found = False
            for pay in insurance_records:
                if pay[0] == insurance_id:
                    insurance_records.remove(pay)
                    print("Insurance record deleted.")
                    found = True
                    break
            if not found:
                    print("Couldn't find that insurance record.")
        elif choice == 5:
            break
        else:
            print("Invalid choice.")

death_records = []
def death_record_info():
    while True:
        print("\n----- DEATH RECORD MANAGEMENT -----")
        print("1. Insert Data")
        print("2. View Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            record_id = int(input("Enter Record ID: "))
            patient_id = int(input("Enter Patient ID: "))
            patient_name = input("Enter Patient Name: ")
            age = int(input("Enter Patient Age: "))
            date = input("Enter Date: ")
            policy = [record_id, patient_id, patient_name, age, date]
            death_records.append(policy)
            print("Death record saved.")
        elif choice == 2:
            if len(death_records) == 0:
                print("No death records stored.")
            else:
                for policy in death_records:
                    print(f"\nRecord ID: {policy[0]}")
                    print(f"Patient ID: {policy[1]}")
                    print(f"Patient Name: {policy[2]}")
                    print(f"Patient Age: {policy[3]}")
                    print(f"Date: {policy[4]}")
        elif choice == 3:
            record_id = int(input("Enter Record ID to update: "))
            found = False
            for policy in death_records:
                if policy[0] == record_id:
                    policy[1] = int(input("Enter New Patient ID: "))
                    policy[2] = input("Enter New Patient Name: ")
                    policy[3] = int(input("Enter New Patient Age: "))
                    policy[4] = input("Enter New Date: ")
                    print("Death record updated.")
                    found = True
                    break
            if not found:
                    print("No record found with that ID.")
        elif choice == 4:
            record_id = int(input("Enter Record ID to delete: "))
            found = False
            for policy in death_records:
                if policy[0] == record_id:
                    death_records.remove(policy)
                    print("Death record deleted.")
                    found = True
                    break
            if not found:
                    print("No record found with that ID.")
        elif choice == 5:
            break
        else:
            print("Invalid choice.")

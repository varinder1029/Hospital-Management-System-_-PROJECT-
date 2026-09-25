bloodbank = []
def bloodbank_info():
    while True:
        print("\n----- BLOOD BANK MANAGEMENT -----")
        print("1. Insert Data")
        print("2. View Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            blood_id = int(input("Enter Blood ID: "))
            blood_group = input("Enter Blood Group: ")
            units = int(input("Enter Number of Units: "))
            donor_id = int(input("Enter Donor ID: "))
            expiry_days = int(input("Enter Expiry Days: "))
            rec = [blood_id, blood_group, units, donor_id, expiry_days]
            bloodbank.append(rec)
            print("Blood entry added.")
        elif choice == 2:
            if len(bloodbank) == 0:
                print("No units in the blood bank yet.")
            else:
                for rec in bloodbank:
                    print("\nBlood ID:", rec[0])
                    print("Blood Group:", rec[1])
                    print("Number of Units:", rec[2])
                    print("Donor ID:", rec[3])
                    print("Expiry Days:", rec[4])
        elif choice == 3:
            blood_id = int(input("Enter Blood ID to update: "))
            found = False
            for rec in bloodbank:
                if rec[0] == blood_id:
                    rec[1] = input("Enter New Blood Group: ")
                    rec[2] = int(input("Enter New Number of Units: "))
                    rec[3] = int(input("Enter New Donor ID: "))
                    rec[4] = int(input("Enter New Expiry Days: "))
                    print("Blood entry updated.")
                    found = True
                    break
            if not found:
                print("No blood entry with that ID.")
        elif choice == 4:
            blood_id = int(input("Enter Blood ID to delete: "))
            found = False
            for rec in bloodbank:
                if rec[0] == blood_id:
                    bloodbank.remove(rec)
                    print("Blood entry removed.")
                    found = True
                    break
            if not found:
                print("No blood entry with that ID.")
        elif choice == 5:
            break
        else:
            print("Invalid choice.")

medicines = []
def medicine_stock():
    while True:
        print("\n----- MEDICINE STOCK MANAGEMENT -----")
        print("1. Insert Data")
        print("2. View Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            medicine_id = int(input("Enter Medicine ID: "))
            name = input("Enter Medicine Name: ")
            quantity = int(input("Enter Quantity: "))
            price = int(input("Enter Price: "))
            expiry_year = int(input("Enter Expiry Year: "))
            appt = [medicine_id, name, quantity, price, expiry_year]
            medicines.append(appt)
            print("Medicine added to stock.")
        elif choice == 2:
            if len(medicines) == 0:
                print("No medicines in stock yet.")
            else:
                for appt in medicines:
                    print("\nMedicine ID:", appt[0])
                    print("Medicine Name:", appt[1])
                    print("Quantity:", appt[2])
                    print("Price:", appt[3])
                    print("Expiry Year:", appt[4])
        elif choice == 3:
            medicine_id = int(input("Enter Medicine ID to update: "))
            found = False
            for appt in medicines:
                if appt[0] == medicine_id:
                    appt[1] = input("Enter New Medicine Name: ")
                    appt[2] = int(input("Enter New Quantity: "))
                    appt[3] = int(input("Enter New Price: "))
                    appt[4] = int(input("Enter New Expiry Year: "))
                    print("Stock details updated.")
                    found = True
                    break
            if not found:
                print("No medicine with that ID.")
        elif choice == 4:
            medicine_id = int(input("Enter Medicine ID to delete: "))
            found = False
            for appt in medicines:
                if appt[0] == medicine_id:
                    medicines.remove(appt)
                    print("Medicine removed from stock.")
                    found = True
                    break
            if not found:
                print("No medicine with that ID.")
        elif choice == 5:
            break
        else:
            print("Invalid choice.")

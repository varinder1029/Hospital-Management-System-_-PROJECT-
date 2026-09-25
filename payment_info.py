payments = []
def payment_info():
    while True:
        print("\n----- PAYMENT MANAGEMENT -----")
        print("1. Insert Data")
        print("2. View Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            payment_id = int(input("Enter Payment ID: "))
            patient_id = int(input("Enter Patient ID: "))
            patient_name = input("Enter Patient Name: ")
            amount = int(input("Enter Payment Amount: "))
            payment_method = input("Enter Payment Method: ")
            cam = [payment_id, patient_id, patient_name, amount, payment_method]
            payments.append(cam)
            print("Payment recorded.")
        elif choice == 2:
            if len(payments) == 0:
                print("No payments recorded yet.")
            else:
                for cam in payments:
                    print(f"\nPayment ID: {cam[0]}")
                    print(f"Patient ID: {cam[1]}")
                    print(f"Patient Name: {cam[2]}")
                    print(f"Payment Amount: {cam[3]}")
                    print(f"Payment Method: {cam[4]}")
        elif choice == 3:
            payment_id = int(input("Enter Payment ID to update: "))
            found = False
            for cam in payments:
                if cam[0] == payment_id:
                    cam[1] = int(input("Enter New Patient ID: "))
                    cam[2] = input("Enter New Patient Name: ")
                    cam[3] = int(input("Enter New Payment Amount: "))
                    cam[4] = input("Enter New Payment Method: ")
                    print("Payment details updated.")
                    found = True
                    break
            if not found:
                print("No payment with that ID.")
        elif choice == 4:
            payment_id = int(input("Enter Payment ID to delete: "))
            found = False
            for cam in payments:
                if cam[0] == payment_id:
                    payments.remove(cam)
                    print("Payment record deleted.")
                    found = True
                    break
            if not found:
                print("No payment with that ID.")
        elif choice == 5:
            break
        else:
            print("Invalid choice.")

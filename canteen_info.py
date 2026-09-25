canteen = []
def canteen_info():
    while True:
        print("\n----- CANTEEN MANAGEMENT -----")
        print("1. Insert Data")
        print("2. View Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            item_id = int(input("Enter Item ID: "))
            item_name = input("Enter Item Name: ")
            quantity = int(input("Enter Quantity: "))
            price = int(input("Enter Price: "))
            staff_name = input("Enter Staff Name: ")
            case = [item_id, item_name, quantity, price, staff_name]
            canteen.append(case)
            print("Item added to the canteen list.")
        elif choice == 2:
            if len(canteen) == 0:
                print("Canteen list is empty right now.")
            else:
                for case in canteen:
                    print("\nItem ID:", case[0])
                    print("Item Name:", case[1])
                    print("Quantity:", case[2])
                    print("Price:", case[3])
                    print("Staff Name:", case[4])
        elif choice == 3:
            item_id = int(input("Enter Item ID to update: "))
            found = False
            for case in canteen:
                if case[0] == item_id:
                    case[1] = input("Enter New Item Name: ")
                    case[2] = int(input("Enter New Quantity: "))
                    case[3] = int(input("Enter New Price: "))
                    case[4] = input("Enter New Staff Name: ")
                    print("Canteen item updated.")
                    found = True
                    break
            if not found:
                print("No item with that ID.")
        elif choice == 4:
            item_id = int(input("Enter Item ID to delete: "))
            found = False
            for case in canteen:
                if case[0] == item_id:
                    canteen.remove(case)
                    print("Item removed from the canteen list.")
                    found = True
                    break
            if not found:
                print("No item with that ID.")
        elif choice == 5:
            break
        else:
            print("Invalid choice.")

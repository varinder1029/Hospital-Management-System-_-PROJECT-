guards = []
def guard_info():
    while True:
        print("\n----- GUARD MANAGEMENT -----")
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
            guard_id = int(input("Enter Guard ID: "))
            name = input("Enter Guard Name: ")
            age = int(input("Enter Age: "))
            shift_hours = int(input("Enter Shift Hours: "))
            salary = int(input("Enter Salary: "))
            p = [guard_id, name, age, shift_hours, salary]
            guards.append(p)
            print("Guard saved.")
        elif choice == 2:
            if len(guards) == 0:
                print("No guards registered yet.")
            else:
                for p in guards:
                    print(f"\nGuard ID: {p[0]}")
                    print(f"Guard Name: {p[1]}")
                    print(f"Age: {p[2]}")
                    print(f"Shift Hours: {p[3]}")
                    print(f"Salary: {p[4]}")
        elif choice == 3:
            guard_id = int(input("Enter Guard ID to update: "))
            found = False
            for p in guards:
                if p[0] == guard_id:
                    p[1] = input("Enter New Guard Name: ")
                    p[2] = int(input("Enter New Age: "))
                    p[3] = int(input("Enter New Shift Hours: "))
                    p[4] = int(input("Enter New Salary: "))
                    print("Guard details updated.")
                    found = True
                    break
            if not found:
                print("No guard with that ID.")
        elif choice == 4:
            guard_id = int(input("Enter Guard ID to delete: "))
            found = False
            for p in guards:
                if p[0] == guard_id:
                    guards.remove(p)
                    print("Guard removed.")
                    found = True
                    break
            if not found:
                print("No guard with that ID.")
        elif choice == 5:
            break
        else:
            print("Invalid choice.")

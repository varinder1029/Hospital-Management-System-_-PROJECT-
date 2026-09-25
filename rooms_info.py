rooms = []
def rooms_info():
    while True:
        print("\n----- ROOM MANAGEMENT -----")
        print("1. Insert Data")
        print("2. View Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            room_id = int(input("Enter Room ID: "))
            room_number = int(input("Enter Room Number: "))
            room_type = input("Enter Room Type: ")
            patient_id = int(input("Enter Patient ID: "))
            charges = int(input("Enter Room Charges: "))
            data = [room_id, room_number, room_type, patient_id, charges]
            rooms.append(data)
            print("Room saved.")
        elif choice == 2:
            if len(rooms) == 0:
                print("No rooms allocated yet.")
            else:
                for data in rooms:
                    print("\nRoom ID:", data[0])
                    print("Room Number:", data[1])
                    print("Room Type:", data[2])
                    print("Patient ID:", data[3])
                    print("Room Charges:", data[4])
        elif choice == 3:
            room_id = int(input("Enter Room ID to update: "))
            found = False
            for data in rooms:
                if data[0] == room_id:
                    data[1] = int(input("Enter New Room Number: "))
                    data[2] = input("Enter New Room Type: ")
                    data[3] = int(input("Enter New Patient ID: "))
                    data[4] = int(input("Enter New Room Charges: "))
                    print("Room details updated.")
                    found = True
                    break
            if not found:
                print("No room with that ID.")
        elif choice == 4:
            room_id = int(input("Enter Room ID to delete: "))
            found = False
            for data in rooms:
                if data[0] == room_id:
                    rooms.remove(data)
                    print("Room record deleted.")
                    found = True
                    break
            if not found:
                print("No room with that ID.")
        elif choice == 5:
            break
        else:
            print("Invalid choice.")

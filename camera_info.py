cameras = []
def camera_info():
    while True:
        print("\n----- SECURITY CAMERA MANAGEMENT -----")
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
            camera_id = int(input("Enter Camera ID: "))
            location = input("Enter Camera Location: ")
            camera_type = input("Enter Camera Type: ")
            working_hours = int(input("Enter Working Hours: "))
            status = input("Enter Camera Status: ")
            doc = [camera_id, location, camera_type, working_hours, status]
            cameras.append(doc)
            print("Camera saved.")
        elif choice == 2:
            if len(cameras) == 0:
                print("No cameras registered yet.")
            else:
                for doc in cameras:
                    print(f"\nCamera ID: {doc[0]}")
                    print(f"Camera Location: {doc[1]}")
                    print(f"Camera Type: {doc[2]}")
                    print(f"Working Hours: {doc[3]}")
                    print(f"Camera Status: {doc[4]}")
        elif choice == 3:
            camera_id = int(input("Enter Camera ID to update: "))
            found = False
            for doc in cameras:
                if doc[0] == camera_id:
                    doc[1] = input("Enter New Camera Location: ")
                    doc[2] = input("Enter New Camera Type: ")
                    doc[3] = int(input("Enter New Working Hours: "))
                    doc[4] = input("Enter New Camera Status: ")
                    print("Camera details updated.")
                    found = True
                    break
            if not found:
                print("No camera with that ID.")
        elif choice == 4:
            camera_id = int(input("Enter Camera ID to delete: "))
            found = False
            for doc in cameras:
                if doc[0] == camera_id:
                    cameras.remove(doc)
                    print("Camera removed.")
                    found = True
                    break
            if not found:
                print("No camera with that ID.")
        elif choice == 5:
            break
        else:
            print("Invalid choice.")

emergencies = []
def emergency_info():
    while True:
        print('\n----- EMERGENCY MANAGEMENT -----')
        print('1. Insert Data')
        print('2. View Data')
        print('3. Update Data')
        print('4. Delete Data')
        print('5. Back')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            emergency_id = int(input('Enter Emergency ID: '))
            patient_id = int(input('Enter Patient ID: '))
            patient_name = input('Enter Patient Name: ')
            emergency_type = input('Enter Emergency Type: ')
            doctor_id = int(input('Enter Doctor ID: '))
            med = [emergency_id, patient_id, patient_name, emergency_type, doctor_id]
            emergencies.append(med)
            print('Emergency case logged.')
        elif choice == 2:
            if len(emergencies) == 0:
                print('No emergency cases logged yet.')
            else:
                for med in emergencies:
                    print('\nEmergency ID:', med[0])
                    print('Patient ID:', med[1])
                    print('Patient Name:', med[2])
                    print('Emergency Type:', med[3])
                    print('Doctor ID:', med[4])
        elif choice == 3:
            emergency_id = int(input('Enter Emergency ID to update: '))
            found = False
            for med in emergencies:
                if med[0] == emergency_id:
                    med[1] = int(input('Enter New Patient ID: '))
                    med[2] = input('Enter New Patient Name: ')
                    med[3] = input('Enter New Emergency Type: ')
                    med[4] = int(input('Enter New Doctor ID: '))
                    print('Emergency case updated.')
                    found = True
                    break

            if not found:
                print("No emergency case with that ID.")
        elif choice == 4:
            emergency_id = int(input('Enter Emergency ID to delete: '))
            found = False
            for med in emergencies:
                if med[0] == emergency_id:
                    emergencies.remove(med)
                    print('Emergency case removed.')
                    found = True
                    break

            if not found:
                print("No emergency case with that ID.")
        elif choice == 5:
            break
        else:
            print('Invalid choice.')

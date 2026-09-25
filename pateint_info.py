patients = []
def patient_info():
    while True:
        print('\n===== PATIENT MANAGEMENT =====')
        print('1. Insert Data')
        print('2. View Data')
        print('3. Update Data')
        print('4. Delete Data')
        print('5. Back')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            patient_id = int(input('Enter Patient ID: '))
            name = input('Enter Patient Name: ')
            age = int(input('Enter Patient Age: '))
            gender = input('Enter Gender: ')
            disease = input('Enter Disease: ')
            entry = [patient_id, name, age, gender, disease]
            patients.append(entry)
            print('Got it, patient saved.')
        elif choice == 2:
            if len(patients) == 0:
                print('No patient records yet.')
            else:
                for entry in patients:
                    print('\nPatient ID:', entry[0])
                    print('Patient Name:', entry[1])
                    print('Patient Age:', entry[2])
                    print('Gender:', entry[3])
                    print('Disease:', entry[4])
        elif choice == 3:
            patient_id = int(input('Enter Patient ID to update: '))
            found = False
            for entry in patients:
                if entry[0] == patient_id:
                    entry[1] = input('Enter New Patient Name: ')
                    entry[2] = int(input('Enter New Patient Age: '))
                    entry[3] = input('Enter New Gender: ')
                    entry[4] = input('Enter New Disease: ')
                    print('Patient record updated.')
                    found = True
                    break

            if not found:
                print("Couldn't find that patient ID.")
        elif choice == 4:
            patient_id = int(input('Enter Patient ID to delete: '))
            found = False
            for entry in patients:
                if entry[0] == patient_id:
                    patients.remove(entry)
                    print('Patient record deleted.')
                    found = True
                    break

            if not found:
                print("Couldn't find that patient ID.")
        elif choice == 5:
            break
        else:
            print('Invalid choice.')

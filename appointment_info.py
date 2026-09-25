appointments = []
def appointment_info():
    while True:
        print('\n----- APPOINTMENT MANAGEMENT -----')
        print('1. Insert Data')
        print('2. View Data')
        print('3. Update Data')
        print('4. Delete Data')
        print('5. Back')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            appointment_id = int(input('Enter Appointment ID: '))
            patient_id = int(input('Enter Patient ID: '))
            doctor_id = int(input('Enter Doctor ID: '))
            date = input('Enter Appointment Date: ')
            time = input('Enter Appointment Time: ')
            staff = [appointment_id, patient_id, doctor_id, date, time]
            appointments.append(staff)
            print('Appointment booked.')
        elif choice == 2:
            if len(appointments) == 0:
                print('No appointments booked yet.')
            else:
                for staff in appointments:
                    print('\nAppointment ID:', staff[0])
                    print('Patient ID:', staff[1])
                    print('Doctor ID:', staff[2])
                    print('Appointment Date:', staff[3])
                    print('Appointment Time:', staff[4])
        elif choice == 3:
            appointment_id = int(input('Enter Appointment ID to update: '))
            found = False
            for staff in appointments:
                if staff[0] == appointment_id:
                    staff[1] = int(input('Enter New Patient ID: '))
                    staff[2] = int(input('Enter New Doctor ID: '))
                    staff[3] = input('Enter New Appointment Date: ')
                    staff[4] = input('Enter New Appointment Time: ')
                    print('Appointment details updated.')
                    found = True
                    break
            if not found:
                print("Couldn't find that appointment.")
        elif choice == 4:
            appointment_id = int(input('Enter Appointment ID to delete: '))
            found = False
            for staff in appointments:
                if staff[0] == appointment_id:
                    appointments.remove(staff)
                    print('Appointment cancelled.')
                    found = True
                    break
            if not found:
                print("Couldn't find that appointment.")
        elif choice == 5:
            break
        else:
            print('Invalid choice.')

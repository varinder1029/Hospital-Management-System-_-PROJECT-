cleaningstaff = []
def cleaningstaff_info():
    while True:
        print('\n***** CLEANING STAFF MANAGEMENT *****')
        print('1. Insert Data')
        print('2. View Data')
        print('3. Update Data')
        print('4. Delete Data')
        print('5. Back')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            staff_id = int(input('Enter Staff ID: '))
            name = input('Enter Staff Name: ')
            area = input('Enter Cleaning Area: ')
            hours = int(input('Enter Working Hours: '))
            salary = int(input('Enter Salary: '))
            g = [staff_id, name, area, hours, salary]
            cleaningstaff.append(g)
            print('Cleaning staff member added.')
        elif choice == 2:
            if len(cleaningstaff) == 0:
                print('No cleaning staff records yet.')
            else:
                for g in cleaningstaff:
                    print('\nStaff ID:', g[0])
                    print('Staff Name:', g[1])
                    print('Cleaning Area:', g[2])
                    print('Working Hours:', g[3])
                    print('Salary:', g[4])
        elif choice == 3:
            staff_id = int(input('Enter Staff ID to update: '))
            found = False
            for g in cleaningstaff:
                if g[0] == staff_id:
                    g[1] = input('Enter New Staff Name: ')
                    g[2] = input('Enter New Cleaning Area: ')
                    g[3] = int(input('Enter New Working Hours: '))
                    g[4] = int(input('Enter New Salary: '))
                    print('Cleaning staff details updated.')
                    found = True
                    break
            if not found:
                print('No staff member with that ID.')
        elif choice == 4:
            staff_id = int(input('Enter Staff ID to delete: '))
            found = False
            for g in cleaningstaff:
                if g[0] == staff_id:
                    cleaningstaff.remove(g)
                    print('Cleaning staff member removed.')
                    found = True
                    break
            if not found:
                print('No staff member with that ID.')
        elif choice == 5:
            break
        else:
            print('Invalid choice.')

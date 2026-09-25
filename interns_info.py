interns = []
def interns_info():
    while True:
        print('\n----- INTERN MANAGEMENT -----')
        print('1. Insert Data')
        print('2. View Data')
        print('3. Update Data')
        print('4. Delete Data')
        print('5. Back')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            intern_id = int(input('Enter Intern ID: '))
            name = input('Enter Intern Name: ')
            department = input('Enter Department: ')
            duration = int(input('Enter Internship Duration in Months: '))
            stipend = int(input('Enter Stipend: '))
            rm = [intern_id, name, department, duration, stipend]
            interns.append(rm)
            print('Intern added.')
        elif choice == 2:
            if len(interns) == 0:
                print('No interns added yet.')
            else:
                for rm in interns:
                    print('\nIntern ID:', rm[0])
                    print('Intern Name:', rm[1])
                    print('Department:', rm[2])
                    print('Internship Duration in Months:', rm[3])
                    print('Stipend:', rm[4])
        elif choice == 3:
            intern_id = int(input('Enter Intern ID to update: '))
            found = False
            for rm in interns:
                if rm[0] == intern_id:
                    rm[1] = input('Enter New Intern Name: ')
                    rm[2] = input('Enter New Department: ')
                    rm[3] = int(input('Enter New Internship Duration in Months: '))
                    rm[4] = int(input('Enter New Stipend: '))
                    print('Intern details updated.')
                    found = True
                    break
            if not found:
                print('No intern with that ID.')
        elif choice == 4:
            intern_id = int(input('Enter Intern ID to delete: '))
            found = False
            for rm in interns:
                if rm[0] == intern_id:
                    interns.remove(rm)
                    print('Intern removed.')
                    found = True
                    break
            if not found:
                print('No intern with that ID.')
        elif choice == 5:
            break
        else:
            print('Invalid choice.')

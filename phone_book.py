import csv

# phonebook = {'Kieran': {'name': 'Kieran','number': 8456331959,'phrase': 'Good code is not written, it\'s re-written.'},'Lambda': {'name': 'Lambda','number': 8454185633, 'phrase': 'I am a robot.'}}
running = True

def make_decision():
    making_decision = True
    while making_decision:
        try:
            query = int(input('Enter 1 to create contact, 2 to search phonebook, 3 to update contact, or 6 to quit: '))
        except ValueError:
            print('Input must be a number')
            continue

        if query == 1:
            return 1
        elif query == 2:
            return 2
        elif query == 3:
            return 3
        elif query == 4:
            return 4
        elif query == 5:
            return 5
        elif query == 6:
            quit()
        else:
            print('I did not understand that')

def create_contact():
    with open('phonebookdata.csv', 'a') as userFile:
        userFileWriter = csv.writer(userFile)
        line = []
        line.append(input("Enter a name: "))
        line.append(input("Enter a phone-number: "))
        line.append(input("Enter a catch-phrase: "))
        userFileWriter.writerow(line)

def retrieve_contact():
        searching = True
        while searching:
            with open('phonebookdata.csv', 'r') as userFile:
                with open('mostRecentSearch.csv', 'w') as newFile:
                    newFileWriter = csv.writer(newFile)
                    userFileReader = csv.reader(userFile)
                    search = input('Enter a name, phone number(with correct punctuation), or phrase ')
                    search = search.lower()
                    for line in userFileReader:
                        for index in line:
                            if search in index.lower():
                                newFileWriter.writerow(line)

                                print('You might be looking for' + str(line))
            searching = False


def update_existing_contact():
    searching = True
    while searching:
        with open('phonebookdata.csv', 'r') as userFile:
            with open('temp_phonebookdata.csv', 'a') as newFile:
                newFileWriter = csv.writer(newFile)
                userFileReader = csv.reader(userFile)
                search = input('Enter a name, phone number(with correct punctuation), or phrase to find a contact to update ')
                search = search.lower()
                for line in userFileReader:
                    change_line = False

                    for index in line:
                        if search in index.lower():
                            change_line = True
                    if change_line:
                        print('You might be trying to modify this contact: ' + str(line))
                        user_input = input("Are you indeed trying to modify this contact?(answers other than 'yes' won't modify file)")
                        if user_input == 'y' or user_input == 'yes' or user_input == 'Yes' or user_input == 'YES':
                            print("Enter updated information: ")
                            temp_line = []
                            temp_line.append(input("Enter a name: "))
                            temp_line.append(input("Enter a phone-number: "))
                            temp_line.append(input("Enter a catch-phrase: "))
                            newFileWriter.writerow(temp_line)
                    else:
                        newFileWriter.writerow(line)

        searching = False

while running:
    choice = make_decision()


    if choice == 1:
        create_contact()
    if choice == 2:
        retrieve_contact()
    if choice == 3:
        update_existing_contact()

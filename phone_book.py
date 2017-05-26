import csv

# phonebook = {'Kieran': {'name': 'Kieran','number': 8456331959,'phrase': 'Good code is not written, it\'s re-written.'},'Lambda': {'name': 'Lambda','number': 8454185633, 'phrase': 'I am a robot.'}}
running = True

while running:
    search_or_quit = True
    while search_or_quit:
        try:
            query = int(input('Enter 1 to search phonebook, or 2 to quit: '))
        except ValueError:
            print('Input must be a number')
            continue

        if query == 1:
            search_or_quit = False
        elif query == 2:
            quit()
        else:
            print('I did not understand that')

    searching = True
    while searching:
        with open('phonebookdata.csv', 'r') as userFile:
            userFileReader = csv.reader(userFile)
            search = input('Enter a name, phone number(with correct punctuation), or phrase ')
            for line in userFileReader:
                for index in line:
                    if search in index:
                        with open('mostRecentSearch.csv', 'w') as newFile:
                            newFileWriter = csv.writer(newFile)
                            newFileWriter.writerow(line)

                        print('You might be looking for' + str(line))
modifying = True
while modifying:
    while add_delete_quit:
        try:
            query = int(input('Enter 1 to add contact, 2 to delete contact, or 3 to quit: '))
        except ValueError:
            print('Input must be a number')
            continue
        if query == 1:

        if query == 1:
            add_delete_quit = False
        elif query == 3
            quit()
        else:
            print('I did not understand that')



    with open('phonebookdata.csv', 'r') as userFile:
        userFileReader = csv.reader(userFile)
        search = input('Enter a name, phone number(with correct punctuation), or phrase ')
        for line in userFileReader:

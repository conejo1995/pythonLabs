print("This program will tell you what meal it is time for based upon user input.")

print("Enter a the hour (ex. 8am):")

time = input()

if time in ['7am', '8am', '9am']:
    print("Breakfast Time!")
elif time in ['12pm', '1pm', '2pm']:
    print("Lunch Time!")
elif time in ['7pm', '8pm', '9pm']:
    print("Dinner Time")
elif time in ['10pm','11pm','12am','1am','2am','3am','4am']:
    print("Hammer Time!")
else:
     print("Not time to eat.")

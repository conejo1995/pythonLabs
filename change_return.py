hundred_bill = 10000
twenty_bill = 2000
ten_bill = 1000
five_bill = 500
dollar_bill = 100
quarter_value = 25
dime_value = 10
nickel_value = 5
penny_value = 1

register = {'hundreds' : 1,'twenties' : 4, 'tens' : 1, 'fives' : 1, 'ones' : 9, 'quarters' : 3, 'dimes' : 9, 'nickels' : 1, 'pennies' : 4}

def give_change(change_due):
    change_due = change_due * 100
    print('Change given back will be: ' )
    if change_due >= 10000 and int(change_due/hundred_bill) <= register['hundreds']:
        print( str(int(change_due/hundred_bill)) + ' Hundred Dollar Bills, ' )
        change_due = int(change_due%hundred_bill)

    if change_due >= 2000 and int(change_due/twenty_bill) <= register['twenties']:
        print( str(int(change_due/twenty_bill)) + ' Twenty Dollar Bills, ' )
        change_due = int(change_due%twenty_bill)

    if change_due >= 1000 and int(change_due/ten_bill) <= register['tens']:
        print( str(int(change_due/ten_bill)) + ' Ten Dollar Bills, ' )
        change_due = int(change_due%ten_bill)

    if change_due >= 500 and int(change_due/five_bill) <= register['fives']:
        print( str(int(change_due/five_bill)) + ' Five Dollar Bills, ' )
        change_due = int(change_due%five_bill)

    if change_due >= 100 and int(change_due/dollar_bill) <= register['ones']:
        print( str(int(change_due/dollar_bill)) + ' Dollar Dollar Bills, ' )
        change_due = int(change_due%dollar_bill)

    if change_due >= 25 and int(change_due/quarter_value) <= register['quarters']:
        print( str(int(change_due/quarter_value)) + ' Quarters, ' )
        change_due = int(change_due%quarter_value)

    if change_due >= 10 and int(change_due/dime_value) <= register['dimes']:
        print( str(int(change_due/dime_value)) + ' Dimes, ' )
        change_due = int(change_due%dime_value)

    if change_due >= 5 and int(change_due/nickel_value) <= register['nickels']:
        print( str(int(change_due/nickel_value)) + ' Nickels, ' )
        change_due = int(change_due/nickel_value)

    if change_due >= 1 and int(change_due/penny_value) <= register['pennies']:
        print( 'and ' + str(int(change_due/penny_value)) + ' Pennies')
    else:
        print("Not enough cash in register to give change")


print("This program will give change as optimally as possible depending on change")
print("available in the register. If an exact amount can't be achieved with the available")
print("change, then the program will state such")
change = float(input("Enter an amount of change to be given (in dollars): "))

give_change(change)

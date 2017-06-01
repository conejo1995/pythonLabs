#Takes muddled string input and converts into readable string
import re

def scrub_numbers(some_string):
    numbers =['1','2','3','4','5','6','7','8','9','0']
    for num in numbers:
        some_string = some_string.replace(num, '')
    print(some_string)

def gentle_clean(some_string):
    lines =['-', '_']
    some_string = some_string.replace(' ','')
    for line in lines:
        some_string = some_string.replace(line, ' ')
    print(some_string)

def clean_data(some_string):
    lines =['-', '_']
    numbers =['1','2','3','4','5','6','7','8','9','0']
    for line in lines:
        some_string = some_string.replace(line, ' ')
    for num in numbers:
        some_string = some_string.replace(num, '')
    some_string = some_string.strip()
    print(some_string)
def some_scrubber(some_string):
    temp_string = ''
    index = 3
    for letter in some_string:
        if index % 2 == 1:
            temp_string = temp_string + letter
        index = index + 1
    some_string = temp_string
    print(some_string)

def mr_clean(some_string):
    temp_string = ''
    for letter in some_string:
        temp_string = temp_string + letter + ' '
    some_string = temp_string
    print(some_string)
def ms_clean(some_string):
    list_of_strings = some_string.split()
    temp_string = ''
    for string in list_of_strings:
        temp_string =  temp_string + string[1:-1] + ' '
    list_of_strings = temp_string.split()
    for string in list_of_strings:
        some_string = some_string.replace(string, str(len(string)))
    print(some_string)
def strong_cleaner(some_string):
    special_chars =['!','@','#','$','%','^','&','*','(',')','1','2','3','4','5','6','7','8','9','0']
    for special_char in special_chars:
        some_string = some_string.replace(special_char, '')
    print(some_string)
def extracto(some_string):
    numbers =['1','2','3','4','5','6','7','8','9','0']
    temp_counter = 0
    total = 0
    for num in numbers:
        temp_counter = some_string.count(num)
        total = total + temp_counter * int(num)
    print(total)


scrub_numbers('Be9autiful9 i4s be2tter th4an ug42ly')

gentle_clean('Explicit_is-better_than -implicit')

clean_data('  42Simple-is_better_than-compl9ex   ')

some_scrubber('F l a t   i s   b e t t e r   t h a n   n e s t e d . ')

mr_clean('Sparse is better than dense')

ms_clean('Readability counts')

strong_cleaner('Err@#%$ors sho@#$@#$uld nev1!$#@er pass sile&I&&*(ntly')

extracto("1S2pe3cia4l ca5ses ar6en't sp7ecial en8ough to b9reak the r0ules.")

extracto("2S4pe6cia8l ca0ses ar2en't sp4ecial en6ough to b8reak the r0ules.")

extracto("3S6pe9cia2l ca5ses ar8en't sp1ecial en4ough to b7reak the r0ules.")

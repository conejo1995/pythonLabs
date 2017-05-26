def check_case(phrase):
    if '_' in words:
        print("Your phrase is snake_case")
        to_camel_case(phrase)
    else:
        print("Your phrase is CamelCase")
        to_snake_case(phrase)

def to_camel_case(converted_phrase):
    underscore_index = converted_phrase.find('_')
    print("This is your phrase in CamelCase! " + converted_phrase[:underscore_index] + converted_phrase[underscore_index+1:])

def to_snake_case(converted_phrase):
    underscore_index = converted_phrase.find('_')


words = input("Enter a phrase in either snake_case or CamelCase: ")

check_case(words)

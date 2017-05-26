

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}


running = True
while running:
    number_of_sentences = 0
    number_of_words = 0
    number_of_chars = 0
    automated_readability_index = 0

    print("To compute its automated readability index, pick from one of the files below:")
    print("1) geneology_of_morals.txt")
    print("2) gettysburg_address.txt")
    print("3) jack_and_jill.txt")
    print("q) Quit")
    print("")
    user_input = input()
    print("")
    user_input = user_input.lower()

    if user_input == '1':
        with open('geneology_of_morals.txt','r') as f:
            for line in f:
                words = line.split()
                number_of_sentences = number_of_sentences + line.count('.')
                number_of_words = number_of_words + len(words)
                number_of_chars = number_of_chars + len(line) - line.count('.') - line.count(' ') - line.count(',') - line.count('(') - line.count(')') - line.count('-') - line.count('[') - line.count(']') - line.count(':')

            automated_readability_index = (4.71) * (number_of_chars/number_of_words) + (0.5) * (number_of_words/number_of_sentences) - 21.43

            print(str(number_of_words) + " words")
            print(str(number_of_chars) +" characters")
            print(str(number_of_sentences) + " sentences")
            print(str(automated_readability_index) + " is its ARI")
            automated_readability_index = int(automated_readability_index)
            if automated_readability_index > 14:
                automated_readability_index = 14
            print("Ages: " + ari_scale[automated_readability_index]['ages'] + " Grade:" + ari_scale[automated_readability_index]['grade_level'])
            print("")
    elif user_input == '2':
        with open('gettysburg_address.txt','r') as f:
            for line in f:
                words = line.split()
                number_of_sentences = number_of_sentences + line.count('.')
                number_of_words = number_of_words + len(words)
                number_of_chars = number_of_chars + len(line) - line.count('.') - line.count(' ') - line.count(',') - line.count('(') - line.count(')') - line.count('-') - line.count('[') - line.count(']') - line.count(':')

            automated_readability_index = (4.71) * (number_of_chars/number_of_words) + (0.5) * (number_of_words/number_of_sentences) - 21.43

            print(str(number_of_words) + " words")
            print(str(number_of_chars) +" characters")
            print(str(number_of_sentences) + " sentences")
            print(str(automated_readability_index) + " is its ARI")
            automated_readability_index = int(automated_readability_index)
            if automated_readability_index > 14:
                automated_readability_index = 14
            print("Ages: " + ari_scale[automated_readability_index]['ages'] + " Grade:" + ari_scale[automated_readability_index]['grade_level'])
            print("")
    elif user_input == '3':
        with open('jack_and_jill.txt','r') as f:
            for line in f:
                words = line.split()
                number_of_sentences = number_of_sentences + line.count('.')
                number_of_words = number_of_words + len(words)
                number_of_chars = number_of_chars + len(line) - line.count('.') - line.count(' ') - line.count(',') - line.count('(') - line.count(')') - line.count('-') - line.count('[') - line.count(']') - line.count(':')

            automated_readability_index = (4.71) * (number_of_chars/number_of_words) + (0.5) * (number_of_words/number_of_sentences) - 21.43

            print(str(number_of_words) + " words")
            print(str(number_of_chars) +" characters")
            print(str(number_of_sentences) + " sentences")
            print(str(automated_readability_index) + " is its ARI")
            automated_readability_index = int(automated_readability_index)
            if automated_readability_index > 14:
                automated_readability_index = 14
            print("Ages: " + ari_scale[automated_readability_index]['ages'] + " Grade:" + ari_scale[automated_readability_index]['grade_level'])
            print("")
    elif user_input == 'q':
        quit()
    else:
        print("Enter valid input ")
        print("")

print("Enter a word and this program will determine if it follows the i before e rule")
word = input()

if 'ie' in word:
    index = word.find('ie')
    if 'c' in word[index-1:index]:
        print("Word does not follow rule")
    else:
        print("This word is fine and follows the rules")
if 'ei' in word:
    index = word.find('ei')
    if 'c' in word[index-1:index]:
        print("This word is fine and follows the rules")
    else:
        print("Word does not follow rule")

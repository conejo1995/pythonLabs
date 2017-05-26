import string
print("Enter a word and this program will determine if it is a palindrome or not")
word = input()

for punct in string.punctuation:
    if punct in word:
        word = word.replace(punct,'')


print(word)
if word == word[::-1]:
    print("Word is a palindrome")
else:
    print("Word is not a palindrome")

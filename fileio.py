
with open('text.txt', 'r') as text:
    with open('temp.txt', 'w') as new_text:
        for line in text.readlines():
            new_text.write(line[15:20] + '\n')
    print(text.readlines())

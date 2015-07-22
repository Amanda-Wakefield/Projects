myword = input('Enter a word: ')
mylist= list(myword.lower())
edited_word =''
vowels = list('aeiou')
for letter in range(0,len(mylist)):
    if mylist[letter] not in vowels:
        edited_word += mylist[letter]
print(edited_word)

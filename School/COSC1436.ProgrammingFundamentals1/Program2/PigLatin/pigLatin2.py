'''
Program 2
Pig Latin version 2.0
Ethan D. Hann
'''

print("Enter a word to translate.")
word = input("> ")

mut_word = word.lower()
first_letter = mut_word[0]
vowels = 'aeiou'
pig_latin_word = ""
consonants = ""
new_word = ""

while mut_word != '.':
    pig_latin_word = ""
    consonants = ""
    first_letter = mut_word[0]
    if first_letter in vowels:
        print(mut_word + "yay")
    else:
        index = 0
        while index <= len(mut_word):
            if mut_word[index] in vowels:
                break
            else:
                new_word = mut_word.replace(mut_word[index], '')
                consonants += mut_word[index]
            index += 1

        pig_latin_word = new_word + consonants + 'ay'
        print(pig_latin_word)
        print(new_word)
        print(mut_word)
    word = input("> ")
    mut_word = word.lower()
print(consonants)
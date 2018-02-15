#Ethan Hann
#Pig Latin Translator Version 1
#Project 2 (option 2 worth 70 points)
#Due November 4, 2014

#Import modules
import os

#------------------------------------------------------------------------------------------
#Defining functions

#Function to convert a word into pig latin.
def pig_latin(word):
    """ Convert a word to pig latin """
    vowels = "aeiouAEIOU"
    const_list = []
    original_word = word
    first_letter = original_word[0]

    if first_letter in vowels:
        pig_latin_word = original_word + "yay"
        print(pig_latin_word)

    else:
        for ch in original_word:
            if ch in vowels:
                break
            else:
                const_list.append(ch)

        const_string = ""
        for i, letter in enumerate(const_list):
            const_string += "".join(letter)

        length = len(const_string)
        pig_latin_word = original_word[length:] + const_string + "ay"
        print(pig_latin_word)
    output_file.write("{} --> {}".format(original_word, pig_latin_word))
    output_file.write("\n")

#Function to check if a word is valid input. If the word is not alphabetical, return False. If the word is a period,
#return False. If the word is a valid word, return True
def check_word(word):
    """ Returns True if word is correct and False if word is not correct """
    if not word.isalpha():
        print("Must enter a valid string containing only alphabetical characters!")
        return False
    elif word == '.':
        return False
    else:
        return True
#------------------------------------------------------------------------------------------
#File checking

#Open the file and create a header. If it exists, add the pig latin words to the end of the file.
if os.path.exists("pig_latin_words.txt"):
    output_file = open("pig_latin_words.txt", "a+")
else:
    output_file = open("pig_latin_words.txt", "w")
    print("Original Word --> Pig Latin", file=output_file)
    print("---------------------------------------------", file=output_file)
    output_file.close()
    output_file = open("pig_latin_words.txt", "a+")
#------------------------------------------------------------------------------------------
#Beginning of main code. Start accepting input.

#Welcome message displayed to the user.
print("Pig Latin Translator Version 1")
print("The original word will be translated and added to a new text file which will open when the program is exited.")

#Default value of entering_words is first set to True so that the loop begins execution.
entering_words = True

#While the user is entering words (if the input_word isn't a period), the word is checked.
#If the check function returns False, the loop is restarted skipping the elif statement (note the continue keyword).
#If the check function returns True, the word is converted into pig latin.
while entering_words is True:
    input_word = input("Enter a word to translate (<.> to exit): ")
    if not check_word(input_word):
        if input_word == '.':
            #Close the file and open it on the desktop.
            output_file.close()
            os.popen("pig_latin_words.txt")
            entering_words = False
        else:
            continue
    elif check_word(input_word):
        pig_latin(input_word)
#------------------------------------------------------------------------------------------
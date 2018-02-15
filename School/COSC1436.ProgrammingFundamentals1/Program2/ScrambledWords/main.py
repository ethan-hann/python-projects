#Ethan Hann
#Paragraph Scrambler Version 1
#Project 2 (option 3 worth 70 points)
#Due November 4, 2014

#Import necessary modules
import os
import random
import textwrap

#Defining functions
#Function to check if a file exists. If not, it creates it. Of course, there is nothing in the file it creates though.
def check_file(file):
    if os.path.isfile(file):
        pass
    else:
        f = open(file, "w")
        f.close()

#Function to scramble the middle of a word
def scramble(word):
    if len(word) == 1:
        return word
    else:
        output = list(word[1:-1])
        random.shuffle(output)
        output.append(word[-1])
        return word[0] + "".join(output)

#Start of program.
file = input("File containing the paragraph (no extension required; if doesn't exist, a new empty file will be"
             "created): ")
newFile = file + ".txt"

#Check if file exists using the check_file() function defined earlier.
check_file(newFile)

inputFile = open(newFile, "r")
outputFile = open("jumbled_paragraph.txt", "w+")

#Define the two lists and the new paragraph variables.
words = []
words_scrambled = []
new_paragraph = ""

#Iterate through each line in the file. Iterate through each word in the line and append it to the words list.
for line in inputFile:
    for word in line.split():
        words.append(word)

#Iterate through each enumeration of the words list.
for ix, word in enumerate(words):
    #Check if the end of the word contains a comma or period.
    #If it does, only scramble the middle not containing the punctuation.
    #After scrambling, add the punctuation back to the end of the scrambled word and append the word to the
    #words_scrambled list.
    if word[-1] == ',':
        punctuation = ","
        s = scramble(word[0:len(word) - 1])
        new_scram = s + punctuation
        words_scrambled.append(new_scram)
    elif word[-1] == '.':
        punctuation = "."
        s = scramble(word[0:len(word) - 1])
        new_scram = s + punctuation
        words_scrambled.append(new_scram)
    #If no punctuation is in the word, simply use the scramble function defined earlier and append the word to the
    #words_scrambled list.
    else:
        words_scrambled.append(scramble(word))

#Iterate through the words_scrambled list and create a new_paragraph with the word followed by a space.
for i, w in enumerate(words_scrambled):
    new_paragraph += w + " "

#Format the new_paragraph to be a paragraph. Before textwrap, every word was added to the same line.
#textwrap.fill() constricts the lines to only 100 characters.
wrapped_para = textwrap.fill(new_paragraph, 100)

#Finally, write the formatted paragraph to the outputFile.
outputFile.write(wrapped_para)
print("Done.")

#Open the new file on the screen.
os.popen("jumbled_paragraph.txt")
outputFile.close()
inputFile.close()
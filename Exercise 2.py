#Author: Warren Spalding - SID: 52199280
#Date: 22/11/2021
#CS1032 Assessment 2: Exercise 2
#Program that asks the user to input the name of a file to open. Opens the file, and
#if its successful in opening the file, then it must read from the file and calculate
#how many characters are in the file and how many words are in the file.
#Then try to create a new file named results.txt if successful in creating the file
#then it must write in that file the results to it in an approved format.
#E.g
#"Information about filename:
#The number of characters is: x characters.
#The number of words is: y words."
#If not successful in creating a file, then it must not throw out an error, it must
#print out the message: "I am sorry, I cannot seem to be able to create the results
#file."

import string
import sys

try:
    resultsFile = open("results.txt", "w+")
except IOError:
    print("I am sorry, I cannot seem to be able to create the results file.")
    sys.exit()
    


myFile_user = input("Please type in file name you wish to open including extension: ")
try:
    myFile = open(myFile_user)
except IOError:
    print("I am sorry, I cannot seem to be able to open the file you have chosen.")
    sys.exit()


data = myFile.read()
words = (data).split()
no_of_characters = len(data)
no_of_words = len(words)

no_of_characters = 0
for character in data:
    if not character.isspace():
        no_of_characters += 1


no_of_words = 0
for word in words:
    if len(word) >= 2:
        for letter in word:
            if not letter.isalpha():
                break
        else:
            no_of_words += 1
    
        

print("Number of characters in text file: ", no_of_characters)
print("Number of words in text file: ",  no_of_words)

resultsFile.write("Information about exercise2.txt:\n")
resultsFile.write("The number of characters is: " + str(no_of_characters) + " characters.\n")
resultsFile.write("The number of words is: " + str(no_of_words) + " words.")



resultsFile.close()
myFile.close()


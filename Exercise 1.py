#Author: Warren Spalding - SID: 52199280
#Date: 22/11/2021
#CS1032 Assessment 2: Exercise 1
#Program that asks a user to input a sentence, removes all the spaces between words
#in the sentence and assign to a new variable, prints the value of the new variable,
#reverses the letters in the new variable and prints the result.

userSentence = input("Please enter a sentence: ")

sentenceStr = userSentence
remove_whitespace = sentenceStr.replace(" ", "")
print(remove_whitespace)

def backwards(remove_whitespace):
    reverse = []
    final = ""
    count = len(remove_whitespace) - 1
    while count >= 0:
        reverse.append(remove_whitespace[count])
        count = count - 1
        final = " ".join(reverse)
        final_2= final.replace(" ", "")
    return final_2
print(backwards(remove_whitespace))

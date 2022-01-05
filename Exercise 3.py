#Author: Warren Spalding - SID: 52199280
#Date: 22/11/2021
#CS1032 Assessment 2: Exercise 3
#Program that randomly generates a list containing four numbers between 1 and 10.
#Creates a second list from the user's input of four numbers between 1 and 10.
#Then compares the values of each index in the two lists and creates a new list
#with the letters.
import random
randList = []
userList = []
charList = []
for i in range(0,4):
    num = random.randint(1,10)
    randList.append(num)
print("\n")

print("Please enter a list that consists of integers between one and ten.")

print("\n")
for i in range(0, 4):
    print("Enter number at index", i + 1)
    x = int(input())
    userList.append(x)
print("User typed list ", userList)

for i in range(0, 4):
    if randList[i] == userList[i]:
        charList.append("S")#indicates the number in a position of the two lists are the same
    elif randList[i] > userList[i]:
        charList.append("L")#indicates if the number in that position is lower than random generated list
    else:
        charList.append("H")#indicates if the number in that position is higher than the random generated list.
print("\n")
print("The random list is ", randList)
print("\n")
print(charList)

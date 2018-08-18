#! /usr/bin/python3

#William Skyler Garrison
#Principles of Programming Languages
#2/22/2016

from collections import defaultdict
import sys

#defaultdict allows ease of creating a dictionary of lists
grammarDict = defaultdict(list)

if len(sys.argv) == 3:
    #truncate the second command to get the integer length of desired strings
    specLength = int(sys.argv[1][2:])
    
    #open the file in the third argument in reading mode
    grammarFile = open(sys.argv[2], 'r')
else:
    #open the file from the second argument in reading mode
    grammarFile = open(sys.argv[1], 'r')
    
    #default length is 3
    specLength = 3

#Seperate items; leftmost symbols are keys, symbols after assignment operator
#are put in a list
for line in grammarFile:
    tempLine = line.strip()
    
    tempList = tempLine.split()
    
    itemsList = []
    
    for index in range(2, len(tempList)):
        itemsList.append(tempList[index])
    
    grammarDict[tempList[0]].append(itemsList)
    
grammarFile.close()

workList = []

#use a dictionary for the printlist to eliminate repeated productions
printDic = defaultdict(int)

#Push starting symbols all onto the worklist
for key in grammarDict:
    for item in grammarDict[key]:
        workList.append(item)

#Start the iteration on the worklist
#Keep going while the worklist has members
while len(workList) > 0:
    
    #necessary to keep an independent index variable, because the index
    #function on lists in python returns the first instance of the character
    #in a list, and we need to account for repeated terminals in output strings
    index = 0    

    #copy the initial worklist entry and remove it from the worklist
    sentence = workList[0]
    holderSentence = list(sentence)
    workList.remove(sentence)
    
    for character in holderSentence:
        if character in grammarDict:
            for replacement in grammarDict[character]:
                
                newItem = list(holderSentence)
                newItem.pop(holderSentence.index(character))
                
                #copy a list of the replacement string, which needs to be
                #reversed because we will use the insert function multiple times
                #with the same index, and insert puts the element in before the
                #given index
                addList = list(replacement)
                addList.reverse()
                
                for element in addList:
                    newItem.insert(holderSentence.index(character), element)
                
                #check the length against the specified length before adding it
                #to the end of the worklist
                if len(newItem) <= specLength:
                    workList.append(newItem)
            break
        
        #if the symbol is a terminal, check if it's the last symbol in the
        #production. If so, that means it's a complete sentence, so put it on
        #the printing list.
        else:
            if index == len(holderSentence)-1:
                holderString = ""
                for letter in holderSentence:
                    holderString = holderString + " " + letter
                holderString = holderString[1:]
                printDic[holderString]
            index += 1

for key in printDic:
    print(key)
                        
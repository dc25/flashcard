#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Set up flash card sets in $HOME/.flashcards/filename
# where each filename defines an array called cards, like this:
# cards = [
#     [ "1", "one" ],
#     [ "2", "two" ],
# ]
# It will look for .flashcards/all as a default, or you can pass
# the filename as an argument, e.g. flashcard shortlist will
# use the cards defined in $HOME/.flashcard/shortlist.
#
# Copyright 2007 by Akkana Peck.
# This program is free software -- please share it under the terms
# of the GNU Public License.

import os, sys, random, pickle, getopt

workingCardCount = 5
passingLevel = 3

def print_card(card) :
    for word in card :
        print word, "      ",
    print ""

class StudyCard:
    # "store a card and how well known it is."              1
    def __init__(self, card):
        self.myCard = card
        self.skillLevel = 0
        pass

    def show(self):
        print_card(self.myCard)

class StudyTask:
    def __init__(self, studyCardsArg, keyArg):
        self.studyCards = studyCardsArg
        self.unknownCards = []
        self.knownCards = []
        self.workingCards = []
        self.key = keyArg
        for card in self.studyCards:
            self.unknownCards.append(card)
        for index in range(0, workingCardCount):
            card = random.choice(self.unknownCards)
            self.workingCards.append(card)
            self.unknownCards.remove(card)

class TwoWayStudyTask:
    def __init__(self, studyCardsArg):
        self.studyTask0 = StudyTask(studyCardsArg, 0)
        self.studyTask1 = StudyTask(studyCardsArg, 1)

def importFromFile(file):
    localForCards={'cards': []}
    if (os.path.exists(file)):
        execfile(file, {}, localForCards)
    else:
        print file, " does not exist."

    if len(localForCards['cards']) > 0 :
        print "Read", len(localForCards['cards']), "cards from", file

    return localForCards['cards']

def main(argv):                         
    try:                                
        opts, args = getopt.getopt(argv, "r:w:i:", ["read=", "write=", "import="])
    except getopt.GetoptError:   
        # usage()                 
        sys.exit(2)                

    doImport = False
    doRead = False
    doWrite = False
    for opt, arg in opts:           
        if opt in ("-i", "--import"):
            importFile=arg
            doImport = True
        elif opt in ("-r", "--read"):
            readFile=arg
            doRead = True;
        elif opt in ("-w", "--write"):
            writeFile=arg
            doWrite=True

    if doImport:
        cards = importFromFile(importFile)

        studyCards = []
        for card in cards:
            studyCards.append(StudyCard(card))

        twoWayTask = TwoWayStudyTask(studyCards)

    if doRead:
        readInput = open(readFile, 'r')
        twoWayTask = pickle.load(readInput)


    while True :
        task = twoWayTask.studyTask1
        card = random.choice(task.workingCards)
        which = card.myCard[task.key]

        print which,

        ans = raw_input()
        card.show()
        ans = raw_input()
        if ans == "q" :
            break
        if ans == "" :
            card.skillLevel+=1
            if card.skillLevel >= passingLevel:
                task.workingCards.remove(card)
                task.knownCards.append(card)
                print card.myCard[0], " moved to known."
                if random.randint(0,1):
                    newCard = random.choice(task.knownCards)
                    task.knownCards.remove(newCard)
                    card.skillLevel-=1
                else:
                    newCard = random.choice(task.unknownCards)
                    task.unknownCards.remove(newCard)
                task.workingCards.append(newCard)
        else:
            card.skillLevel=0

    if doWrite:
        output = open(writeFile, 'wb')
        pickle.dump(twoWayTask, output)

if __name__ == "__main__":
        main(sys.argv[1:])


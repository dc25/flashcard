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

import os, sys, random

def print_card(card) :
    for word in card :
        print word, "      ",
    print ""


cardset = "all"

cardfile = os.path.join(os.path.expanduser("~"), "flashcards", cardset)

if (os.path.exists(cardfile)) :
    execfile(cardfile)
                      
if len(cards) > 0 :
    print "Read", len(cards), "cards from", cardfile

class StudyCard:
    # "store a card and how well known it is."              1
    def __init__(self, card):
        self.myCard = card
        self.skillLevel = 0
        pass

    def show(self):
        print_card(self.myCard)

studyCards = []
for card in cards:
    studyCards.append(StudyCard(card))

workingCardCount = 5
passingLevel = 3

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


twoWayTask = TwoWayStudyTask(studyCards)


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


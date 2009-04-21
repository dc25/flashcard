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

print "Flash card script version 0.3 by Akkana Peck.\n"
print "On seeing a word, think of the answer then hit return."
print "Then hit return again to see the next word."
print "But if you got it wrong, type anything besides q before hitting Return"
print "and the word will be added to a list to be presented more often."
print "q<Return> quits."
print ""

if len(sys.argv) > 1 :
    cardset = sys.argv[1]
    print "Using cards from set '" + cardset + "'"
else :
    cardset = "all"

cardfile = os.path.join(os.path.expanduser("~"), ".flashcards", cardset)
if (os.path.exists(cardfile)) :
    execfile(cardfile)
else :
    cardfile = os.path.join(os.path.expanduser("~"), "flashcards", cardset)
    if (os.path.exists(cardfile)) :
        execfile(cardfile)
                      
if len(cards) > 0 :
    print "Read", len(cards), "cards from", cardfile

print ""

bonus_words = len(cards)

while True :
    card = random.choice(cards)
    which = random.choice(card)

    print which,
    if raw_input() == "q" :
        break
    print_card(card)

    ans = raw_input()
    if ans == "q" :
        break
    if ans != "" :
        # Save another copy of this word in the list
        cards.append(card)

# Print the ones missed
print "\nMissed:"
for card in cards[bonus_words:] :
    print_card(card)


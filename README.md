# Graphs
This repository contains a series of graph algorithms. Each file is described below:

BreadthFirstSearch.py:

An implementation of BFS on a dictionary representation of a Graphs

IsEulerianDictionary.py:

Determines if a graph has an Eulerian cycle. Run BFS

DictionaryToMatrix.py:

Returns the Matrix representation of a graph, give a dictionary representation as
input.

word_ladder.py (requires "google-10000-english.txt" in the same directory):

Reads in 10000 english words from a text file and builds a graph representation of
all of the words. Given two words as input, a starting word and ending word, it
will tell you the shortest "Word Ladder" sequence between the two words. Essentially,
it transforms the first word into the second word be changing no more than one letter
at a time, where each letter change must result in another english word.

Example Dog -> Cat: Dog -> Do(t)->D(a)t -> (C)at (apparently 'dat' is a real word according to google!)

To run word_ladder.py enter the following command in your terminal:

>> python3 word_ladder.py <starting_word> <ending_word>

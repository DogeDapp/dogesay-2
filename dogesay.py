#!/usr/bin/python

from argparse import ArgumentParser
from random   import randrange

DOGE_PREFIXES = ["such", "much", "so", "many", "wow"]
DOGE_EJACULATES = ["wow"]

def num_words(clause):
    numwords = 0
    for word in clause.split():
        numwords += 1
    return numwords

def doge_syntax(clause):
    if num_words(clause) > 1:
        return clause
    else:
        return DOGE_PREFIXES[randrange(0,len(DOGE_PREFIXES))]+" "+clause

    
if __name__ == "__main__":
    parser = ArgumentParser(description="Cowsay for a new generation.")
    parser.add_argument("inputfile", metavar="<input file>")

    clausefile = open(parser.parse_args().inputfile, "r")

    for clause in clausefile:
        move_next_iter = False

        while not move_next_iter:
            generate_wow? = True if randrange(0,100) > 60 else False
            # TODO: work with "wow" as the clause
            move_next_iter = True

        # TODO: work with clause as the clause

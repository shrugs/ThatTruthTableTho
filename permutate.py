#! /usr/bin/env python
import sys
import itertools
import pprint

INDENT_LEVEL = '\t'
VARIABLE_DEFINITION_STR = INDENT_LEVEL + '%s = %i;'
DELAY_TIME_STR = INDENT_LEVEL + '#%i;'


def halp():
    print 'Usage:'
    print '    python permutate.py A B C D 10'
    print '    python permutate.py Input1 [Input2...] TimeToWait'
    print ''
    exit()


if __name__ == '__main__':

    # need at least 3 args
    if len(sys.argv) < 3:
        halp()

    inputs = sys.argv[1:-1]
    dt = int(sys.argv[-1])

    # via http://stackoverflow.com/questions/6336424/python-build-a-dynamic-growing-truth-table
    truth_table = list(itertools.product([False, True], repeat=len(inputs)))

    for row in truth_table:
        # for each row, generate a set of variable definitions
        for i, value in enumerate(row):
            print VARIABLE_DEFINITION_STR % (inputs[i], value)

        print DELAY_TIME_STR % (dt)
        print ''

#-------------------------------------------------------------------------------
# Name:        store_credit.py
# Purpose:     solution to Google CodeJam problem 'Store Credit' from the
#              Africa 2010 Qualification Round:
#              http://code.google.com/codejam/contest/dashboard?c=351101#s=p0
#
# Author:      GrayA
#
# Created:     23/11/2011
# Copyright:   (c) GrayA 2011
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import os

def main():
    # open the input file
    input_path = os.path.join(os.getcwd(),
        "store_credit_files" + os.sep + "a-large-practice.in")
    input = open(input_path, 'r')

    # the first line in the input file is the number of cases
    num_cases = int(input.readline())

    # build up all answers in this list, then push the whole
    #  list to the output file when we're done
    answers = []

    for case in range(num_cases):
        # each case consists of three lines:
        #  1) the amount of money the consumer has
        credit = int(input.readline())
        #  2) the number of items in the store
        num_items = int(input.readline())
        #  3) the price of each item
        item_prices = [int(x) for x in input.readline().split(' ')]

        done = False
        for (i, price1) in enumerate(item_prices):
            for (j, price2) in enumerate(item_prices[i+1:]):
                if price1 + price2 == credit:
                    # output should use 1-based indices, so we need to
                    #  normalize our values for that
                    answers.append("Case #{0}: {1} {2}".
                        format(case+1, i+1, j+i+2))
                    # we've found an answer; set this flag so we can
                    #  jump out of the both nested loops
                    done = True
                    break
            if done:
                break

    # we're done with the input file
    input.close()

    # create the output file
    output_path = os.path.join(os.getcwd(),
        "store_credit_files" + os.sep + "a-large-practice.out")
    output = open(output_path, 'w')
    # write the answers to the file, one answer per line
    output.write("\n".join(answers))
    output.close()

if __name__ == '__main__':
    main()

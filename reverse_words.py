#-------------------------------------------------------------------------------
# Name:        reverse_words.py
# Purpose:     solution to Google CodeJam problem 'Reverse Words' from the
#              Africa 2010 Qualification Round:
#              http://code.google.com/codejam/contest/dashboard?c=351101#s=p1
#
# Author:      aaron gray
#
# Created:     28Nov2011
# Copyright:   (c) aaron gray 2011
#-------------------------------------------------------------------------------

import os

def solve(input_path, output_path):
    input = open(input_path, 'r')

    # the first line in the input file is the number of cases
    num_cases = int(input.readline())

    # build up all answers in this list, then push the whole
    #  list to the output file when we're done
    answers = []

    for case in range(num_cases):
        # each case consists of one line: the list of words to reverse
        line = input.readline().strip()
        # convert the string to a list of words
        words = line.split(" ")
        # reverse that word list and put the spaces back in
        words.reverse()
        answers.append("Case #{0}: {1}".format(case+1, " ".join(words)))

    # we're done with the input file
    input.close()

    # create the output file
    output = open(output_path, 'w')
    # write the answers to the file, one answer per line
    output.write("\n".join(answers))
    output.close()

def main():
    # solve for small input
    input_path = os.path.join(os.getcwd(),
        "reverse_words_files" + os.sep + "small.in")
    output_path = os.path.join(os.getcwd(),
        "reverse_words_files" + os.sep + "small.out")
    solve(input_path, output_path)

    # solve for large input
    input_path = os.path.join(os.getcwd(),
        "reverse_words_files" + os.sep + "large.in")
    output_path = os.path.join(os.getcwd(),
        "reverse_words_files" + os.sep + "large.out")
    solve(input_path, output_path)

if __name__ == '__main__':
    main()

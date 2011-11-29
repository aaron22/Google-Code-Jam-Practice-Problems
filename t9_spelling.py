#-------------------------------------------------------------------------------
# Name:        t9_spelling.py
# Purpose:     solution to Google CodeJam problem 'T9 Spelling' from the
#              Africa 2010 Qualification Round:
#              http://code.google.com/codejam/contest/dashboard?c=351101#s=p2
#
# Author:      aaron gray
#
# Created:     28Nov2011
# Copyright:   (c) aaron gray 2011
#-------------------------------------------------------------------------------

import os

# create a mapping of characters to their T9 representation
char_to_t9 = {'a': "2", 'b': "22", 'c': "222", 'd': "3", 'e': "33", 'f': "333",
    'g': "4", 'h': "44", 'i': "444", 'j': "5", 'k': "55", 'l': "555", 'm': "6",
    'n': "66", 'o': "666", 'p': "7", 'q': "77", 'r': "777", 's': "7777",
    't': "8", 'u': "88", 'v': "888", 'w': "9", 'x': "99", 'y': "999",
    'z': "9999", ' ': "0"}

def solve(input_path, output_path):
    input = open(input_path, 'r')

    # the first line in the input file is the number of cases
    num_cases = int(input.readline())

    # build up all answers in this list, then push the whole
    #  list to the output file when we're done
    answers = []

    for case in range(num_cases):
        # each case consists of one line: the message to t9-ify
        message = input.readline()[:-1]
        # iterate over characters and replace each with the
        #  correct T9 representation
        last_number = "~"
        converted_message = ""
        for letter in message:
            # get the T9 representation of this character
            representation = char_to_t9[letter]
            # if it's the same number as the previous letter,
            #  we need to input a pause (represented by a space)
            if representation[0] == last_number:
                converted_message += ' '
            # add the T9 representation to the converted message
            converted_message += representation
            last_number = representation[-1]
        # this message is done; add it to the answer list
        answers.append("Case #{0}: {1}".format(case+1, converted_message))

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
        "t9_spelling_files" + os.sep + "c-small-practice.in")
    output_path = os.path.join(os.getcwd(),
        "t9_spelling_files" + os.sep + "c-small-practice.out")
    solve(input_path, output_path)

    # solve for large input
    input_path = os.path.join(os.getcwd(),
        "t9_spelling_files" + os.sep + "c-large-practice.in")
    output_path = os.path.join(os.getcwd(),
        "t9_spelling_files" + os.sep + "c-large-practice.out")
    solve(input_path, output_path)

if __name__ == '__main__':
    main()

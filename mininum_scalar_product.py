#-------------------------------------------------------------------------------
# Name:        minimum_scalar_products.py
# Purpose:     solution to Google CodeJam problem 'Minimum Scalar Product' from
#              Round 1A of the 2008 competition:
#              http://code.google.com/codejam/contest/dashboard?c=32016#s=p0
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
        # the first line in each case is the number of elements
        #  in that case's vectors and can be ignored; the two lines
        #  after that are the vectors themselves
        garbage, v1, v2 = input.readline(), input.readline(), input.readline()
        # the minimum scalar product can be found by sorting the two
        #  vectors in opposite order
        v1 = sorted([int(x) for x in v1.split(' ')])
        v2 = sorted([int(x) for x in v2.split(' ')], reverse=True)
        # get the product of the two vectors
        min = scalar_product(v1, v2)
        # this case is done; add it to the answer list
        answers.append("Case #{0}: {1}".format(case+1, min))

    # we're done with the input file
    input.close()

    # create the output file
    output = open(output_path, 'w')
    # write the answers to the file, one answer per line
    output.write("\n".join(answers))
    output.close()

def scalar_product(v1, v2):
    '''returns the scalar product of the two vectors'''
    product = 0
    for i in range(len(v1)):
        product += v1[i] * v2[i]
    return product

def main():
    # solve for small input
    input_path = os.path.join(os.getcwd(),
        "minimum_scalar_product_files" + os.sep + "small.in")
    output_path = os.path.join(os.getcwd(),
        "minimum_scalar_product_files" + os.sep + "small.out")
    solve(input_path, output_path)

    # solve for large input
    input_path = os.path.join(os.getcwd(),
        "minimum_scalar_product_files" + os.sep + "large.in")
    output_path = os.path.join(os.getcwd(),
        "minimum_scalar_product_files" + os.sep + "large.out")
    solve(input_path, output_path)

if __name__ == '__main__':
    main()

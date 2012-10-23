#-------------------------------------------------------------------------------
# Purpose:     solution to Google CodeJam problem 'Rope Intranet':
#              http://code.google.com/codejam/contest/619102/dashboard#s=p0
#
# Author:      aaron gray
#
# Created:     18Oct2012
#-------------------------------------------------------------------------------

import os

def solve(input_file):
	# the first line in the input file is the number of cases
    num_cases = int(input_file.readline())

    # build up all answers in this list
    answers = []

    for case in range(num_cases):
        # each case starts with the number of wires
        num_wires = int(input_file.readline())
        # get all of the wires for this case
        wires = []
        for i in range(num_wires):
        	wire = input_file.readline().split(" ")
        	wire = int(wire[0]), int(wire[1])
        	wires.append(wire)

        intersections = 0
        for i, wire in enumerate(wires):
        	for cross_wire in wires[i+1:]:
        		if (are_intersecting(wire, cross_wire)):
        			intersections += 1

        # this case is done; add it to the answer list
        answers.append("Case #{0}: {1}".format(case+1, intersections))

    # we're done with the input file
    input_file.close()

    return answers

def are_intersecting(wire1, wire2):
	# is wire1 totally below wire2?
	if wire1[0] < wire2[0] and wire1[1] < wire2[1]:
		return False

	# is wire1 totally above wire2?
	if wire1[0] > wire2[0] and wire1[1] > wire2[1]:
		return False

	# if wire1 is not totally above or below wire 2, then they intersect
	return True

def write_output(output_path, solution):
    # create the output file
    output = open(output_path, 'w')
    # write the answers to the file, one answer per line
    output.write("\n".join(solution))
    output.close()

def main():
    # solve for small input
    input_file = open(
    	os.path.join(os.getcwd(), "rope_intranet", "small.in"), 'r');
    solution = solve(input_file)
    output_path = os.path.join(os.getcwd(),
        "rope_intranet", "small.out")
    write_output(output_path, solution)

    # solve for large input
    input_file = open(
    	os.path.join(os.getcwd(), "rope_intranet", "large.in"), 'r');
    solution = solve(input_file)
    output_path = os.path.join(os.getcwd(),
        "rope_intranet", "large.out")
    write_output(output_path, solution)

if __name__ == '__main__':
    main()
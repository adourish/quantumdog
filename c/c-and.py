from pyeda.inter import *

a, b = map(exprvar, 'ab')

# Create the AND gate expression
and_gate = a & b

# Define the input combinations
input_combinations = [(0, 0), (0, 1), (1, 0), (1, 1)]

# Iterate over input combinations
for input_comb in input_combinations:
    # Assign the input values
    a.value, b.value = input_comb
    
    # Evaluate the AND gate expression directly
    output = and_gate.restrict({a: input_comb[0], b: input_comb[1]})
    
    # Print the input values and the output
    print(f"Input: a={input_comb[0]}, b={input_comb[1]}, Output: {output}")
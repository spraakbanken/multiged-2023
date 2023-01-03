import argparse

# Convert an M2 file to a CoNLL file with an error type label on each token
def main():
    # Parse command line args
    args = parse_args()
    
    # Open the M2 file and output file
    with open(args.m2_file) as m2, open(args.out, "w") as out:
        # Save a complete M2 block here and count blocks
        m2_block = []
        # Loop through M2 lines
        for line in m2:
            line = line.strip()
            # Add non empty lines to the block
            if line: m2_block.append(line)
            # Empty lines signal the end of the block, so process it
            else:
                # Get the original text and edits
                orig = m2_block[0].split()[1:] # Ignore leading "S"
                edits = simplify_edits(m2_block[1:])
                # Create a dict of edited token ids and labels
                tok_dict = create_token_labels(orig, edits)
                # Loop through orig tokens by id
                for i in range(0, len(orig)):
                    # Erroneous token
                    if i in tok_dict: out.write("\t".join([orig[i], tok_dict[i]])+"\n")
                    # Correct token
                    else: out.write("\t".join([orig[i], "-"])+"\n")
                # Write toks and labels to output
                out.write("\n")
                # Reset the block
                m2_block = []

# Parse command line arguments
def parse_args():
    # Define and parse program input
    parser = argparse.ArgumentParser()
    parser.add_argument("m2_file", help="The path to an M2 file.")
    parser.add_argument("-out", help="The path to the output conll file", required=True)
    args = parser.parse_args()
    return args
    
# Input: A list of M2 edit lines
# Output: A list of edit lists; [[o_start, o_end, cat, cor],...]
def simplify_edits(edits_in):
    edits_out = []
    for e in edits_in:
        e = e.split("|||")
        span = e[0].split()
        # Ignore noop, UNK edits
        if e[1] == "noop" or e[1] == "UNK": continue
        # Only process annotator 0 for now
        if e[-1] != "0": continue
        # Save the simplified edit
        edits_out.append([int(span[1]), int(span[2]), e[1], e[2]])
    return edits_out
    
# Input 1: A list of original tokens
# Input 2: A list of edits: [[o_start, o_end, cat, cor],...]
# Output: A dictionary; key is token id, value is label
def create_token_labels(orig, edits):
    tok_dict = {}
    # Loop through edits
    for e in edits:
        # Adjust missing word spans to have a non-zero range
        if e[0] == e[1]: e[1] += 1
        # Loop through the range of ids
        for i in range(e[0], e[1]):
            # Save the label on this token
            tok_dict[i] = e[2]
        # NOTE: Tokens that have multiple labels will end up with the last one
    return tok_dict

# Run the main function
if __name__ == "__main__":
    main()
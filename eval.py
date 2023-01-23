import argparse

def main():
    # Command line args
    args = parse_args()
    # Label name
    lname = "i"
    # True positive, false positive, false negative
    tp, fp, fn = 0, 0, 0

    # Open hyp and ref tsv files
    with open(args.hyp) as hyp_tsv, open(args.ref) as ref_tsv:
        # Process line by line in both files
        for hline, rline in zip(hyp_tsv, ref_tsv):
            # Get the hyp and ref info
            hyp_info = hline.strip()
            ref_info = rline.strip()
            # Ignore empty lines
            if not hyp_info or not ref_info: continue
            # Split on tab
            hyp_info = hyp_info.split("\t")
            ref_info = ref_info.split("\t")
            # Make sure this is the same token in both files
            assert hyp_info[0] == ref_info[0]
            # Get the hyp label and ref label
            hyp_label = hyp_info[1]
            ref_label = ref_info[1]
            # True Positive
            if hyp_label == ref_label == lname: tp += 1
            # Non-matching labels
            if hyp_label != ref_label:
                # False positive
                if hyp_label == lname: fp += 1
                # False negative
                if ref_label == lname: fn += 1

    # Calculate Precision, Recall and F_beta
    p, r, f = compute_fscore(tp, fp, fn, args.beta)
    # Print the overall results.
    print("")
    print('{:=^46}'.format(" Token-Based Detection "))
    print("\t".join(["TP", "FP", "FN", "Prec", "Rec", "F"+str(args.beta)]))
    print("\t".join(map(str, [tp, fp, fn, p, r, f])))
    print('{:=^46}'.format(""))
    print("")

# Parse command line args
def parse_args():
    parser = argparse.ArgumentParser(
        description="Calculate F-score for token-based error detection.",
        formatter_class=argparse.RawTextHelpFormatter,
        usage="%(prog)s [options] -hyp HYP -ref REF")
    parser.add_argument(
        "-hyp",
        help="A hypothesis tsv file.",
        required=True)
    parser.add_argument(
        "-ref",
        help="A reference tsv file.",
        required=True)
    parser.add_argument(
        "-b",
        "--beta",
        help="Value of beta in F-score. (default: 0.5)",
        default=0.5,
        type=float)
    args = parser.parse_args()
    return args

# Input 1-3: True positives, false positives, false negatives
# Input 4: Value of beta in F-score.
# Output 1-3: Precision, Recall and F-score rounded to 4dp.
def compute_fscore(tp, fp, fn, beta):
    p = float(tp)/(tp+fp) if fp else 1.0
    r = float(tp)/(tp+fn) if fn else 1.0
    f = float((1+(beta**2))*p*r)/(((beta**2)*p)+r) if p+r else 0.0
    return round(p, 4), round(r, 4), round(f, 4)

if __name__ == "__main__":
    main()

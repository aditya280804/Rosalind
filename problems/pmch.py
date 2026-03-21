def read_fasta(path):
    with open(path) as f:
        return ''.join(line.strip() for line in f if not line.startswith('>'))

import math
if __name__ == "__main__":
    seq = read_fasta("datasets/rosalind_pmch.txt")
    na = seq.count("A")
    ng = seq.count("G")
    nmatchings = (math.factorial(na)*math.factorial(ng))
    print(nmatchings)
    with open("output/rosalind_pmch.txt","w") as f:
        f.write(str(nmatchings))

def read_fasta(path):
    with open(path) as f:
        return "".join(line.strip() for line in f if not line.startswith('>'))
def ct_matches(n1,n2):
    nmin= min(n1,n2)
    nmax = max(n1,n2)
    prod = 1
    for _ in range(nmin):
        prod *= nmax
        nmax -= 1
    return prod
if __name__ == "__main__":
    seq = read_fasta("datasets/rosalind_mmch.txt")
    na, nu = seq.count("A"), seq.count("U")
    ng, nc = seq.count("G"), seq.count("C")

    tot = ct_matches(na, nu) * ct_matches(ng, nc)
    print(tot)
    with open("output/rosalind_mmch.txt","w") as f:
        f.write(str(tot))


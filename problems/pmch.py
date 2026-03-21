import math
if __name__ == "__main__":
    seq = ""
    with open("datasets/rosalind_pmch.txt","r") as f:
        for line in f:
            if line.startswith(">"):
                continue
            seq += line.strip()
    na = seq.count("A")
    ng = seq.count("G")
    nmatchings = (math.factorial(na)*math.factorial(ng))
    print(nmatchings)
    with open("output/rosalind_pmch.txt","w") as f:
        f.write(str(nmatchings))

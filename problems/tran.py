if __name__ == "__main__":
    seq = ""
    seqs = []
    with open("datasets/rosalind_tran.txt","r") as f:
        for i in f:
            if i.startswith(">"):
                if seq:
                    seqs.append(seq)
                    seq = ""
            else:
                seq+=i.strip()
    if seq:
        seqs.append(seq)
    tsi = 0
    tve = 0
    for i in range(len(seqs[0])):
        a = seqs[0][i]
        b = seqs[1][i]
        if a == b:
            continue
        else:
            if (a in ["A","G"] and b in ["C","T"]) or (a in ["C","T"] and b in ["A","G"]):
                tve +=1
            else:
                tsi +=1
    print(f"{tsi/tve:.11f}")
    with open("output/rosalind_tran.txt","w") as f:
        f.write(f"{tsi/tve:.11f}")

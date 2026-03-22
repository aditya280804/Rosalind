if __name__ == "__main__":
    with open("datasets/rosalind_sseq.txt","r") as f:
        seqs = []
        seq = ""
        for line in f:
            if line.startswith(">") and seq :
                seqs.append(seq)
                seq = ""
            if line.startswith(">"):
                continue
            seq+= line.strip()
    seqs.append(seq)
    s, mot = seqs
    motif_indices = []
    
    pos = 0
    for c in mot:
        while pos < len(s) and s[pos] != c:
            pos += 1
        if pos < len(s):
            motif_indices.append(pos + 1)
            pos += 1
    print(*motif_indices)
    with open("output/rosalind_sseq.txt","w") as f:
        f.write(" ".join(map(str,motif_indices)))



rna_table = {}
with open("datasets/rna_table.txt","r") as rna:
    data = rna.read().strip().split()
    for i in range(0,len(data),2):
        codon = data[i]
        amino = data[i+1]

        if amino in rna_table:
            rna_table[amino].append(codon)
        else:
            rna_table[amino]=[codon]
if __name__ == "__main__":
    mrna_len = 1
    with open("datasets/rosalind_mrna.txt","r") as f:
        prot_seq = f.read().strip()
    for i in prot_seq:
        mrna_len *= len(rna_table[i])
    mrna_len*=3
    with open("output/rosalind_mrna.txt","w") as file:
        file.write(f"{mrna_len % 10**6}")
    print(mrna_len % 10**6, mrna_len)

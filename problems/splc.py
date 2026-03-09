import json
protein_table = {}
with open("datasets/rna_table.txt","r") as rna:
    data = rna.read().strip().split()
    for i in range(0,len(data),2):
        codon = data[i]
        amino = data[i+1]

        protein_table[codon] = amino
with open('datasets/protein_table.json', 'w') as f:
    json.dump(protein_table, f, indent=4) 
with open('datasets/protein_table.json', 'r') as f:
    PROTEIN_TABLE = json.load(f)
if __name__ == "__main__":
    with open("datasets/rosalind_splc.txt","r") as f:
        k = 0
        introns = []
        DNA_str = ""
        for i in f:
            if i[0] == ">":
                k +=1
                continue
            elif k == 1:
                DNA_str = DNA_str+i.strip()
                continue
            introns.append(i.strip())
    print(introns)
    to_rem =[]
    for intron in introns:
        DNA_str = DNA_str.replace(intron, "")
    DNA_str = DNA_str.replace("T","U")
    protein = ""

    for j in range(0, len(DNA_str)-2, 3):
        codon = DNA_str[j:j+3]
        aa = PROTEIN_TABLE[codon]

        if aa == "Stop":
            continue

        protein += aa

    print(protein)

    with open("output/rosalind_splc.txt","w") as f:
        f.write(protein + "\n")

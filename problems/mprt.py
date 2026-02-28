import requests
import re
f = open("datasets/rosalind_mprt.txt","r")
file = open("output/rosalind_mprt.txt","w")
for i in f.readlines():
    i = i.strip()
    id = i.split("_")
    response = requests.get(f"http://www.uniprot.org/uniprot/{id[0]}.fasta")
    response.raise_for_status()
    string = response.text
    for ins in range(len(string)):
        if string[ins] == "\n":
            string = ("".join(string[ins:].strip().split("\n")))
            break
    locations = []
    for j in re.finditer("(?=N[^P][ST][^P])",string):
        locations.append(j.start())
    if locations:
        file.write(i + "\n")
        file.write(" ".join(str(pos + 1) for pos in locations))
        file.write("\n")

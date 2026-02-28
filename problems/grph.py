def solve(suff,pref):
    orderedpair = []
    for keys,values in suff.items():
        for keyp,valuep in pref.items():
            if keyp == keys:
                continue
            if values == valuep:
                orderedpair.append([keyp,keys])
    return orderedpair



if __name__ == "__main__":
    f = open("datasets/rosalind_grph.txt","r")
    file = open("output/rosalind_grph.txt","w")
    suff = {}
    pref = {}
    string = ""
    name = ""
    for i in f.readlines():
        line = i.strip()
        if line[0] == ">":
            if string != "":
                suff[name]=[string[:3]]    
                pref[name]=[string[-3:]]
                string = ""
            name = line[1:]
        else:
            string=string + line
    suff[name]=[string[:3]]    
    pref[name]=[string[-3:]]
    print(suff,"\n",pref)
    orderedpair = solve(suff,pref)
    for i in orderedpair:    
        print(*i)
        file.write(" ".join(i)+"\n")

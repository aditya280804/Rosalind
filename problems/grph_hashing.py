import time
start = time.time()
if __name__ == "__main__":
    f = open("datasets/rosalind_grph.txt","r")
    file = open("output/rosalind_grph_hash.txt","w")
    suff = {}
    pref = {}
    string = ""
    name = ""
    for i in f.readlines():
        line = i.strip()
        if line[0] == ">":
            if string != "":
                prefix = string[:3]
                suffix = string[-3:]
                if prefix in suff:
                    suff[prefix].append(name)
                else:
                    suff[prefix] = [name]
                if suffix in pref:
                    pref[suffix].append(name)
                else:
                    pref[suffix] = [name]
                string = ""
            name = line[1:]
        else:
            string=string + line
    prefix = string[:3]
    suffix = string[-3:]

    if prefix in suff:
        suff[prefix].append(name)
    else:
        suff[prefix] = [name]

    if suffix in pref:
        pref[suffix].append(name)
    else:
        pref[suffix] = [name]
    for keysuf,valuesuf in suff.items():
        if keysuf in pref.keys():
            for i in pref[keysuf]:
                for j in suff[keysuf]:
                    if i !=j:
                        print(i,j)
                        file.write(i+" "+j+"\n")
end = time.time()
print(end-start)


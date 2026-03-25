if __name__ == "__main__":
    edges = []
    with open("datasets/rosalind_tree.txt","r") as f:
        n = int(f.readline().strip())
        for line in f:
            edges.append(tuple(map(int, line.strip().split())))
    grph = [[_] for _ in range(1,n+1)]
    gpa = gpb = None
    for a,b in edges:
        for gpn,gp in enumerate(grph):
            flag = 0
            if a in gp:
                gpa = gpn
                if flag == 1:
                    break
                else:
                    flag =1
                    continue
            if b in gp:
                gpb = gpn
                if flag == 1:
                    break
                else:
                    flag =1
                    continue
        if gpa is not None and gpb is not None and gpa != gpb:
            grph[gpa].extend(grph[gpb])
            grph.pop(gpb)
    print(len(grph)-1)
    with open("output/rosalind_tree.txt","w") as f:
        f.write(f"{len(grph)-1}")
            

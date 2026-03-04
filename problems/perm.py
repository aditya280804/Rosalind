def permute(cur,rem,f):
    if not rem:
        f.append(cur)
        return
    for i in range(len(rem)):
        new_cur = cur + [rem[i]]
        new_rem = rem[:i] + rem[i+1:]
        permute(new_cur,new_rem,f)
if __name__ == "__main__":
    with open("datasets/rosalind_perm.txt","r") as file:
        n = int(file.read().strip())
    n_s = list(range(1, n+1))
    op = []
    permute([],n_s,op)
    with open("output/rosalind_perm.txt","w") as f:
        f.write(str(len(op)) + "\n")
        for p in op:
            f.write(" ".join(map(str, p)) + "\n")

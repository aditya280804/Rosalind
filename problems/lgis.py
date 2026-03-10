def solve(perm, f, n):
    inc = [[] for _ in range(n)]
    inc[0].append(perm[0])
    for i in range(1,n):
        for j in range(i):
            if perm[j] < perm[i] and len(inc[i]) < len(inc[j]):
                inc[i] = inc[j].copy()
        inc[i].append(perm[i])

    best = max(inc, key=len)
    best = [abs(x) for x in best]

    print(best)
    f.write(" ".join(map(str, best)) + "\n")

if __name__ == "__main__":
    with open("datasets/rosalind_lgis.txt","r") as f:
        n = int(f.readline().strip())
        perm = map(int,f.readline().strip().split(" "))
    perm = list(perm)
    with open("output/rosalind_lgis.txt","w") as f:
        perm_neg= [-per for per in perm]
        solve(perm,f,n)
        solve(perm_neg,f,n)

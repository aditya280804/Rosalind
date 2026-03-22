if __name__ == "__main__":
    with open("datasets/rosalind_pper.txt","r") as f:
        n,k = map(int,f.readline().split(" "))
    prod = 1
    for _ in range(k):
        prod = (prod*n)
        n-=1
    print(prod%1000000)
    with open("output/rosalind_pper.txt","w") as f:
        f.write(f"{prod%1000000}")

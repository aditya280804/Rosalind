def recur(n,letters,curr,f):
    if n == 0:
        print(curr)
        f.write(f"{curr}")
        f.write("\n")
        # at the end when n == 0 write the string to file
    else:
        for i in letters:
            recur(n-1,letters,curr+i,f)
        # append all the letters to the existing string (curr)
        # to create all permutations and call it n more times
if __name__ == "__main__":
    with open("datasets/rosalind_lexf.txt") as f:
        letters = sorted(f.readline().strip().split())
        n = int(f.readline().strip())
    with open("output/rosalind_lexf.txt","w") as file:
        recur(n,letters,"",file)
    

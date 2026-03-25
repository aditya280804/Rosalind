if __name__ == "__main__":
    with open("datasets/rosalind_ini6.txt","r") as f:
        string = f.readline().split()
    dictionary = {}
    for i in string: 
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    with open("output/rosalind_ini6.txt","w") as f:
        for i,k in dictionary.items():
            print(i,k)
            f.write(f"{i} {k}"+"\n")

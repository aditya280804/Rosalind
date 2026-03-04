if __name__ == "__main__":
    with open("datasets/rosalind_iev.txt","r")as f:
        i = list(map(int,f.read().strip().split()))
    print((i[0]+i[1]+i[2])*2+(i[3]*3)/2+i[4])
    with open("output/rosalind_iev.txt","w")as file:
        file.write(f"{(i[0]+i[1]+i[2])*2+(i[3]*3)/2+i[4]}")

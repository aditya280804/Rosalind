if __name__ == "__main__":
    seq =""
    sequences = []
    same = False
    start = 0
    with open("datasets/rosalind_lcsm.txt","r") as f:
        for i in f:
            if i.startswith(">") and seq!="":
                sequences.append(seq)
                seq=""
                continue
            elif i.startswith(">") and seq=="":
                continue
            else:
                seq+=i.strip()
    sequences.append(seq)   
    shortest = min(sequences, key=len)
    sequences.remove(shortest)
    sequences.sort(key=len)
    longest = ""
    for length in range(len(shortest),0,-1):# iterate over all subsequences of the shortest sequence
        for start in range(len(shortest)-length +1):
            flag = 0
            candidate = shortest[start:start+length]
            for i in sequences:
                if candidate not in i:
                    flag = 1
                    break  #stop if not found in any sequence
            if flag ==0:
                longest = candidate
                break
        if longest != "":
            break
    print(longest)
    with open("output/rosalind_lcsm.txt","w")as file:
        file.write(f"{longest}")

import math
def perms(curr,rem,output):
    if rem:
        for idx, i in enumerate(rem):
            curr_temp = curr + [i]
            rm_temp = rem[:idx] + rem[idx+1:]
            output = perms(curr_temp, rm_temp, output)

    else:
        n = len(curr)
        for mask in range(1<<n): # iterate over 2^n bitwise masks 
            temp = curr.copy()
            for pos in range(n):
                if mask & (1<<pos): # anding 2^pos with masks gives all possible sign combinations 
                    temp[pos] = -temp[pos]
            output.append(tuple(temp))
    return output


if __name__ == "__main__":
    with open("datasets/rosalind_sign.txt","r") as f:
        n = int(f.read().strip())
    elements = [x for x in range(1,n+1)]
    output = []
    output = perms([],elements,output)
    with open("output/rosalind_sign.txt","w") as f:
        print(math.factorial(n)*pow(2,n))
        f.write(f"{math.factorial(n)*pow(2,n)}"+"\n")
        for i in output:
            print(*i)
            f.write(" ".join(map(str,i))+"\n")
    

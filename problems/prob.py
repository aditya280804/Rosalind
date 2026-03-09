import math
def calc_probs(ATct,CGct,n):
    return math.log10(pow((1-n)/2,ATct)*pow(n/2,CGct))    
if __name__ == "__main__":
    with open("datasets/rosalind_prob.txt","r") as f:
        seq = f.readline().strip()
        probs = f.readline().strip().split(" ")
    ATct = seq.count("A")+seq.count("T")
    CGct = seq.count("C")+seq.count("G")
    with open("output/rosalind_prob.txt","w") as f:
        for prob in probs:
            p_new =calc_probs(ATct, CGct, float(prob)) 
            print(f"{p_new:.3f}")
            f.write(f"{p_new:.3f}")
            f.write(" ")
    

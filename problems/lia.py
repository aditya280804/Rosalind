import math

if __name__ == "__main__":
    with open("datasets/rosalind_lia.txt","r") as f:
        k, n = map(int, f.read().strip().split())
    pop = 2**k
    probability = 0
    for i in range(0, n):
        comb = math.factorial(pop) / (math.factorial(i) * math.factorial(pop - i)) #Use a binomial distribution to find probabilites 
        prob = comb * (0.25 ** i) * (0.75 ** (pop - i))
        probability += prob
    probability = 1 - probability

    with open("output/rosalind_lia.txt","w") as file:
        file.write(f"{probability:.3f}")

import time
f = open("datasets/rosalind_fibd.txt","r")
n,m = f.read().split()
memo={}
def fact(n,m):
    if n <=0:
        return [0,0]
    if n ==1:
        return [1,1]
    if n ==2:
        return [1,0]
    if n in memo:
        return memo[n]
    else:
        N1 = fact(n-1,m)[0]+fact(n-1,m)[0]-fact(n-1,m)[1]-fact(n-m,m)[1]
        N2 = fact(n-1,m)[0]-fact(n-1,m)[1]
        memo[n]= N1,N2
        return [N1,N2]

        
print(fact(int(n),int(m))[0])
file = open("output/rosalind_fibd.txt","w")
file.write(str(fact(int(n),int(m))[0]))

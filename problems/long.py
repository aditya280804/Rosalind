# compute suffix-prefix overlaps between every pair of reads
# for each read keep the partner with the largest overlap
# the read whose best overlap is smallest is likely the start of the chain
# then reconstruct the superstring by following the overlap links
def find_next(PS_dict,curr,least_olp):
    for i,k in PS_dict.items():
        if i == least_olp:
            continue
        if k[0] == curr:
            return i
if __name__ == "__main__":
    seqs = []
    seq = ""

    with open("datasets/rosalind_long.txt") as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if seq:
                    seqs.append(seq)
                    seq = ""
            else:
                seq += line

    if seq:
        seqs.append(seq)
    pre_suf_len = {}
    for i in range(len(seqs)):
        for j in range(len(seqs)):
            if j == i:
                continue
            up = seqs[i] #prefix
            dn = seqs[j] #suffix
            maxnum = 0
            for num in range(min(len(up), len(dn)), 0, -1):
                if dn[-num:] == up[:num]:
                    maxnum = num
                    break
            if up not in pre_suf_len or maxnum > pre_suf_len[up][1]:
                pre_suf_len[up] = (dn, maxnum)
    minlen = 1000
    least_olp = ""
    for i,k in pre_suf_len.items():
        if k[1]<minlen:
            least_olp = i
            minlen = k[1]
    curr = least_olp # first in sequence
    next_seq = find_next(pre_suf_len,curr,least_olp)
    op = curr
    #del pre_suf_len[curr]
    for _ in range(len(pre_suf_len)-1):
        d = pre_suf_len[next_seq][1]
        op += next_seq[d:]
        curr = next_seq
        next_seq = find_next(pre_suf_len,curr,least_olp)
    print(op)
    with open("output/rosalind_long.txt","w") as file:
        file.write(op)

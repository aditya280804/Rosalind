comp = {"A":"T","T":"A","G":"C","C":"G"}
def read_fasta(file):
    sequence = ""
    with open(file) as f:
        for line in f:
            if not line.startswith(">"):
                sequence += line.strip()
    return sequence



def find_palindromes(sequence):
    results = []
    for i in range(len(sequence)):
        for length in range(4,13,2):
            if i + length <= len(sequence):
                subseq = sequence[i:i+length]
                if is_reverse_palindrome(subseq):
                    results.append((i+1,length))
    return results

def is_reverse_palindrome(sequence):
    for i in range(len(sequence)//2):
        if sequence[i] != comp[sequence[-(i+1)]]:
            return False
    return True

if __name__ == "__main__":
    sequence = read_fasta("datasets/rosalind_revp.txt")
    results = find_palindromes(sequence)
    with open("output/rosalind_revp.txt", "w") as out:
        for pos, length in results:
            print(pos, length)
            out.write(f"{pos} {length}\n")

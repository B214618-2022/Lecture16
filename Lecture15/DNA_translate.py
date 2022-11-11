#!/bin/python3

print("\n Codons: \n")

input = 'ATGTTCGGTGNN'
dna_sequence = input.upper()

gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

#chunks, chunk_size = len(input), int(len(input)/3)
#codons = [ input[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
window = 3
offset = 3
seq_len = len(input)
start_point = 0
end_point = window
codons = []
count = 0

def dna_list(some_dna):
    temp_dna = []
    for base in some_dna:
        temp_dna.append(base)
    return temp_dna

def dna_reverse(some_dna_list):
    length = len(some_dna_list)
    for base in some_dna_list:
        if base == "A":
            some_dna_list[count] = "T"
        elif base == "T":
            some_dna_list[count] = "A"
        elif base == "C":
            some_dna_list[count] = "G"
        elif base == "G":
            some_dna_list[count] = "C"
        else:
            some_dna_list[count] = "N"
    count = count + 1
    return some_dna_list

while start_point < len(input):
    codon = input[start_point:end_point]
    codons.append(codon)
    start_point = start_point + offset
    end_point = end_point + offset

print(codons)
p_sequence = []

for codon in codons:
    if len(codon) == 3:
        try:
            amino = gencode[codon]
            p_sequence.append(amino)
        except(KeyError):
            p_sequence.append("N")

print("\n zero frame: \n")
print("".join(p_sequence))

print("\n Forward frames: \n")

print(dna_sequence)
print(dna_reverse(dna_list(dna_sequence)))

import sys
from Bio import SeqIO

if len(sys.argv) != 2:
    print("Usage: python fasta_to_phylip.py input_file.fasta")
    sys.exit(1)

input_file = sys.argv[1]
output_file = input_file.rsplit(".", 1)[0] + ".phy"

sequences = list(SeqIO.parse(input_file, "fasta"))

with open(output_file, "w") as outfile:
    outfile.write(f"{len(sequences)} {len(sequences[0].seq)}\n")
    for sequence in sequences:
        outfile.write(f"{sequence.id} {str(sequence.seq)}\n")

print(f"Conversion complete. Output file: {output_file}")

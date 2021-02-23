def to_rna(dna_strand):
    dna_strand = dna_strand.replace("G", "c")
    dna_strand = dna_strand.replace("C", "g")
    dna_strand = dna_strand.replace("T", "a")
    dna_strand = dna_strand.replace("A", "u")
    dna_strand = dna_strand.upper()
    return dna_strand
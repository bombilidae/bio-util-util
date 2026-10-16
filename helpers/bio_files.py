def convert_fasta(input_fasta: str, output_fasta: str) -> None:
    """Write each FASTA sequence on one line.

    Args:
        input_fasta: Input FASTA file.
        output_fasta: Output FASTA file.
    """
    with open(input_fasta) as in_fasta:
        with open(output_fasta, "w") as out_fasta:
            seq = ""
            header = ""
            for line in in_fasta:
                line = line.strip()
                if line.startswith(">"):
                    if header != "":
                        out_fasta.write(seq + "\n")
                    out_fasta.write(line + "\n")
                    header = line
                    seq = ""
                else:
                    seq = seq + line
            if header != "":
                out_fasta.write(seq + "\n")

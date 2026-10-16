import os

from helpers import fastq, bio_files


def filter_fastq(
    input_fastq: str,
    output_fastq: str,
    gc_bounds: float | tuple[float, float] = (0, 100),
    length_bounds: float | tuple[float, float] = (0, 2**32),
    quality_threshold: float = 0,
) -> None:
    """Filter reads and save the result.

    Args:
        input_fastq: Input file path.
        output_fastq: Output file name.
        gc_bounds: GC percentage limits.
        length_bounds: Sequence length limits.
        quality_threshold: Minimum average quality.
    """
    gc_low, gc_high = fastq.bounds_tuple(gc_bounds)
    len_low, len_high = fastq.bounds_tuple(length_bounds)

    if not os.path.isdir("filtered"):
        os.mkdir("filtered")

    out_path = os.path.join("filtered", output_fastq)

    with open(input_fastq) as fastq_file:
        with open(out_path, "w") as out_fastq_file:
            while True:
                read = fastq.read_fastq(fastq_file)
                if read is None:
                    break
                header, seq, qual = read
                if (
                    fastq.gc_filter(seq, gc_low, gc_high)
                    and fastq.len_filter(seq, len_low, len_high)
                    and fastq.qual_filter(qual, quality_threshold)
                ):
                    out_fastq_file.write(f"{header}\n{seq}\n+\n{qual}\n")


def convert_multiline_fasta_to_oneline(
    input_fasta: str, output_fasta: str | None = None
) -> None:
    """Save FASTA sequences in one line each.

    Args:
        input_fasta: Input FASTA file.
        output_fasta: Output file name, if needed.
    """
    if output_fasta is None:
        output_fasta = input_fasta + "_oneline.fasta"
    bio_files.convert_fasta(input_fasta, output_fasta)

def read_fastq(fastq_file) -> tuple[str, str, str] | None:
    """Read one FASTQ record.

    Args:
        fastq_file: Open FASTQ file.

    Returns:
        Header, sequence and quality, or None.
    """
    header = fastq_file.readline().strip()
    if not header:
        return None
    seq = fastq_file.readline().strip()
    fastq_file.readline()
    qual = fastq_file.readline().strip()
    return header, seq, qual


def bounds_tuple(gc_bounds: float | tuple[float, float]) -> tuple[float, float]:
    """Get the lower and upper limits.

    Args:
        gc_bounds: One number or two limits.

    Returns:
        lower and upper limit.
    """
    if isinstance(gc_bounds, (int, float)):
        low = 0
        high = gc_bounds
    elif isinstance(gc_bounds, tuple):
        low, high = gc_bounds
    return low, high


def gc_filter(seq: str, low: float, high: float) -> bool:
    """Check the GC percentage.

    Args:
        seq: DNA sequence.
        low: Lower limit.
        high: Upper limit.

    Returns:
        True if it fits or False.
    """
    if not seq:
        return False
    gc_num = seq.count("G") + seq.count("C")
    gc_percent = (gc_num / len(seq)) * 100
    return low <= gc_percent <= high


def len_filter(seq: str, low: float, high: float) -> bool:
    """Check the sequence length.

    Args:
        seq: DNA sequence.
        low: Shortest allowed length.
        high: Longest allowed length.

    Returns:
        True if it fits or False.
    """
    return low <= len(seq) <= high


def qual_filter(qual: str, threshold: float) -> bool:
    """Check the average quality.

    Args:
        qual: Quality string.
        threshold: Minimum quality.

    Returns:
        True if it passes or False.
    """
    if not qual:
        return False
    total_score = 0
    for i in qual:
        i_ascii = ord(i)
        total_score += i_ascii - 33
    mean_qual = total_score / len(qual)
    return mean_qual >= threshold

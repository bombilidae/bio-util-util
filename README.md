# FASTQ filter and FASTA converter

This project has two functions: one filters FASTQ reads, and the other puts FASTA sequences on one line each. Both work through the files one sequence at a time.

## Requirements

Python 3.10 or newer. No extra libraries are needed.

## Filter FASTQ reads

Use `filter_fastq()` to keep only the reads you need. It checks GC content, sequence length, and average quality.

Open Python in the project folder and run:

```python
from main import filter_fastq

filter_fastq("reads.fastq", "result.fastq", (40, 60), (50, 300), 30)
```

This keeps reads with 40–60% GC, 50–300 bases, and average quality of at least 30. The result is saved as `filtered/result.fastq`. The `filtered` folder is created automatically.

The arguments are:

- `input_fastq`: FASTQ file to read.
- `output_fastq`: name of the new file in the `filtered` folder.
- `gc_bounds`: allowed GC percentage, for example `(40, 60)`.
- `length_bounds`: allowed sequence length, for example `(50, 300)`.
- `quality_threshold`: minimum average quality score.

The last three arguments are optional. By default, GC can be 0–100%, length can be 0–2**32 bases, and minimum average quality is 0. Reads with empty sequences or quality strings are not kept. You can also use a single upper limit: `gc_bounds=60` means 0–60% GC.

## Convert FASTA to one line

Use `convert_multiline_fasta_to_oneline()` when a FASTA sequence is split across several lines and you want each sequence on a single line.

```python
from main import convert_multiline_fasta_to_oneline

convert_multiline_fasta_to_oneline("sequences.fasta", "oneline.fasta")
```

The first argument is the input FASTA file. The second is the output file and can be omitted:

```python
convert_multiline_fasta_to_oneline("sequences.fasta")
```

In this case, the output is named `sequences.fasta_oneline.fasta`. The input file is not changed.

# Needleman–Wunsch.Py

The Needleman–Wunsch algorithm is a dynamic programming method to perform nucelotide or protein sequencing. This simple Python script (hopefully a package), will allow you to perform sequence alignment as a command line utility.

Visualization of the algorithm:

![Algorithm demonstration](https://upload.wikimedia.org/wikipedia/commons/3/3f/Needleman-Wunsch_pairwise_sequence_alignment.png)

## Usage

To use this command line utility, clone the repo and run:

```bash
python run.py --seq1 ACTCG --seq2 ACAGTAG --match 1 --mismatch 0 --gap -1
```

You can run a sequence of any length and insert your own scoring scheme.

## Features

The currently supported features are:

* Displaying scoring matrix
* Displaying direction matrix (slightly broken)

Future features include:

* Displaying final sequence alignment
* Making it into a true Python package

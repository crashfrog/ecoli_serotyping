#!/usr/bin/env python

"""
    Definitions for the ectyper project
"""

import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, 'Data')
WORKPLACE_DIR = os.getcwd()

SEROTYPE_FILE = os.path.join(DATA_DIR, 'ectyper_data.fasta')
SEROTYPE_ALLELE_JSON = os.path.join(DATA_DIR, 'ectyper_dict.json')
COMBINED = os.path.join(DATA_DIR, 'combined.fasta')

ECOLI_MARKERS = os.path.join(DATA_DIR, 'ecoli_specific_markers.fasta')
SAMTOOLS = 'samtools'
REFSEQ_SUMMARY = os.path.join(DATA_DIR, 'assembly_summary_refseq.txt')
REFSEQ_SKETCH = os.path.join(DATA_DIR, 'refseq.genomes.k21s1000.msh')

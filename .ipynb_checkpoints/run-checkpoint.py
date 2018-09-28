#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse, json, os
import numpy as np


parser = argparse.ArgumentParser()
parser.add_argument('--seq1')
parser.add_argument('--seq2')
parser.add_argument('--match')
parser.add_argument('--mismatch')
parser.add_argument('--gap')

def initialize(matrix_type, len_seq1, len_seq2):
    if matrix_type == 0:
        matrix = np.zeros((len_seq2 + 1, len_seq1 + 1))
        #First row
        for i, cell in enumerate(matrix[0]):
            if i != 0:
                matrix[0, i] = cell + (-1 * i)
        #First column
        for i, cell in enumerate(matrix[:,0]):
            if i != 0:
                matrix[i, 0] = cell + (-1 * i)
        matrix[1:,1:] = np.nan
        return matrix
    else:
        matrix = np.chararray((len_seq2 + 1, len_seq1 + 1), itemsize=2, unicode=True)
        matrix[:,:] = 0
        for i, cell in enumerate(matrix[0]):
            if i != 0:
                matrix[0, i] = str(np.float(cell) + (-1 * i))
        #First column
        for i, cell in enumerate(matrix[:,0]):
            if i != 0:
                matrix[i, 0] = np.float(cell) + (-1 * i)
        return matrix

def find_score(diagonol, left, top, codon_1, codon_2, match, mismatch, gap):
    result = []

    def find_d_score(diagonol, codon_1, codon_2):
        return diagonol + match if codon_1 == codon_2 else diagonol + mismatch
    find_h_score = lambda left: left + gap
    find_v_score = lambda top: top + gap

    d_score = find_d_score(diagonol, codon_1, codon_2)
    h_score = find_h_score(left)
    v_score = find_v_score(top)
    
    scores = [d_score, h_score, v_score]
    
    max_score = max(scores)
    result.append(max_score)
    
    indexes = [i for i, s in enumerate(scores) if max_score == scores]
    
    directions = []
    for i in indexes:
        if i == 0:
            directions.append('↖')
        elif i == 1:
            directions.append('←')
        elif i == 2:
            directions.append('↑')
    results.append(directions)
    return result



def main(args):
    try:
        seq1 = args.seq1
        seq2 = args.seq2
        len_seq1 = len(seq1)
        len_seq2 = len(seq2)
        match = float(args.match)
        mismatch = float(args.mismatch)
        gap = float(args.gap)

        score_matrix = initialize(0, len_seq1, len_seq2)
        direction_matrix = initialize(1, len_seq1, len_seq2)

        for i, row in enumerate(score_matrix):
            if i != 0:
                codon2 = seq2[i - 1]
                for j, value in enumerate(row):
                    if (j != 0):
                        d = score_matrix[i - 1, j - 1]
                        v = score_matrix[i - 1, j]
                        h = row[j - 1]
                        codon1 = seq1[j - 1]
                        result = find_score(d, h, v, codon1, codon2, match, mismatch, gap)
                        score_matrix[i, j] = result[0]
                        #direction_matrix[i, j] = result[1].decode('utf-8')
        print(score_matrix)
        #print(direction_matrix)
        return True
    except():
        return False

if __name__ == '__main__':
    args = parser.parse_args()
    print(args)
    main(args)

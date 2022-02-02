"""
Program that produces an array of the maximum
alignment scores of two gene sequences.

author: Reis Gadsden
version: 2022/02/02
class: CS-5531-101
instructor: Dr. Mohebbi
"""
import numpy as np


def main():
    """
    ## user input could be implemented
    s1 = input("Set the sequence of S1: ")
    ## verify input

    s2 = input("Set the sequence of S2: ")
    ## verify input
    """
    s1 = "acgu"
    s2 = "cgau"
    max_align_score = seq_align(s1, s2)
    print(np.matrix(max_align_score))

def seq_align(s1, s2):
    s1 = "-" + s1
    s2 = "-" + s2
    align_score_matrix = np.zeros([len(s1), len(s2)])
    backtracking_matrix = np.zeros([len(s1), len(s2)])
    for i in range(0, len(s1)):
        for j in range(0, len(s2)):
            if i == 0:
                align_score_matrix[i][j] = j * -6
                insert_backtracking(backtracking_matrix, i, j, "<-");
            elif j == 0:
                align_score_matrix[i][j] = i * -6
            else:
                val = 0
                diagonal = align_score_matrix[i - 1][j - 1]
                if s1[i] == s2[j]:
                    val = diagonal + 5
                else:
                    val = diagonal - 2

                if (align_score_matrix[i-1][j] - 6) > val:
                    val = align_score_matrix[i - 1][j] - 6

                if (align_score_matrix[i][j - 1] - 6) > val:
                    val = align_score_matrix[i][j - 1] - 6

                align_score_matrix[i][j] = val

    return align_score_matrix


def insert_backtracking(matrix, i, j, direction):
    if i == 0 and j == 0:
        matrix[0][0] = 0

if __name__ == "__main__":
    main()
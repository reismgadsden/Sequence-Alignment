"""
Program that produces an array of the maximum
alignment scores of two gene sequences.

author: Reis Gadsden
version: 2022/02/02
class: CS-5531-101
instructor: Dr. Mohebbi
"""
import numpy as np
encoding="utf-8"

def main():
    """
    ## user input could be implemented
    s1 = input("Set the sequence of S1: ")
    ## verify input

    s2 = input("Set the sequence of S2: ")
    ## verify input
    """
    s1 = "AGGCGGCCAUCGCGGCGGGGUUCCUCCCGUACCCAUCCCGAACACGGAAGAUAAGCCUGCCUGCGUAUUGGUGAGUACUGGAGUGGGAGACCCUCUGGGAGAGCCGAUUCGCCGCC"
    s2 = "UGGCGGCCAUAGCGGAGGGGCCAUACCUGGUCUCGUUUCGAUCCCAGAAGUGAAGUCCUCCUGCGUUUUGUUGUUGUACUGUGGACGAGAGUCUAUGGGAAGCUCAUAACGCUGCCGGCC"
    max_align_score, backtrack = seq_align(s1, s2)

    ## print functions that show the alignment and back tracking matrices
    # print("Alignment Score Matrix")
    # for x in max_align_score:
    #     print(x)
    # print("\nBacktracking Matrix")
    # for x in backtrack:
    #     for y in x:
    #         print(y.decode().strip("b").strip("'"), end=" ")
    #     print()
    # print("\nAligned Sequences")
    s1New, s2New = buildStrings(s1, s2, backtrack)
    print("Alignment Score: " + str(max_align_score[len(s1)][len(s2)]))

    i = 0
    totalAlignments = 0
    while i != len(s1New):
        if s1New[i] == s2New[i]:
            totalAlignments += 1
        i += 1
    print("Total # of Alignments: " + str(totalAlignments))
    print("S1: " + s1New)
    print("S2: " + s2New)

def seq_align(s1, s2):
    s1 = "-" + s1
    s2 = "-" + s2
    align_score_matrix = np.zeros([len(s1), len(s2)])
    backtracking_matrix = np.chararray([len(s1), len(s2)])
    for i in range(0, len(s1)):
        for j in range(0, len(s2)):
            if i == 0:
                align_score_matrix[i][j] = j * -6
                insert_backtracking(backtracking_matrix, i, j, '_');
            elif j == 0:
                align_score_matrix[i][j] = i * -6
                insert_backtracking(backtracking_matrix, i, j, '|');
            else:
                insert_backtracking(backtracking_matrix, i, j, '\\');

                val = 0
                diagonal = align_score_matrix[i - 1][j - 1]
                if s1[i] == s2[j]:
                    val = diagonal + 5
                else:
                    val = diagonal - 2

                if (align_score_matrix[i-1][j] - 6) > val:
                    val = align_score_matrix[i - 1][j] - 6
                    insert_backtracking(backtracking_matrix, i, j, '|');

                if (align_score_matrix[i][j - 1] - 6) > val:
                    val = align_score_matrix[i][j - 1] - 6
                    insert_backtracking(backtracking_matrix, i, j, '_');

                align_score_matrix[i][j] = val

    return align_score_matrix, backtracking_matrix


def insert_backtracking(matrix, i, j, direction):
    if i == 0 and j == 0:
        matrix[0][0] = '0'
    else:
        matrix[i][j] = direction
   ## return matrix

def buildStrings(s1, s2, backtrack):
    i = len(s1)
    j = len(s2)
    s1New = ""
    s2New = ""
    num_aligned = 0
    while True:
        back_symbol = backtrack[i][j].decode("utf-8")
        if back_symbol == '\\':
            s1New = s1[i - 1] + s1New
            s2New = s2[j - 1] + s2New
            i -= 1
            j -= 1
        elif  back_symbol == '_':
            s1New = "-" + s1New
            s2New = s2[j - 1] + s2New
            j -= 1
        elif back_symbol == '|':
            s1New = s1[i - 1] + s1New
            s2New = "-" + s2New
            i -= 1
        else:
            break
    return s1New, s2New

if __name__ == "__main__":
    main()
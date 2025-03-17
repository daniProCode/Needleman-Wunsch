import csv
import sys

#Intialize matrix given rows, columns, and penalty number
def init_matrix(r, c, d): 
    m = [[0 for i in range(r+1)] for j in range(c+1)]

    for i in range(len(m[0])):
        m[0][i] = i*d

    for i in range(len(m)):
        m[i][0] = i*d
    
    return m

#This function returns 1 if both characters are a match and -1 if they're a mismatch.
def is_match(a, b):
    if a == b:
        return 1
    else:
        return -1

# Algorithm implementation. s1 and s2 represent the sequences and d is the gap penalty assigned.
# s1 is rows, s2 columns
def NW_align (s1, s2, d):
    m = init_matrix(len(s2),len(s1),-2)  # 2d array, rows = sequence 2, columns = sequence 1 
    r = len(s1)                          # rows
    c = len(s2)                          # columns

    # This loop will complete the Needleman-Wunsch matrix
    for i in range(1,r+1):
        for j in range(1,c+1):
            # Evaluate for up, left, and diagonal and set current cell's value to the maximum 
            # value between the three
            n1 = m[i-1][j-1] + is_match(s1[i-1], s2[j-1])   # Diagonal, calls is_match function to determine what should be added
            n2 = m[i-1][j] + d                              # Up
            n3 = m[i][j-1] + d                              # Left

            m[i][j] = max(n1,n2,n3)                         # Set max value
    curr_r = i          # Current Row
    curr_c = j          # Current Column
    align_score = m[i][j]
# For debugging purposes
    for i in m:
        print(i)
    
    s1_temp = s1  
    s2_temp = s2 
    s1_align = ''   # Alignment for sequence 1
    s2_align = ""      # Alignment for sequence 2

    while curr_r > 0 or curr_c > 0 or s1_temp == '' or s2_temp == '':
        curr_v = m[curr_r][curr_c]                                              # Current Value
        # Backtracking values
        diagonal_v = m[curr_r-1][curr_c-1] + is_match(s1_temp[-1],s2_temp[-1])  # Diagonal Value
        up_v =  m[curr_r-1][curr_c] + d                                         # Upper Value
        left_v = m[curr_r][curr_c-1] + d                                        # Left Value
        max_v = max(diagonal_v, up_v, left_v)

        # If statements done with bias for left value
        
        
        if max_v == left_v:
            # If left value is maximum, add a gap in sequence 1 and add corresponding letter to sequence 2
            s2_align = s2_temp[-1] + s2_align
            s1_align = '-' + s1_align
            s2_temp = s2_temp[:-1]
            curr_c -= 1

        elif max_v == up_v:
            # If right value is maximum, add a gap in sequence 2 and add corresponding letter to sequence 1
            s1_align = s1_temp[-1] + s1_align
            s2_align = '-' + s2_align
            s1_temp = s1_temp[:-1]
            curr_r -= 1

        else:
            # If diagonal value is maximum, add corresponding letter to both sequences
            s2_align = s2_temp[-1] + s2_align
            s1_align = s1_temp[-1] + s1_align
            s2_temp = s2_temp[:-1]
            s1_temp = s1_temp[:-1]
            curr_c -= 1
            curr_r -= 1

        if s1_temp == '' or s2_temp == '':
            # End loop once we run out of letters in either sequence and add the rest of the letters
            s1_align = s1_temp + s1_align
            s2_align = s2_temp + s2_align
            break
    
    # If one of the alignments is longer than the other, gaps should be added
    if len(s2_align) - len(s1_align) != 0:
        # If s1_align is shorter than s2_align, gaps are added at the start of s1
        if len(s2_align) > len(s1_align):
            for i in range(len(s2_align) - len(s1_align)):
                s1_align = '-' + s1_align

        # If s2_align is shorter than s1_align, gaps are added at the start of s2
        else:
            for i in range(len(s1_align) - len(s2_align)):
                s2_align = '-' + s2_align

    #Returns string with both alignments and the alignment score
    return s2_align + " " + s1_align + " " + str(align_score)

def main():
    
    with open('Book1.csv', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            sequences = []
            for el in row:
                sequences.append(el)
            print (NW_align(sequences[0], sequences[1], -2))

    

    

main()
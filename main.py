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
    m = init_matrix(len(s2),len(s1),-2) #2d array
    r = len(s1)                          #rows 
    c = len(s2)                          #columns

    # This loop will complete the Needleman-Wunsch matrix
    for i in range(1,r+1):
        for j in range(1,c+1):
            # Evaluate for up, left, and diagonal and set current cell's value to the maximum 
            # value between the three
            n1 = m[i-1][j-1] + is_match(s1[i-1], s2[j-1])   # Diagonal
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

        diagonal_v = m[curr_r-1][curr_c-1] + is_match(s1_temp[-1],s2_temp[-1])  # Diagonal Value
        up_v =  m[curr_r-1][curr_c] + d                                         # Upper Value
        left_v = m[curr_r][curr_c-1] + d                                        # Left Value
        max_v = max(diagonal_v, up_v, left_v)

        if max_v == left_v:
            s2_align = s2_temp[-1] + s2_align
            s1_align = '-' + s1_align
            s2_temp = s2_temp[:-1]
            curr_c -= 1

        elif max_v == diagonal_v:
            s2_align = s2_temp[-1] + s2_align
            s1_align = s1_temp[-1] + s1_align
            s2_temp = s2_temp[:-1]
            s1_temp = s1_temp[:-1]
            curr_c -= 1
            curr_r -= 1

        else:
            s1_align = s1_temp[-1] + s1_align
            s2_align = '-' + s2_align
            s1_temp = s1_temp[:-1]
            curr_r -= 1

        if s1_temp == '' or s2_temp == '':
            s1_align = s1_temp + s1_align
            s2_align = s2_temp + s2_align
            break

    return s2_align + " " + s1_align + " " + str(align_score)

def test():
    s1 = 'attc'
    s2 = 'agttcg'
    print(NW_align(s1,s2,-2))

def main():
    # TODO Implement csv file data extraction and test in moodle
    return

    
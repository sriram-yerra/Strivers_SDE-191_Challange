def rotateImg(mat): # ---> just transpose
    if not mat:
        return
    
    m = len(mat)
    # n = len(mat[0])

    for i in range(0, m): # -------> revise
        for j in range(i, m): # ---> to skip checking the diagonal elements use "i+1".
            # in the above line, if u use (0, m), it will resettle the matrix as it is.
            mat[i][j], mat[j][i] =  mat[j][i], mat[i][j]
        # mat[i][i], mat[i][i] =  mat[i][i], mat[i][i]
    
    # now reverse the rows
    for i in mat:
        i.reverse()

    return mat

mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
print(rotateImg(mat))
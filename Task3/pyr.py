__author__ = 'user'



def pyr(tr, row=0, col=0, total=0):
    if row == len(tr)-1:
        return total + tr[row][col]
    else:
        return max(pyr(tr, row+1, col, total+tr[row][col]),
                   pyr(tr, row+1, col+1, total+tr[row][col]))

#tr=[[1],[2,1],[1,2,1],[1,2,1,1],[1,2,1,1,1],[1,2,1,1,1,1],[1,2,1,1,1,9,1]]

p=[[1],[1,6],[1,5,8],[2,5,6,1]]
print(pyr(p))

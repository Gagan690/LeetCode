class Solution(object):
    def setZeroes(self, matrix):
        t=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    t.append(i)
                    t.append(j)
        for i in range(0,len(t)-1,2):
            for k in range(len(matrix)):
                matrix[k][t[i+1]]=0
            matrix[t[i]]=[0]*len(matrix[0])
        return matrix

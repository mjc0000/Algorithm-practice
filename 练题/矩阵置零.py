from typing import List




class Solution:
    def setZeroes(self,matrix:List[List[int]]) ->None:
        m =len(matrix)

        if m==0:              return
        n=len(matrix[0])  #一行的个数

        #第一个[]是位于第几行，第二个[]位于该行第几列

        first_row_has_zero=False
        first_col_has_zero=False

        for j in range(n):
            if matrix[0][j]==0:
                first_row_has_zero=True
                break

        for i in range(m):
            if matrix[i][0]==0:
                first_col_has_zero=True
                break

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0


        if first_row_has_zero:
            for i in range(n):
                matrix[0][i]=0

        if first_col_has_zero:
            for i in range(m):
                matrix[i][0]=0



#先判断首行或首列是否要全变0，然后更具首行和首列为索引，把首行首列的0映射到其他整行整列行列

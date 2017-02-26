import numpy as np
import array
A= np.matrix('8.29381 0.995516 -0.560617 ; 0.995516 6.298198 0.595772 ;-0.560617 0.595772 4.997407')
b=np.matrix(' 0.766522 ; 3.844422 ; 3.844422 ')

def norm_inf(mat):
	max=0
	num_rows, num_cols =mat.shape
	i=0
	while(i<num_rows):
		j=0
		sum=np.sum(np.absolute(mat[i]))
		if (max<sum):
			max=sum	
		i=i+1
	return max
eps=0.00001
def solve(mat):
	i=0
	num_rows, num_cols=A.shape
	#strait run
	while(i<num_rows):
		j=i+1
		a_i_i=mat[i,i]
		if (a_i_i<eps):
			print 'warning: div by small number'
		mat[i]=mat[i]/a_i_i
		while(j<num_cols):
			mat[j]=mat[j]-mat[j,i]*mat[i]				
			j=j+1
			
		i=i+1
	#print(mat)
	#reverce run
	i=num_rows-1;
	while(i>=0):
		j=i-1
		while(j>=0):
			mat[j]=mat[j]-mat[i]*mat[j,i]	
			j=j-1
		i=i-1
#	print(mat)
	return mat[:,num_cols]
def find_max(mat,row,col):
	i=row
	c=i
	r=i
	num_rows, num_cols=A.shape
	ret=mat[row,col]
	while(i<num_rows):
		if(ret<mat[i,col]):
			ret=mat[i,col]
			r=i
			c=col	
		i=i+1
	
	j=col
	while(j<num_cols-1):
		if(ret<mat[row,j]):
			ret=mat[row,j]
			c=j
			r=row						
		j=j+1
	return ret,r,c	
def solve_ch(mat):
#	print mat	
	i=0
	num_rows, num_cols=A.shape
	#strait run
	index = array.array('i',(i for i in range(0,num_cols)))
#	print index	
	while(i<num_rows):
	#	print(mat)		
		j=i+1
		a_i_i,max_row,max_col=find_max(mat,i,i)
	#	print max_row,max_col
		index[i],index[max_col]=index[max_col],index[i]
		if(max_row!=i):
			tmp=mat[i].copy()		
			mat[i]=mat[max_row]
			mat[max_row]=tmp	
		if(max_col!=i):	
			tmp=mat[:,i].copy()
			mat[:,i]=mat[:,max_col]
			mat[:,max_col]=tmp
	#	print(mat)
		mat[i]=mat[i]/mat[i,i]
		while(j<num_cols):
			mat[j]=mat[j]-mat[j,i]*mat[i]				
			j=j+1
	#	print(mat)	
		i=i+1
	#print(mat)
	#reverce run
	i=num_rows-1;
	while(i>=0):
		j=i-1
		while(j>=0):
			mat[j]=mat[j]-mat[i]*mat[j,i]	
			j=j-1
		i=i-1
#	print(mat)
	print index[0],index[1],index[2]
	return mat[:,num_cols]
def inv_matrix(A):
	
	num_rows, num_cols=A.shape
	x=np.empty([1,num_rows])
	x[:,0]=1
#	print x
	ret=np.linalg.solve(A,x.T)
	i=1
	while (i<num_cols):
		x=np.empty([1,num_rows])
		x[:,i]=1
		s=np.linalg.solve(A,x.T)
		ret = np.concatenate((ret,s),axis=1)
		i=i+1
		
	return ret
def fun(A,b):
	print("matrix A: ") 
	print(A)
	print("vector b: ")
	print(b)
	print("solve exact: ")
	x_ext=np.linalg.solve(A,b)
	print(x_ext)
	print("solve: ")
	x=solve(np.concatenate((A,b),axis=1))
	print x;
	print("solve advance: ")
	x_ad=solve_ch(np.concatenate((A,b),axis=1))
	print x_ad;	
	print("inv matrix: ") 
	A_inv=inv_matrix(A)
	print A_inv
	#print(A_inv)
	norm = norm_inf(A)
	print('norm: ')	
	print(norm)
	norm_inv = norm_inf(A_inv)
	print('norm inv: ')
	print(norm_inv)
	cond =norm*norm_inv;
	print('cond:');
	print(cond);
	print ('ERROR normal: ')
	print (x_ext-x)	
	print ('ERROR advance: ')
	print (x_ext-x_ad)
print("normal matrix: ")
fun(A,b)
print("extremal  matrix: ")
A[0,0]=eps/10000000;
b=np.matrix(' 0.766522 ; 3.844422 ; 3.844422 ')
fun(A,b)

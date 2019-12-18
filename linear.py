#program using linear algebra commands
import numpy as np
import scipy
from scipy import linalg
a=np.array([[1,2],[3,4]])
print "array1=",a
b=np.array([[5],[6]])
print "array2=",b
#solving linear equations
c=np.linalg.solve(a,b)
print "solved linear equations=",c
#finding eigen values
d=np.linalg.eig(a)
print "eigen values=",d
#finding det
e=np.matrix([[1,2],[3,4]])
print "matrix=",e
f=np.linalg.det(a)
print "det=",f
g=np.linalg.det(e)
print g 
#finding first deravative
h=np.gradient(a)
print "gradient=",h
#dot product of two arrays
i=np.dot(a,b)
print "dot product=",i
#matrix multiplication of two arrays
j=np.matmul(a,b)
print "matrix multiplication=",j
#raise a matrix to power n
k=np.linalg.matrix_power(a,2)
print "power raised matrix=",k
#finding inverse
l=np.linalg.inv(a)
print "inverse=",l
#finding norm
m=np.linalg.norm(a)
print "norm=",m
#finding rank of a matrix
n=np.linalg.matrix_rank(e)
print "rank=",n
#trace
o=np.trace(a)
print "trace=",o
#square root
p=scipy.linalg.sqrtm(a)
print "square root=",p
q=scipy.linalg.tri(2,4,3,dtype=int)
print "special matrix=",q
#matrix logarithm
r=scipy.linalg.logm(e)
print "matrix logarithm=",r
#matrix exponential
s=scipy.linalg.expm(e)
print "matrix exponential=",s




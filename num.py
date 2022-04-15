# # NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. 
import numpy as np
d=np.array([1,2,3])
print(d)
# print(type(d))#ndarray:- Number direction
# print(d.shape)

# mat=np.array([[1,2],[3,4]])
# print(mat)
# print(type(mat))
# print(mat.shape)
# print(mat[0,0])
# print(mat[0,1])
# print(mat[1,0])
# print(mat[1,1])
# mat[0,0]=5
# print(mat)
# mat[0,0]=5
# print(mat)

# sl=np.arange(0,10,1)
# print(sl)
# sl1=np.random.rand(5,5)
# print(sl1)
# arr=[2,3,4,5]
# sl3=np.random.choice(arr)
# print(sl3)
# sl2=np.linspace(0,10,20)
# print(sl2)
# print(sl2.shape)

# m1=np.array([0,3,4,2])
# print(m1.dtype)#64-bit integer value, 64-bit float value, 6-bit caharacter unicode string.
# m=np.array(["kite","more"])
# m[1]="pop"#this is for updating only not for inserting the elements.
# print(m)
# print(m.dtype)
# m2=np.array([0.3,9.4])
# print(m2.dtype)

# a = np.matrix([[1, 21, 30],
#                  [63 ,434, 3],
#                  [54, 54, 56]])
 
# print("Main Diagonal elements :", a.diag(a))
 
# print("Diagonal above main diagonal :", a.diag(a, 1))
 
# print("Diagonal below main diagonal :", a.diag(a, -1))

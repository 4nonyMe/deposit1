# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 19:01:39 2023

@author: Augustin
"""

#Write a NumPy program to create a vector with values from 0 to 20 
#and change the sign of the numbers in the range from 9 to 15.

import numpy as np
n=int(input("enter the number of values in the vector: "))
a=np.linspace(0,20,n)
for i in range(0,n):
    if a[i]>=9 and a[i]<=15:
        a[i]*=(-1)
print(a)


#Write a NumPy program to create a vector with values ranging from 15 to 55 
#and print all values except the first and last.

n=int(input("enter the number of values in the vector: "))
b=np.linspace(15,55,n)
print(b)
print(b[1:n-1])

#Write a NumPy program to create a 3X4 array and iterate over it.

array=np.zeros((3,4))
for i in range(0,3):
    for j in range(0,4):
        array[i,j]=int(input("enter the value at coordinates [{},{}]: ".format(i+1,j+1)))
print(array)

#Write a NumPy program to create a vector of length 10 
#with values evenly distributed between 5 and 50.

c=np.linspace(5, 50,10)
print(c)

#Write a NumPy program to create a vector of length 5 
#filled with arbitrary integers from 0 to 10.
d=np.zeros(5)
for i in range(0,5):
    test=False
    while test==False:
        try:
            d[i]=int(input("enter the interger at index {}, must be between 0 and 10: ".format(i)))
            if d[i]>=0 and d[i]<=10:
                test=True
        except ValueError as e:
            print(e)
print(d)

#Write a NumPy program to multiply the values of two given vectors.
e=np.linspace(2,10,5)
f=np.linspace(11,20,5)
g=e*f
print(e,f,g)

#Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.
h=np.linspace(10,22,12).reshape(3, 4)
print(h)

#Write a NumPy program to find the number of rows and columns in a given matrix.
import random as rd
max_width=int(input("enter the maximum matrix widht: "))
max_height=int(input("enter the maximum matrix height: "))
width=rd.randint(1,max_width)
height=rd.randint(1, max_height)
matrix=np.zeros((width, height))
print(matrix)
print(matrix.shape)

#Write a NumPy program to create a 4x4 matrix in which 
#0 and 1 are staggered, with zeros on the main diagonal.

matrix=np.zeros((4,4))
for i in range(0,4):
    for j in range(0,4):
        if (i+j)%2==1:
            matrix[i,j]=1
print(matrix)

#Write a NumPy program to find common values between two arrays.
array1=[0,10,20,40,50]
array2=[10,30,40]
common_val=[]
for i in range(0,len(array1)):
    for j in range(0,len(array2)):
        if array1[i]==array2[j]:
            common_val.append(array1[i])
print(common_val)

#Write a NumPy program to get the unique elements of an array.
array1=[10,10,20,20,30,30]
array2=[[1,1],[2,3]]
unique_elements = np.unique(array1)
print(unique_elements)
unique_elements = np.unique(array2)
print(unique_elements)


#Write a NumPy program to compute the cross product of two given vectors
vect1=[1,3,5]
vect2=[2,4,6]
cross_product = np.cross(vect1, vect2)
print(cross_product)

#Write a NumPy program to convert cartesian coordinates to polar coordinates 
#of a random 10x2 matrix representing cartesian coordinates.

cart_coord=np.random.rand(10,2)
xs=cart_coord[:,0]
ys=cart_coord[:,1]
rs=np.sqrt(xs**2+ys**2)
thetas=np.degrees(np.arctan2(ys,xs))
pol_coord=np.column_stack((rs,thetas))
print(pol_coord)


#Write a NumPy program to find the closest value (to a given scalar) in an array.
array=np.linspace(0,99,100)
x=float(input("enter the scalar to approximate: "))
array2=np.abs(array-x)
y=array[np.argmin(array2)]
print(y)




























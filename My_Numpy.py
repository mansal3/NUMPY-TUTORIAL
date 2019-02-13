import numpy as np

#array
arr = np.array([1, 2, 3])
print(arr)

#size(no of elements in array
print(arr.size)

#ndim(no of rows)
print(arr.ndim)

#dtype(data type of each element in array)
print(arr.dtype)

#shape(return the shape of array)
print(arr.shape)

#type(array)
print(type(arr))

#if you want to create array of particular data type
arr1=np.array([[1,2,3,4],[5,6,7,8]],dtype=float)
print(arr1)

#creating array using tuple
arr2=np.array((1,2,3))
print(arr2)

#creating array with all zeros
arr3=np.zeros((3,4))
print(arr3)

# array with complex values
arr4=np.full((3,3),4,dtype="complex")
print(arr4)

#array wth random values
arr5=np.random.random((2,3))
print(arr5)

# Create a sequence of integers
# from 0 to 30 with steps of 5
f = np.arange(0, 30, 5)
print(f)

# Create a sequence of 10 values in range 0 to 5
g = np.linspace(0, 5, 10)
print(g)

#reshape the rows and columns of the array
arrayreshape=np.array([[1,2,3],[2,3,4]])
print(arrayreshape)
print(arrayreshape.reshape(3,2))

#flatten array
print(arrayreshape.flatten())

#slicing
s=slice(1)
print(arrayreshape[s])
print(arrayreshape[1:3])
print(arrayreshape[1:])

a = np.array ( [ 1 , 2 , 5 , 3 ] )

# add 1 to every element
print ( "Adding 1 to every element:" , a + 1 )

# subtract 3 from each element
print ( "Subtracting 3 from each element:" , a - 3 )

# multiply each element by 10
print ( "Multiplying each element by 10:" , a * 10 )

# square each element
print ( "Squaring each element:" , a ** 2 )

# modify existing array
a *= 2
print ( "Doubled each element of original array:" , a )

# transpose of array
a = np.array ( [ [ 1 , 2 , 3 ] , [ 3 , 4 , 5 ] , [ 9 , 6 , 0 ] ] )

print ( "\nOriginal array:\n" , a )
print ( "Transpose of array:\n" , a.T )

arr = np.array ( [ [ 1 , 5 , 6 ] ,
                   [ 4 , 7 , 2 ] ,
                   [ 3 , 1 , 9 ] ] )

# maximum element of array
print ( "Largest element is:" , arr.max () )
print ( "Row-wise maximum elements:" ,
        arr.max ( axis=1 ) )

# minimum element of array
print ( "Column-wise minimum elements:" ,
        arr.min ( axis=0 ) )

# sum of array elements
print ( "Sum of all array elements:" ,
        arr.sum () )

# cumulative sum along each row
print ( "Cumulative sum along each row:\n" ,
        arr.cumsum ( axis=1 ) )

a = np.array ( [ [ 1 , 2 ] ,
                 [ 3 , 4 ] ] )
b = np.array ( [ [ 4 , 3 ] ,
                 [ 2 , 1 ] ] )

# add arrays
print ( "Array sum:\n" , a + b )

# multiply arrays (elementwise multiplication)
print ( "Array multiplication:\n" , a * b )

# matrix multiplication
print ( "Matrix multiplication:\n" , a.dot ( b ) )
a = np.array ( [ [ 1 , 4 , 2 ] ,
                 [ 3 , 4 , 6 ] ,
                 [ 0 , -1 , 5 ] ] )

# sorted array
print ( "Array elements in sorted order:\n" ,
        np.sort ( a , axis=None ) )

# sort array row-wise
print ( "Row-wise sorted array:\n" ,
        np.sort ( a , axis=1 ) )

# specify sort algorithm
print ( "Column wise sort by applying merge-sort:\n" ,
        np.sort ( a , axis=0 , kind='mergesort' ) )

# Example to show sorting of structured array
# set alias names for dtypes
dtypes = [ ('name' , 'S10') , ('grad_year' , int) , ('cgpa' , float) ]

# Values to be put in array
values = [ ('Hrithik' , 2009 , 8.5) , ('Ajay' , 2008 , 8.7) ,
           ('Pankaj' , 2008 , 7.9) , ('Aakash' , 2009 , 9.0) ]

# Creating array
arr = np.array ( values , dtype=dtypes )
print ( "\nArray sorted by names:\n" ,
        np.sort ( arr , order='name' ) )

print ( "Array sorted by grauation year and then cgpa:\n" ,
        np.sort ( arr , order=[ 'grad_year' , 'cgpa' ] ) )

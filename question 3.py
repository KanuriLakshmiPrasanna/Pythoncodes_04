'''Write a program  where we take 
where each element is the square of the index of the element in the list.'''
numbers=map(int,input().split())
tuple_numbers=tuple(numbers)
square_numbers=[]
for i in tuple_numbers:
    square_numbers.append(i**2)
tuple_square_numbers=tuple(square_numbers)
print(tuple_square_numbers)


'''Write a program to remove the even number from a list'''
nums=tuple(map(int,input().split()))
nums_list=list(nums)
for i in nums:
    if i%2==0:
        nums_list.remove(i)
print(tuple(nums_list))


'''You are given 2 tuples of equal length add the corresponding elements of both tuples and print the resulting tuple.
input format: two lines containing space separated integers representing the two tuples.
output format: a tuple of element wise sums.'''
tup1=tuple(map(int,input().split()))
tup2=tuple(map(int,input().split()))
result=zip(tup1,tup2)
lst=[]
for a,b in result:
    lst.append(a+b)
print(tuple(lst))


'''Given a tuple of integers second largest element 
input: Sapce separated integers
output: second largest element'''


'''Given list of integersm filterout the elements containing only positive integers'''


'''Given a number n,create a tuple that contain first n natural numbers'''

'''given a tuple find how many even and odd numbers are there'''



    
from functools import reduce
# Exercise 1
'''
6
15
33

'''

# Exercise 2
list_1=[1 , 2 , 3 , 4] 

def mul(*num):
     s = 1 
     for n in num:   
         s = s * n
     return s
 
print(mul(*list_1))


# Exercise 3
mul_2 = lambda b , *y:b * y

print(mul_2(3 , 2 , 5 ))


# Exercise 4

_list = range(-5, 5)
print("xxXXXXx",list(filter(lambda x: x<0, _list)))

# Exercise 5
'''
13
'''

# Exercise 6
'''
(("joey" , "chandler" , "David") , ("Monica","Pheobe","Rachel"))
'''

# Exercise 7
coin = ('Bitcoin' , 'Ether' , 'Ripple' , 'Litecoin')
code = ('BTC' , "ETH" ,'XRP','LTC')

d = dict(zip(coin , code))
print(d)

'''
{'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'Litecoin': 'LTC'
'''

# EXercise 8
'''
['e' , 'o']
'''

# Exercise 9
k = list(map(int,input("Enter a multiple value: ").split()))
print("List of student:" , k)
'''
List of student: [20]
'''

# Exercise 10
'''
Error in the parametr
'''

# Exercise 11
def func(a,b):
    return a+b
a=list(map(func,[2,4,5],[1,2,3,4]))
print(a)
'''
[3, 6, 8]
'''
# Exercise 12
c = map(lambda x:x+x,filter(lambda x:(x>=3),(1,2,3,4)))
print(list(c))
'''
[6, 8]
'''

# Exercise 13
'''
[4 , 6 , 8]
'''

# Exercise 14

list1 = [ 10, 3, 5, 6, 2] 

print (reduce(lambda a,b : a if a < b else b,list1)) 

# Exercise 15
numbers = [1 , 2 , 3]
letters = ['a' , 'b' , 'c']

e =list(zip(numbers , letters))
print(e)






































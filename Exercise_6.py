# exercise 1
import numpy as np
e11=np.array([0,0,0,0,0,0,0,0,0,0])
e12=np.array([1,1,1,1,1,1,1,1,1,1])
e13=np.array([5,5,5,5,5,5,5,5,5,5])
                       
print(e11)
print(e12)
print(e13)

print('-----------------------------------')

# exercise 2
e2=np.arange(30,70)
print(e2)

print('-----------------------------------')

# exercise 3
e3=np.arange(30,70,2)
print(e3)

print('-----------------------------------')

# exercise 4
ex4=np.identity(3)
print(ex4)

print('-----------------------------------')

# exercise 5
ex5=np.random.normal(0,1,1)
print(ex5)

print('-----------------------------------')

# exercise 6

e6=np.arange(10,22).reshape((3,4))
print (e6)
for x in np.nditer(e6):
  print(x)
  
print('-----------------------------------')

# exercise 7
e7= np.arange(0,20)
e7[(e7>=9)&(e7<=15)]*=-1
print(e7)

print('-----------------------------------')

# exercise 8
x = np.array([1, 8, 3, 5])
y= np.random.randint(0, 11, 4)
result = x * y
print(result)

print('-----------------------------------')

# exercise 9
ex9=np.arange(1,10).reshape((3, 3))
print(ex9)


print('-----------------------------------')

# exercise 10
e10=np.arange(1,17).reshape((4, 4))
print(e10)

print('-----------------------------------')

# exercise 11
a = np.array([9,-1,2,5])
b = np.array([1,-6,0,10])
c = np.array([[1,8,2,5],[3,1,7,9]])

print("a-b: ",a-b)
print("a*b: ",a*b)
print("a.dot(b): ",a.dot(b))
print("a*2: ",a*2)
print("np.sin(a): ",np.sin(a))
print("a<3: ",a<3)
print("a.sum(): ",a.sum())
print("a.sum(axis=0): ",a.sum(axis=0))
print("c.sum(): ",c.sum())
print("c.sum(axis=0): ",c.sum(axis=0))
print("a.min(): ",a.min())
print("a.max(): ",a.max())
print("a.mean(): ",a.mean())
print("a average(): ",np.average(a))
print("a median(): ",np.median(a))
print("a std(): ",np.std(a))
print("a var(): ",np.var(a))
print("c.cumsum(): ",c.cumsum())
print("a[1:2] : ",a[1:2])
print("a[2:] : ",a[2:])
print("c[-1] : ",c[-1])

print('-----------------------------------')

# exercise 12
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(1,50)
y =[value*3 for value in x]
plt.plot(x, y)
plt.title('Drawe a line .')
plt.ylabel('Y-axis')
plt.xlabel('X-axi')
plt.show()


print('-----------------------------------')

# exercise 13
x1=[10,20,30]
x2=[10,20,30]
plt.figure()
plt.plot(x1, [20,40,10], label = "line1")
plt.plot(x2, [40,10,30], label = "line2")
plt.title("Tow or more lines on same plot with suitable legends")
plt.legend(loc='upper right')
plt.show


print('-----------------------------------')

# exercise 14
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'b--', t, t**2, 'ys', t, t**3,'g^')
plt.show()

print('-----------------------------------')

# exercise 15

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

objects = ('Python', 'Java', 'PHP', 'JavaScript', 'C#','C++')
y_pos = np.arange(len(objects))
popularity = [22.2,17.6,8.8,8,7.7,6.7]

plt.bar(y_pos, popularity, align='center', color=['green','yellow','red','pink','black','gray'])

plt.xticks(y_pos, objects)
plt.ylabel('PopulartiY')
plt.title('PopulartiY of Programming Language')

plt.show()
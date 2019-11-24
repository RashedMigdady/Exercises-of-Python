#  Function in python 

def fun_1():                # Normal function
    print("this is first function$ ")
     
fun_1()


def fun_2(name):            # Function with parametr
    print("My name is : " ,name )
    
fun_2("Rashed")
fun_2("Migdady")

def fun_3(age = 0):        # Function with Default value
    print("My age is : ",age)
    
fun_3()
fun_3(24)

def fun_4(x=2):           # function with "return"
    return 10 * x

print(fun_4(3))


def fun_5_adder(*number):
    s = 0
    for n in number:
        s = s + n
    print("The sum of values is : ", end=" ")
    return s

print(fun_5_adder(2 , 10 , 20 , 10))

array = [1 , 2 , 3 , 4 , 5]

print(fun_5_adder(1 , 2 , 2 , *array)) 


def fun_6(**KeyValue):
    for k,v in KeyValue.items():
        print("%s == %s" %(k , v) , end="   ")
        
fun_6(theName="Rashed" , age="20" , theMajor="CS")

var = "Irbid"

def fun_7():
    var = "AMMAN"
    print(var)
    
fun_6()




def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)
    
print("The answar is : ",factorial(4))



###############
summ =lambda x, y , z=3 : x+y+z

print("sum = " , summ(10, 7))
print("sum = " , summ(10, 7 , 19))


li = [5 , 7 , 2 , 9 , 5 , 4 , 6]

f_list = list(map(lambda x: x*2 ,li)) # Map

print(f_list)


l1 = [1 , 2 , 3]
l2 = ["a" , "b" , "c"]
l3 = ["X" , "Y" , "Z"]

results = list(zip(l1 , l2 , l3)) # Zipping 

print(results)

































































    
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 09:30:37 2023

@author: Augustin
"""



print("hello world")
name='Augustin Vanlerberghe'
print(type(name))
print(name)
num1=321
num2=123
add=num1+num2
print(add)
print("""Hello python's,
how are you doing ?""")
x=6
y=9
print(x,y)
print(x+y)
print(x-y)
print(x*y) 
print(x**y)
print(y**(1/2))
xSTR=str(x)
print(type(xSTR))

#Exercice 2

print("caffè\ncafé\ncoffee")
print("""café
caffè
coffee""")

#Exercice 3

x=input("How much? ")
y=float(x)
print(2.5+y)

#Exercice 4

print(223/71)
print((1+1/10)**10)
print((1+1/100)**100)
print((1+1/1000)**1000)

#Exercice 5

print('sparrow'>'eagle')
print('dog'>'cat' or 45%3==0)
print(60-45/5+10==1)

#SECOND LESSON

import math as m
import sys
import pandas
import random
import numpy as np

def V(r,h):
    return float((1/3)*m.pi*(r**2)*h)

print(V(float(input("enter r")),float(input("enter h"))))



a=float(input("enter a"))
b=float(input("enter b"))
print("product of {} and {} is {}".format(a,b,a*b))

print("{} °C = {} K".format(c:=float(input("Enter temperature in celsius : ")), c + 273.15))

def wallet():
    tens=int(input("enter number of 10 euros banknotes"))
    twenties=int(input("enter number of 20 euros banknotes"))
    fifties=int(input("enter number of 50 euros banknotes"))
    return tens*10+twenties*20+fifties*50

print(wallet())

print ("total value of wallet is {}".format(total:=10*(int(input("enter number of 10 euros banknotes")))+20*int(input("enter number of 20 euros banknotes"))+50*int(input("enter number of 50 euros banknotes"))))


print("length search is {}".format(c:=m.sqrt( (a:=float(input("enter length a")))**2 + (b:=float(input("enter b length")))**2 -2*a*b*m.cos(m.radians(float(input("enter angle in degrees")))))))

message="good morning"
print("{} - {} - {} - {}".format(message, len(message), message[8:11],message[:-1]))


print(message.count('o'))
print(message.upper())
print(message.replace("good","bad"))


marks=float(input("enter your marks : "))
if marks<40:
    print("student has failed the test and got an F grade")
elif marks>=40 and marks<50:
    print("student has passed marginaly and got an E grade")
elif marks>50 and marks<5:
    print("student has passed with c grade")
elif marks>=75 and marks<90:
    print("The student has done well and has scored B grade")
else:
    print("the student has done excellent and passed with distinct")
    
#Exo IMC

weight=float(input('Enter your weight:'))
height=float(input('Enter your height'))   
BMI=weight/(height**2)
if BMI<18.5:
    print("Your BMI is {} and you are in underweight".format(BMI))
elif BMI>=18.5 and BMI<25:
    print("Your BMI is {} and you are in normal weigth".format(BMI))
elif BMI>=25 and BMI<30:
    print("Your BMI is {} and you are in overweight".format(BMI))
else:
    print("Your BMI is {} and you are in obesity".format(BMI))


#Divisible natural number

a=int(input("enter a value"))
b=int(input("enter b value"))
maxi=max(a,b)
mini=min(a,b)
if maxi%mini==0:
    print("it is divisible and the quotient is {}".format(maxi//mini))
else:
    print("it is not divisible and {} = {} * {} + {}".format(maxi,mini,maxi//mini,maxi%mini))


def price_energy(energy):
    price=int(0)
    if energy<=100:
        price=0
    elif energy>100 and energy<=200:
        price=(energy-100)*5
    elif energy>200:
        price=500+(energy-200)*10
    return price

print(price_energy(float(input("enter units of energy"))))

num=int(input("enter an integer value "))
ndiv=1
while(ndiv<num):
    print("The integer division of {} by {} gives {}".format(num,ndiv,res:=num//ndiv))
    ndiv+=1


num=1
ndiv=0
while num>0 and num<211:
    if num%3==0:
        print(f"the number is {num}")
        ndiv+=1
    num+=1
    
print("total number of iterations: {}".format(ndiv))

somme=0
i=1
while i<=10:
    somme+=i
    i+=1
print(somme)


i=1
somme=0
while i<=10:
    value=int(input("enter int value: "))
    somme+=value
    i+=1
print(somme/10.0)

i=0
sum=0
while i<10:
    num=int(input("Enter an integer value:"))
    sum=sum+num
    i=i+1
average=sum//10
print(average)


#pyramide
i=1
while i<=4:
    print("*"*i)
    i=i+1
    
# avec boucle for     

x=int(input("nb of line: "))
nb=0
for i in range (x):
    nb+=1
    print(nb*"*")




#factoriel

value=int(input("enter a value to find the factorial of: "))
result=1
while value>0:
    result*=value
    value-=1
print(result)

name="jesaa29Roy"
size=len(name)
i=0
while i < size:
    if name[i].isdecimal():
        break;
    print(name[i], end=' ')
    i+=1
   
    

   
name="jesaa29Roy"
size=len(name)
i=-1
while i+1 < size:
    i+=1
    if not name[i].isalpha(): 
        continue
    print(name[i], end=' ')







# for i in range(nb_initial, nb_final, pas)

n=int(input("enter the integer to do the sum of "))
sigma=0
for i in range(1,n+1,1):
    sigma+=i
print(sigma)


for i in range(1,10):
    for j in range(1,10):
        if i!=j:print(10*i+j)
 
for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            print((100*i)+(10*j)+k)    
            
for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            if(i+j+k==22):print((100*i)+(10*j)+k)        
    
    
n=int(input("enter an integer: "))   
for i in range(1,n+1):
    if(n%i==0): print(i)

#premier number
n=int(input("enter an integer: "))
premier=True
for i in range(2,n)   :
    if n%i==0:premier=False
print(premier)


n=int(input("Enter an integer value: "))
u0=0
u1=1
u2=0
for i in range(2,n):
    u2=u0+u1
    u0=u1
    u1=u2
print (u2)
    
    
Integers = [1,2,3,4]
print(Integers)
smooth=[3.14, 7, -2+3j, 'water', False, [1,2]]
long_smooth=len(smooth)
print(smooth)
print(long_smooth)
print(smooth[3][4])
print(smooth[4:], smooth[:2])

bg=[3.14,7,-2+3j,'water',False,[1,2],5,"Hello","Hi","1","e"]
bg[::2]#ca fait un pas de 2 en 2 , on ^rend que les éléments 1 sur 2
print(bg[-1])
print(bg[-2])
bg.pop(2)#retire l'élément à l'index 2
print(bg)

names=[]
grades=[]
name=input("enter name: ")
while name!='':
    names.append(name)
    grade=int(input("enter grade: "))
    grades.append(grade)
    name=input("enter name: ")
fin=len(names)
for i in range (0,fin):
    print(names[i], grades[i])
print("mean: {}".format(sum(grades)/fin))


num=int(input("enter an int: "))
nums=[]
while num!='':
    nums.append(int(num))
    num=input("enter the next integer or just press enter to stop: ")
for i in range (0,len(nums)):
    print(nums[i])
print("mean: {}".format(sum(nums)/len(nums)))

noms_str=input("enter a list of names separated by spaces: ")
noms=noms_str.split(" ")
for i in range(0, len(noms)):
    print("Hi {}".format(noms[i]))


max_deg=int(input("enter the max degre of the polynomial"))
degs=[]
for i in range (0, max_deg):
    deg_i=int(input("enter the coefficient of X^{}".format(i)))
    degs.append(deg_i)
for i in range(0,max_deg):
    print


#Dictionnaries
country_capitals = {"United States": "Washington D.C.", "Italy": "Rome", "England": "London"}
print (country_capitals)

#empty dictionnary : 
dict={}

#creating dictionnary with dict() method
d = dict(k1=1, k2=2, k3=3)

#creating a nested dictionnary
Dict={1: 'Geeks', 2: 'For', 3:{'A':'Welcome','B':'To', 'C':'Geeks'}}

print(Dict)
print(Dict[3]['A'])

country_capitals = {"United States": "Washington D.C.", "Italy": "Naples"}
country_capitals["Italy"]="Rome"
country_capitals["Germany"]="Berlin"

keys=['Ten','Twenty', 'Thirty']
values=[10,20,30]
borne=len(keys)
dict={}
for i in range(borne):
    dict[keys[i]]=values[i]
print(dict)


elements={'H':{'element':'hydrogen', 'atomic number': 1, 'melting point':14,'boiling point':20},
          'He':{'element':'helium', 'atomic number': 2, 'melting point':1,'boiling point':4},
          'Li':{'element':'lithium', 'atomic number': 3, 'melting point':453,'boiling point':1603},
          'Be':{'element':'beryllium', 'atomic number': 4, 'melting point':1560,'boiling point':2742},
          'B':{'element':'boron', 'atomic number': 5, 'melting point':2349,'boiling point':4200},
          'C':{'element':'carbon', 'atomic number': 6, 'melting point':3915,'boiling point':3915},
          'N':{'element':'nitrogen', 'atomic number': 7, 'melting point':63,'boiling point':77},
          'O':{'element':'oxygen', 'atomic number': 8, 'melting point':54,'boiling point':90},
          'F':{'element':'fluorine', 'atomic number': 9, 'melting point':53,'boiling point':85},
          'Ne':{'element':'neon', 'atomic number': 10, 'melting point':25,'boiling point':27}}

choice=input('enter an element symbol: ')
while (choice!='H'and choice!='He'and choice!='Li'
        and choice!='Be'and choice!='B'and choice!='C'and choice!='N'
        and choice!='O'and choice!='F'and choice!='Ne'):
    choice=input('enter an element symbol: ')
temp=int(input('enter a temperature in kelvin: '))
temp_mel=elements[choice]['melting point']
temp_boil=elements[choice]['boiling point']
state='solid'
if (temp>temp_boil):
    state='gaz'
elif (temp>temp_mel):
    state='liquid'
print(state)



nombres=list()
for i in range (5):
    nombres.append(int(input("enter the {}th value of the list: ".format(i+1))))

print(nombres)
mini=nombres[0]
maxi=nombres[0]
for i in range(4):
    if nombres[i]>maxi:
        maxi=nombres[i]
    elif nombres[i]<mini:
        mini=nombres[i]

print("The biggest number of the list is {} and the smallest number of the list is {}".format(maxi,mini))



number=int(input("enter an int number: "))
even=True
if number%2!=0:
    even=False
print("even: {}".format(even))


while True:
    try:
        num=int(input("enter a number: "))
        if (num%2)==0:
            print("{} is even".format(num))
        else:
            print("{} is odd".format(num))
        break
    except ValueError as e:
        print(e)

import matplotlib.pyplot as plt

y=np.linspace(10, 30, 21)
y[4]=1
print (y)

x=np.linspace(-2,2,101)
y=x**2
print(x)
plt.plot(x,y)

x=np.linspace(0,3*np.pi,500)
plt.plot(x, np.sin(x**2))
plt.title('A simple chirp')
plt.show()

n=int(input('Enter the number of points to draw: '))
x=np.linspace(-1,1,n)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title=("Body function (2πx)")
y=np.cos(2*np.pi*x)
plt.plot(x,y)
plt.savefig("cos2pix.png")
plt.show

a=int(input("Enter the number of points to draw: "))
x=np.linspace(-1,1,a)
y1=np.sin(2*np.pi*x)
plt.plot(x,y1,"sin(2pix)")
y2=np.cos(2*np.pi*x)
plt.plot(x,y2,"cos(2pix)")
plt.xlim(-1,1)
plt.legend()
plt.savefig("trigonometric.png")
plt.show()

n=int(input('Enter the number of points to draw: '))
x=np.linspace(-1,1,n)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title=("Body function sin(πx)sin(20πx)e^(-x) ")
y=np.sin(20*np.pi*x)*np.sin(np.pi*x)*np.exp(-x)
plt.plot(x,y)
plt.savefig("sin(pix)sin(20pix)emoinsx.png")
plt.show
































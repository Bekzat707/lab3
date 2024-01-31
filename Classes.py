class String:

    def getString(self, strings):
        print(strings)
    def printString(self, strings):
        strings = strings.upper()
        print(strings)

string = String()

string.getString("Hello Bekzat")
string.printString("kbtu")

import math
class Shape:
    def __init__(self):
        pass
        
    def area(self):
        return 0
    
    def rectangle(self):
        return self.length * self.width

class Square(Shape):
    def __init__(self, length, width):
        self.width = width
        self.length = length

    def area(self):
        return self.length * self.length

square = Square(5, 7)

print(square.area())

print(square.rectangle())


class cord():
    def unit(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def show (x1,y1,x2,y2):
        print( x1,y1,x2,y2)
    
    def move(x1,y1,x2,y2):
        points=[]
        x1 = int(input("x1: "))
        y1 = int(input("y1: "))
        x2 = int(input("x2: "))
        y2 = int(input("y2: "))
        points.append(x1)
        points.append(y1)
        points.append(x2)
        points.append(y2)
        
        print(points)

    def dict(x1,y1,x2,y2):
        print( math.sqrt(((x1-x2)**2)+(y1-y2)**2))
    
cord.dict(2,3,5,6)

cord.move(2,3,4,5)


class Bank():
    def __init__(self,account,money):
        self.account=account
        self.money=money

    def owner(self):
        return self.account
    
    def deposit(self,money):
        self.money+=money
         
        return f"You are deposit {money} money"
    
    def balance(self):
        return self.money
    
    def withdraw(self,money):
        if self.money-money <0:
            return "not enough"
        else:
            self.money-=money

            return "the money was returned"
        

bank = Bank ( "Bekzat" ,1000)

print(bank.balance())

print(bank.owner())

print(bank.deposit(1000))

print(bank.withdraw(3000))

print(bank.withdraw(3))

print(bank.balance())



n=int(input())                   #we provide the length of the array

numbers=[]   
for i in range(n):               #______________________________________
    num=int(input())             # we enter the array elements ourselves   
    numbers.append(num)          #______________________________________

print(numbers)                   #show array

class Prime():
    def __init__(self,list):
        self.list=list

    def filter_prime_numbers(self):
        prime_num=[]
        s=0
        for i in self.list:
            if i<=3:
                prime_num.append(i)
            for j in range(2,i):
                if i<=3:
                    break
                elif i%j!=0:
                    s+=1

            if (s==(i-2) and s>2):
                 prime_num.append(i)
                 s=0
            s=0  
        print(prime_num)

                
prime=Prime(numbers)

prime.filter_prime_numbers()
       

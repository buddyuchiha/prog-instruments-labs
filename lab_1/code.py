import math

class MathOperations:
    def Add(x,y):
      return x+y
    def subtract(a, b):return a-b

    def MULTIPLY(v1,v2):
        return v1*v2
    def divide(num1,num2):
      if num2!=0:
       return num1/num2
      else:return "Undefined"

class Geometry:
      def __init__(self,radius,height):
            self.radius= radius
            self.height= height
      def areaCircle(self):
            return math.pi*self.radius*self.radius
      def volumeCylinder(self):
         return math.pi*self.radius*self.radius*self.height

def Factorial(number): 
    if number == 0: return 1
    else: return number * Factorial(number - 1)
    
def Power(base, exp):
        result=1
        for i in range(1,exp+1):
                result =result*base
        return result

def fibonacci(n):
 if n<=0:return "Invalid Input"
 elif n==1: return 0
 elif n==2: return 1
 else: return fibonacci(n-1)+fibonacci(n-2)

def isPrime(num):
      if num<=1:
            return False
      for i in range(2, int(num/2)+1):
            if num % i == 0:
                  return False
      return True

class MatrixOperations:
 def addMatrices(m1,m2):
    result=[[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]
    return result

 def multiplyMatrices(m1,m2):
    result=[[sum(a*b for a,b in zip(m1_row,m2_col)) for m2_col in zip(*m2)] for m1_row in m1]
    return result

def sort_list(lst):
 for i in range(len(lst)-1):
    for j in range(i+1, len(lst)):
        if lst[i]>lst[j]:
            lst[i], lst[j] = lst[j],lst[i]
 return lst

def binary_search(arr, low, high, x):
 if high>=low:
  mid=(high+low)//2
  if arr[mid] == x: return mid
  elif arr[mid]>x: return binary_search(arr, low, mid-1, x)
  else: return binary_search(arr, mid+1, high, x)
 else:return -1

class SimpleStatistics:
      def Mean(data):return sum(data) / len(data)
      def Median(data):
           s_data=sorted(data)
           n=len(s_data)
           if n%2==0:
               return (s_data[n//2-1]+s_data[n//2])/2
           else: return s_data[n//2]

def Mode(data):
 frequency={}
 for value in data:frequency[value]=frequency.get(value,0)+1
 mode=[key for key, value in frequency.items() if value==max(frequency.values())]
 return mode

def gcd(a,b):
 while b!=0: a,b=b,a%b
 return a

def lcm(a,b):
 return abs(a*b)//gcd(a,b)

def Pascal_triangle(n):
 for i in range(n):
  print(' '*(n-i), end=' ')
  number=1
  for j in range(1,i+2):
    print(number, end=' ')
    number=number*(i-j+1)//j
  print()

def checkPalindrome(s):
 s=s.lower()
 return s==s[::-1]

def UniqueElements(lst):
 unique_lst=[]
 for element in lst:
     if element not in unique_lst:
        unique_lst.append(element)
 return unique_lst

def is_anagram(str1,str2):
 return sorted(str1)==sorted(str2)

class Calculator:
      def __init__(self,a,b):
            self.a=a
            self.b=b

      def add(self):return self.a+self.b
      def subtract(self):return self.a-self.b
      def multiply(self):return self.a*self.b
      def divide(self): 
          if self.b!=0: return self.a/self.b
          else:return "Cannot divide by zero"

def countdown(n):
 while n>0:print(n);n-=1

def is_even(n): return n%2==0

def fibonacci_iterative(n):
 f1, f2=0,1
 if n==1: return f1
 elif n==2: return f2
 else:
     for i in range(2,n):
         f3=f1+f2
         f1=f2
         f2=f3
 return f2

class Person:
      def __init__(self, name, age):self.name=name; self.age=age
      def greet(self):print("Hello, my name is",self.name)

class StringOps:
      def ReverseString(s):return s[::-1]
      def ToUpperCase(s):return s.upper()

def main():
 calculator = Calculator(10,5)
 print("Add:", calculator.add())
 print("Subtract:", calculator.subtract())
 print("Multiply:", calculator.multiply())
 print("Divide:", calculator.divide())
 print("Factorial of 5:", Factorial(5))
 print("Power of 2^3:", Power(2,3))
 print("Fibonacci(10):", fibonacci(10))
 print("Is 7 prime?", isPrime(7))
 matrix1=[[1,2],[3,4]]
 matrix2=[[5,6],[7,8]]
 print("Matrix Addition:", MatrixOperations.addMatrices(matrix1, matrix2))
 print("Matrix Multiplication:", MatrixOperations.multiplyMatrices(matrix1, matrix2))
 data=[2,3,5,7,3,5,3]
 print("Mean:", SimpleStatistics.Mean(data))
 print("Median:", SimpleStatistics.Median(data))
 print("Mode:", Mode(data))
 print("GCD of 8 and 12:", gcd(8,12))
 print("LCM of 8 and 12:", lcm(8,12))
 Pascal_triangle(5)
 print("Is 'radar' palindrome?", checkPalindrome("radar"))
 print("Unique elements:", UniqueElements(data))
 print("Is 'listen' anagram of 'silent'?", is_anagram("listen","silent"))
 countdown(5)
 print("Is 10 even?", is_even(10))
 print("Iterative Fibonacci of 7:", fibonacci_iterative(7))
 person=Person("Alice",30)
 person.greet()
 string_ops=StringOps
 print("Reverse 'hello':", string_ops.ReverseString("hello"))
 print("To upper 'world':", string_ops.ToUpperCase("world"))

main()

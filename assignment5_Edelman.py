# creating a class for basic math operations
class BasicMathOperations:
    # creating a function that takes in a first name and last name as inputs and returns a greeting
    def GreetUser(self,f_n,l_n):
        print(f"Hello {f_n} {l_n}")
    # creating a function that takes in two numbers and returns the sum
    def AddNumbers(self,num1,num2):
        return num1+num2
    # creating a function that adds, subtracts, multiplies, or divides a number based on a string input
    def PerformOp(self,num1,num2,operator):
        if operator.upper()=="A":
            return num1+num2
        if operator.upper()=="S":
            return num1-num2
        if operator.upper()=="M":
            return num1*num2
        if operator.upper()=="D":
            if num2==0:
                return "infinity"
            else:
                return num1/num2
    # creating a function that returns the square of a number
    def calculateSqare(self,num):
        return num**2
    # creating a function that retuns the factorial of a number
    def factorial(self,num):
        if num==0:
            return 1
        fact=1
        for i in range(1,num+1):
            fact*=i
        return fact

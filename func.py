def main():
    num=int(input("enter number:"))#asking user for input
    def checkEvenOdd(): '''cfunction to check if the number entered is even or odd'''
    if num%2==0: #checking for divisibity  
        print("the number is even")
    else:
        print("the number is odd")
        
        """the function below is to find the cube and square of the number entered"""
    def squarecubenum():

         print("the square of the number is:",num**2) #squaring the number
         print("the cube of the number is:",num**3) #cubing the number
    squarecubenum()
    checkEvenOdd()
main()#function call

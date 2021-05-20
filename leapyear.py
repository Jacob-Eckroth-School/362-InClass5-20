def main():
   
   
    number = input("Please enter the year you want to check for leapyear status:")
    intNumber = int(number)

    if(isLeapYear(intNumber)):
        print("The year " + number + " is a leap year!")
    else:
        print("The year " + number + " is not a leap year.")
    

def isLeapYear(number):
    if(number % 400 == 0):
        return True
    elif(number %  100 == 0):
        return False
    elif(number % 4 == 0):
        return True
    else:
        return False

if __name__ == "__main__":
    main()
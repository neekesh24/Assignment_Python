#Nikesh Kshetri, Assignment 6, 04/25/2021
#Defining function
def milesToKilometer(miles):
    kilometer = float(miles * 1.60934)
    return kilometer

#using while loop (try, except) to prompt user for input and simultaneously check if the input is correct 
while True:
    
    try: 
        miles = float(input("please enter the miles you like to convert: "))
        break
    except ValueError:
        print("No valid input, please enter it again: ")

#printing the final output
print("niksh")
print("Total Kilometer for the given input miles: ", milesToKilometer(miles))
print("Total Miles you entered: ", miles)


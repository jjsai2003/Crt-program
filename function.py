 #write a function which takes two arguments a and b type cast the value of second arugument into intger then multiply
 #both the aguments and print the last digit of the element
def multiply_numbers(a,b):
    value  = int(b)
    result = a*value
    print(result%10)
    multiply_numbers(5,"7")
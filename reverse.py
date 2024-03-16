def rev(num):
    if(num==0):
        return
        print(num%10)
        return rev(num//10)
rev(123456)
#write a recursive function to count te number the digits of a number
#write a recursive function to calculate the sum of digits 
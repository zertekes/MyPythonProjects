def main():
    sum_number()
    
def sum_number():
    in_1 = int(input('Please enter the first number: '))
    in_2 = int(input('Please enter the second number: '))
    in_3 = int(input('Please enter the third number: '))
    
    if (in_1 == in_2 and in_2 == in_3):
        sum_x = (in_1+in_2+in_3)*3
        print('The tree number are equal. The sum*3 i= ', sum_x)
    else:
        sum_x = in_1+in_2+in_3
        print('The entered numbers sum is = ', sum_x)
    
if __name__ == '__main__': main()
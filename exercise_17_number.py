def main():
    check_number()
def in_number():
    x = int(input('Please enter a number: '))
    return x
def check_number():
    x_in = in_number()
    print(x_in)
    if x_in >= 100 and x_in<1000:
        print('The entered number between 100-1000.')
    elif (x_in >1000 and x_in<2000):
        print('The entered number between 1000-2000.')
    else:
        print('The entered number is not in the range.')

if __name__ == '__main__': main()
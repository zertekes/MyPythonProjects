def main():

    print_abs()
    
def in_number():
   n = int(input('Please enter a number: '))
   return n

def print_abs():
   x = in_number()
   print(abs.__doc__)
   print('The absolute is: ', abs(x))

if __name__ == '__main__': main()    
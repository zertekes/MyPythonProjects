def main():
    diff_number()
    
def in_number():
    x = int(input('Please enter a number: '))
    return x

def diff_number():
    in_x = in_number()    
    if in_x <= 17 :
        x_out = 17-in_x
        print('The result is: ', x_out)
    else:
        x_out = (abs(17-in_x))*2
        print('The result is: ', x_out)
        
if __name__ == '__main__': main()
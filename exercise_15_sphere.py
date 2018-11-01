import math

def main():
    volume_sphere()
def volume_sphere():
    r = float(input('Please enter the radius: '))
    p_pi = math.pi
    v = (4/3)*p_pi*(r**3)
    #return v
    print('The sphere volume is: ', v)
if __name__ == '__main__' : main()


#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    kitten('meow', 'grrr', 'purr')

def kitten(*arg):
    if len(arg):
        for s in arg:
            print(s)
    else: print('argument is empty')

if __name__ == '__main__': main()

def main():
    add_string()
def add_string():
    st_in = input('Please enter words: ')
    if (st_in != 'Is%'):
        st_new = 'Is'+st_in
        print(st_new)
    else:
        print(st_in)
if __name__ == '__main__': main()
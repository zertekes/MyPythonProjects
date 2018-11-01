in_list = input('please enter numbers separated by comma: ')
in_list = tuple(int(x) for x in in_list.split(','))
print (' tuple list: ', in_list)
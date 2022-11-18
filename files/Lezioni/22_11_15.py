def sum_list (my_list): 
    sum = 0
    if not my_list:
        sum = None
    for item in my_list:
        sum += item
    print ('sum result: {}' .format(sum))
    return sum

my_list = [1, 31.5, 4.37, 7, 105];
sum = sum_list(my_list)
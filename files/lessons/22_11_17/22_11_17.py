def sum_csv (file_name):
    elem = []
    sumresult = 0.0
    my_file = open(file_name, 'r')

    if my_file == []:
        return None 
        
    for line in my_file:
        elem = line.split (',')        
        if elem[0] != 'Date':
            elem[1] = float(elem [1])
            sumresult = sumresult + elem[1] 
    
    if sumresult == 0.0:
        return None
    return sumresult

    # codice che non lavora su autograding!!:
sumresult = sum_csv('shampoo_sales.txt')
print('sum result is: {}' .format(sumresult))

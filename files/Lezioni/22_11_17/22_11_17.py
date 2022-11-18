def sum_csv (my_file):
    sumresult = 0.0
    
    for line in my_file:
        elem = line.split (',')
        print ('{}' .format(elem))
        
        if elem[1] != 'Sales\n':
            elem[1] = float(elem [1])
            sumresult = sumresult + elem[1] 
    
    return sumresult

my_file = open ('shampoo_sales.txt', 'r')
result = sum_csv (my_file)
print ('{}' .format(result))
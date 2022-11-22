def sum_csv (file_name):
    elem = []
    sumresult = 0.0
    my_file = open(file_name, 'r')

    if len(my_file) == 0:
        return None 
        
    for line in my_file:
        elem = line.split (',')        
        if elem[0] != 'Date':
            elem[1] = float(elem [1])
            sumresult = sumresult + elem[1] 
    
    return sumresult
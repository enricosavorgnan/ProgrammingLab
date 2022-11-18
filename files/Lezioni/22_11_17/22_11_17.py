def sum_csv (file_name):
    sumresult = 0.0
    
    for line in file_name:
        elem = line.split (',')        
        if elem[1] != 'Sales\n':
            elem[1] = float(elem [1])
            sumresult = sumresult + elem[1] 
    
    return sumresult
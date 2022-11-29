class CSVFile ():
    def __init__(self, name):
        self.name = name                         #associo al file  il nome "shampoo_sales_copy"

    def get_data(self):
        my_list = []
        my_file = open((self.name)                #perché get_data apre il file specifico "shampoo_sales_copy.txt", non un generico oggetto "csvfile"

        #if len(my_file) == 0:
        if my_file == []:
            return None 
        
        for line in my_file:
            elements = line.strip('\n').split(',')     
            # .strip toglie "\n" da line
            # .split separa le linee di my_file in ","
            if elements[0] != 'Date':
                my_list.append (elements)      #.append aggiunge "elements" a "my_list"
        return my_list

csvfile = CSVFile ('shampoo_sales_copy.txt') #nel main, oggetto csvfile in classe CSVFile

#list = csvfile.get_data() 
#print (list) #list è lista che contiene ritorno di metodo get_data 
#csvfile.get_data() è metodo get_data() "applicato" a oggetto csvfile. P
#parentesi vuote perché self.name (per capirci, csvfile.name) è già definito prima

# in alternativa, senza dichiarare list:
print ('{}' .format(csvfile.get_data() ))
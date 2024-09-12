import csv

file = "tab_data_5exits_5OFs.txt"
f = open(file, 'r')
lines = f.readlines() #gets all lines of the file in a list
m = len(lines) #number of lines of raw output in the file

# of columns depends on:
OF_count = 0 #  i
# of rows depends on:
exit_count = 5 #  n

n = exit_count #this should be given as input
i = (m-1)/(2+n) #number of O/Fs aka columns


def get_Columns():
    columns = [] #an array to contain all the column arrays that will be created in the following loop

    loop_counter = 1 #skipping index 0 which corresponds to "isp" at beginning of file
    while (loop_counter < m):
        temp_arr = [] #initialize a temp arr containing value of the ith column
        exit_counter=0 #this counts from 0 to n
        loop_counter += 2 #skip the "chamber" and "throat" lines which precede each set of exit data
        for exit_counter in range(n):
            temp_arr.append(lines[loop_counter])
            loop_counter += 1
        #now all exits from 0 to n of this OF have been put into an array for that OFs column
        columns.append(temp_arr) #append the ith column array to columns
        #repeat until no values remain in file
        
    return columns

def get_Rows():
    #now that we have columns: to make the first row, take the 0th index of each column in order.
    #continue until you've gone up to n (# of exits)
    columns = get_Columns()
    rows = []
    for x in range(n): #where x is the index of the current exit we are at in the loop; starting at 0; ending at n
        temp_arr=[]
        for col in columns:
            temp_arr.append(col[x]) #take that exit value from each column and append it to the row array
        rows.append(temp_arr)  #append the nth row array to rows
    return rows

def corrected_Rows(): #accounts for 
    final_rows = []
    start = 0 #start will increase with each increment of row
    for row in get_Rows():
        temp_arr = []
        for col in range(start, len(row), n):
            temp_arr.append(row[col])
        start += 1
        final_rows.append(temp_arr)
    return final_rows

def get_Column_Headers(): #OF0, OF1, OF2,...
    headers = []
    for i in range(len(corrected_Rows()[0])): #because number of OFs = number of columns
        headers.append(f'O/F{i}')
    return headers

def create_csv():
    with open('CEA_Matrix.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(get_Column_Headers()) #writes column headers first
        for row in corrected_Rows():
            writer.writerow(row) #writes every row found in get_Rows()
    print("CSV created.")

def create_xlsx():
    pass

print(corrected_Rows())
create_csv()







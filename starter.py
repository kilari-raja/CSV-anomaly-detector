""" This file integrates command line execution to the tool. This redirects to trigger.py """

from trigger import *

def commaChecker(filesname):
    global row_no_in_original_file,counter
    counter = row_no_in_original_file = 0   
    you = get_mylist(filesname)
    with open(filesname,'rU') as data :
        defective_rows = count = 0
        for row in reader(data) :           
            row_no_in_original_file += 1
            if (len(row) != len(you)) :
                defective_rows += 1
                print "This file has rows with imperfect commas. Open \"improperData.txt\""
                print_improper_comma(defective_rows,row_no_in_original_file,row)            
            if (len(row) == len(you)):
                counter+=1
    return counter
def printHeader(filesname):
    you = get_mylist(filesname)
    print you
    return "inside printHeader function"
def sample_header(filesname,columns) :  
    global table,row_count  
    you = get_mylist(filesname)
    if columns in you:
        with open(filesname,'rU') as data :
            for line in data :
                row_count+=1
                if row_count >1 and row_count <= 11 :
                    cells = line.split(",")
                    table+=cells[you.index(columns)] + "\n"
            print table     
    else :
        print "header is not available"
    return "return from sample_header function" 
def count_rows(filesname):  
    row_count = 0   
    with open(filesname,'rU') as data :     
        for row in data:
            row_count+=1
    print "No of rows in",filesname,":",row_count
    return row_count

def ten_rows(filesname):    
    row_count = 0       
    with open(filesname,'rU') as data :
        for line in data:
            row_count+=1
            if row_count < 11:              
                stutter =''.join(line)
                print "\n" + stutter
    return "return from ten_rows"
    
def work_header(filesname,columns) :
    else_count = 0
    you = get_mylist(filesname)
    returnCommaChecker = commaChecker(filesname)
    returnRowCount  =  count_rows(filesname)
    for i in range(0,len(you)):     
        if columns in you[i]:               
            start = you.index(columns)
            end = you.index(columns)+1
            startTool(filesname,start,end,returnCommaChecker,returnRowCount)
            else_count += 1 
    if else_count == 0:
        print "header is not available"
    return "return from work_header"
def whole_file(filesname):
    you = get_mylist(filesname) 
    with open(filesname,'rU') as data :
        returnCommaChecker = commaChecker(filesname)
        returnRowCount  =  count_rows(filesname)
        for variable in range(0,len(you)):
            start = variable
            end = variable+1            
            startTool(filesname,start,end,returnCommaChecker,returnRowCount)
    return "return from whole_file"

@app.command
def columns(filename="something"):  
    open('improperData.txt', 'w').close()
    printHeader(filename)
@app.command
def sample(filename="filename"):    
    open('improperData.txt', 'w').close()
    ten_rows(filename)
@app.command
def sampleHeader(filename="filename",columns="headerName"): 
    open('improperData.txt', 'w').close()
    sample_header(filename,columns)
@app.command
def count(filename="filename"): 
    open('improperData.txt', 'w').close()
    count_rows(filename)
@app.command
def executeColumns(filename="filename",columns="headerName"):
    open('improperData.txt', 'w').close()
    work_header(filename,columns)    
@app.command
def execute(filename="filename"):   
    open('improperData.txt', 'w').close()
    whole_file(filename)
if __name__ == '__main__': 
    app.run() 
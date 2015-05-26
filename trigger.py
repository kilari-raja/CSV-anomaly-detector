from DisplayerIII import *
from Classifier import *
from Calculator import *

def commaChecker(filesname):
	you = get_mylist(filesname)	
	with open(filesname,'rU') as data :
		defective_rows = count = 0		
		for row in data :
			global row_no_in_original_file
			row_no_in_original_file += 1
			if (len(row.split(",")) != len(you)) :					
				defective_rows += 1
				with open('improperData.txt','a') as fp :
					count+=1
					if count == 1:							
						fp.write("_"*90 + "\n" + "THESE ROWS ARE PRINTED BECAUSE THEY HAVE IMPERFECT COMMAS\n" + "_"*90 + "\n" + str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n")
					new_row_no_in_original_file = row_no_in_original_file + 1
					fp.write("Row no in original file is ")
					fp.write(str(row_no_in_original_file)+"\n" + "\n")				
			if (len(row.split(",")) == len(you)):				
				global counter
				counter+=1
	return counter

def startTool(filesname,start,end):
	returnCommaChecker = commaChecker(filesname)
	if returnCommaChecker == row_no_in_original_file :		
		global you,datum
		you = get_mylist(filesname)
		datum = get_real_data(filesname)		
		for i in range(1,len(datum)):
			# for j in range(0,len(you)):
			regular_expressions(datum[i][start])
			purestringFunction(datum[i][start])
			stringFunction(datum[i][start])
			# pureStringWithSpacesFunction(datum[i][start])
			stringWithSpecialCharactersFunction(datum[i][start])
			websiteFunction(datum[i][start])
			websiteWithoutWWWFunction(datum[i][start])
			emailFunction(datum[i][start])								
			zipcodeFunction(datum[i][start])
			phoneFunction(datum[i][start])
			integerFunction(datum[i][start])
			stateCodeFunction(datum[i][start])
			emptyFunction(datum[i][start])
			calculation()
		print "bdict before observations",bdict
		observations(filesname,start,end,returnCommaChecker)		
	return "return from startTool"
	InstanceExecuteProgram = ExecuteProgram('mock.csv','2','3')	
def printHeader(filesname):
	you = get_mylist(filesname)
	print you
	return "inside printHeader function"
def sample_header(filesname,columns) :	
	table=""
	row_count=  0
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
	return "return from row count"
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
	for i in range(0,len(you)):		
		if columns in you[i]:				
			start = you.index(columns)
			end = you.index(columns)+1
			startTool(filesname,start,end)			
			else_count += 1	
	if else_count == 0:
		print "header is not available"
	return "return from work_header"
def whole_file(filesname):
	you = get_mylist(filesname)
	datum = get_real_data(filesname)	
	with open(filesname,'rU') as data :		
		# for variable in range(0,len(you)):
		# 	start = variable
		# 	end = variable+1
			# fix_file(filesname,start,end)
		startTool(filesname)		
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
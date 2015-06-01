from DisplayerIII import *
from Classifier import *
from Calculator import *

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
				with open('improperData.txt','a') as fp :
					count+=1
					if count == 1:							
						fp.write("_"*90 + "\n" + "THESE ROWS ARE PRINTED BECAUSE THEY HAVE IMPERFECT COMMAS\n" + "_"*90 + "\n" + str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n")
					new_row_no_in_original_file = row_no_in_original_file + 1
					fp.write("Row no in original file is ")
					fp.write(str(row_no_in_original_file)+"\n" + "\n")				
			if (len(row) == len(you)):
				counter+=1
	return counter

def startTool(filesname,start,end):
	returnCommaChecker = commaChecker(filesname)	
	# print "returnCommaChecker is",returnCommaChecker
	# print "row_no_in_original_file is",row_no_in_original_file
	if returnCommaChecker == row_no_in_original_file :		
		global you,datum
		you = get_mylist(filesname)
		datum = get_real_data(filesname)
		email_array = []
		bdict={}
		bdict[' valid_verified_zipcode_without_hyphen']=bdict['valid_verified_zipcode_with_two_hyphen']=bdict['zipcode_with_two_not_successive_hyphens']=bdict['valid_verified_zipcode_with_one_hyphen']=bdict['mostly_zipcode_with_one_hyphen']=bdict['mostly_zipcode_without_hyphen']=bdict['mostly_zipcode_with_two_hyphen']=bdict['mostly_zipcode_four_digits']=bdict['phone_no_two_hyphens']=bdict['phone_no_without_hyphen_or_alphabets']=bdict['phone_no_with_alphabets']=bdict['phone_no_with_parantheses']=bdict['phone_no_one_hyphen']=bdict['phone_no_with_only_open_parantheses']=bdict['phone_no_with_only_close_parantheses']=bdict['phone_three_parts_two_hyphens']=bdict['phone_three_parts_one_hyphen_one_parantheses']=bdict['phone_three_parts_plus_one']=bdict['phone_10_digits']=bdict['phone_no_two_hyphens']=bdict['phone_no_without_hyphen_or_alphabets']=bdict['phone_no_with_parantheses']=bdict['phone_no_one_hyphen']=bdict['phone_no_with_only_open_parantheses']=bdict['phone_no_with_only_close_parantheses']=bdict['string_with_space_no_integer']=bdict['string_with_integer_spaces']=bdict['pure_uppercase_string']=bdict['string_with_integer_hyphen']=bdict['string_without_integer_without_spaces']=bdict['string_with_symbol_instead_of_at']=bdict['two_letter_uppercase_string_not_state_code']=bdict['string_first_line_address']=bdict['string_with_dots_not_email_not_website']=bdict['two_letter_lowercase_string_not_state_code']=bdict['string_with_integer_without_spaces']=bdict['website']=bdict['website_without_www']=bdict['string_without_integer_without_spaces']=bdict['string_with_space_no_integer']=bdict['pure_uppercase_string']=bdict['two_letter_uppercase_string_not_state_code']=bdict['email_without_integer']=bdict['state_code']=bdict['string_with_special_characters']=bdict['integer_with_special_characters']=bdict['email_with_integer']=bdict['email_without_integer']=bdict['decimal_integer'] = bdict['integer_with_at'] = bdict['pure_integer'] = 0
		for i in range(1,len(datum)):			
			regular_expressions(datum[i][start])
			purestringFunction(datum[i][start],bdict)
			stringFunction(datum[i][start],bdict)
			# pureStringWithSpacesFunction(datum[i][start],bdict)
			stringWithSpecialCharactersFunction(datum[i][start],bdict)
			websiteFunction(datum[i][start],bdict)
			websiteWithoutWWWFunction(datum[i][start],bdict)
			emailReturn = emailFunction(datum[i][start],email_array,bdict)								
			zipcodeFunction(datum[i][start],bdict)
			phoneFunction(datum[i][start],bdict)
			integerFunction(datum[i][start],bdict)
			stateCodeFunction(datum[i][start],bdict)
			emptyFunction(datum[i][start],bdict)
			# calculation()			
		# print "bdict before observations is",bdict
		# print "emailReturn is",emailReturn			
		observations(filesname,start,end,returnCommaChecker,datum,emailReturn,bdict)		
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
	# datum = get_real_data(filesname)
	with open(filesname,'rU') as data :		
		for variable in range(0,len(you)):
			start = variable
			end = variable+1			
			startTool(filesname,start,end)
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
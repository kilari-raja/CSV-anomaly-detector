# from Classifier import *
# from Reader import *
from Calculator import *
# from Displayer import *
arr = rows = []
dictator = {}
row_no_in_original_file = 0
open('improperData.txt', 'w').close()

def get_mylist(filesname) :
	r = csv.reader(open(filesname, "rU"), dialect=csv.excel_tab)	
	line1=r.next()
	for element in line1:
		mylist = element.split(',')
	return mylist
def get_real_data(filesname) :
	with open(filesname,'rU') as data :
		real_data = csv.reader(data)
		for row in real_data :
			rows.append(row)
	return rows	
# you = get_mylist()
# datum = get_real_data()
# header = datum[0]
# del(datum[0])
j =0
def print_uppercase_entries():
	defective_rows = row_no_in_original_file = 0
	for i in range(0,len(datum)):
		# for j in range(0,len(datum[0])):
		find_uppercase = re.findall(pattern_uppercase,datum[i][j])
		row_no_in_original_file += 1
		if find_uppercase :
			with open('improperData.txt','a') as fp :
				defective_rows+=1
				if defective_rows == 1 : 
					global func_count
					func_count += 1
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE AN UPPERCASE STRING IS PRESENT IN COLUMN " + header[j] + " OF THE CSV FILE\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+	str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )				
def print_empty_entries(self):	
	defective_rows = row_no_in_original_file = 0
	for i in range(int(globvar),int(globar)):
		find_empty = re.findall(pattern_empty,datum[i][j])
		find_no_entry = re.findall(pattern_no_entry,datum[i][j])
		row_no_in_original_file += 1			
		if find_empty or find_no_entry :			
			with open('improperData.txt','a') as fp :
				defective_rows+=1
				if defective_rows == 1 : 
					global func_count
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE THE COLUMN " + header[j] + " OF THE CSV FILE IS EMPTY \n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write("This row" + " has empty entry \n" + str(datum[i])+str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )
def print_string_entries(self):
	defective_rows = row_no_in_original_file = 0	
	for i in range(int(globvar),int(globar)):
		find_string = re.findall(pattern_string,datum[i][j])
		row_no_in_original_file += 1
		if find_string :
			with open('improperData.txt','a') as fp :
				defective_rows+=1
				if defective_rows == 1 :
					global func_count
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE A STRING IS PRESENT IN COLUMN " + header[j] + " OF THE CSV FILE\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains string \n" + str(datum[i])+str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )			
def print_string_without_hyphen_entries(self):
	defective_rows = row_no_in_original_file = 0		
	for i in range(int(globvar),int(globar)):
		find_string = re.findall(pattern_string,datum[i][j])
		find_phone = re.findall(pattern_phone,datum[i][j])
		row_no_in_original_file += 1
		if find_string and not find_phone :
			with open('improperData.txt','a') as fp :
				defective_rows+=1
				if defective_rows == 1 :
					global func_count
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE A STRING WITHOUT HYPHEN IS PRESENT IN COLUMN " + header[j] + " OF THE CSV FILE\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains string without hyphen \n" + str(datum[i])+str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )
def print_string_only_entries(self):
	defective_rows = row_no_in_original_file = 0	
	for i in range(int(globvar),int(globar)):
		find_string = re.findall(pattern_string,datum[i][j])
		row_no_in_original_file += 1
		if find_string and len(find_string) == len(datum[i][j]) :
			with open('improperData.txt','a') as fp :
				defective_rows+=1
				if defective_rows == 1 : 
					global func_count
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE THE ENTRY IN COLUMN " + header[j] + " OF THE CSV FILE CONTAINS ONLY STRINGS\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains string only entry\n" + str(datum[i])+	str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )	
def print_string_with_integer_and_space_entries(self):
	defective_rows = row_no_in_original_file = 0		
	for i in range(int(globvar),int(globar)):
		find_string = re.findall(pattern_string,datum[i][j])
		row_no_in_original_file += 1
		if find_string and find_integer and find_space :
			with open('improperData.txt','a') as fp :
				defective_rows+=1
				if defective_rows == 1 : 
					global func_count
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE A STRING WITH INTGER AND SPACES IS PRESENT IN COLUMN " + header[j] + " OF THE CSV FILE\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains string with integer and spaces\n" + str(datum[i])+str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )	
	return "inside function print_string_with_integer_and_space_entries "	
def print_integer_entries(self):	        
	defective_rows = row_no_in_original_file = 0				
	for i in range(int(globvar),int(globar)):		
		find_integer = re.findall(pattern_integer,datum[i][j])
		row_no_in_original_file += 1				
		if find_integer and len(find_integer)!=len(datum[i][j]):
			with open('improperData.txt','a') as fp :
				defective_rows += 1
				if defective_rows == 1 : 
					global func_count
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE AN INTEGER IS PRESENT IN COLUMN " + header[j] + " OF THE CSV FILE\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains integer entries\n" + str(datum[i])+str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )
	return "inside function print_integer_entries "	
def print_integer_only_entries(self):	
	defective_rows = row_no_in_original_file = 0	
	for i in range(int(globvar),int(globar)):
		find_integer = re.findall(pattern_integer,datum[i][j])
		find_string = re.findall(pattern_string,datum[i][j])
		row_no_in_original_file += 1				
		if find_integer and not find_string and len(find_integer)==len(datum[i][j]) :
			with open('improperData.txt','a') as fp :
				defective_rows += 1
				if defective_rows == 1 : 
					global func_count
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE ONLY INTEGER IS PRESENT IN COLUMN " + header[j] + " OF THE CSV FILE\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains integer only entries \n" + str(datum[i])+	str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )
	return "inside function print_integer_only_entries "	
def print_improper_decimal_integers(self):
	defective_rows = row_no_in_original_file = 0	
	counter_decimal_integer = Counter(decimal_integer_lengths)
	for i in range(int(globvar),int(globar)):		
		find_integer = re.findall(pattern_integer,datum[i][j])
		find_string = re.findall(pattern_string,datum[i][j])
		find_dot = re.findall(pattern_dot,datum[i][j])
		row_no_in_original_file += 1
		if find_integer and not find_string and len(decimal_integer_lengths) > 0  and len(find_dot) != counter_decimal_integer.most_common(1)[0][0]:
			with open('improperData.txt','a') as fp :
				defective_rows += 1
				if defective_rows == 1 : 
					global func_count
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE IMPROPER DECIMAL INTEGER IS PRESENT IN COLUMN " + header[j] + " OF THE CSV FILE\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+	str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )
	return "inside function print_improper_decimal_integers"
def improper_integer_entries(self):
	defective_rows = row_no_in_original_file = 0	
	for i in range(int(globvar),int(globar)):
		find_space = re.findall(pattern_space,datum[i][j])
		find_empty = re.findall(pattern_empty,datum[i][j])
		find_phone = re.findall(pattern_phone,datum[i][j])
		find_integer = re.findall(pattern_integer,datum[i][j])
		find_string = re.findall(pattern_string,datum[i][j])
		find_hashtag = re.findall(pattern_hashtag,datum[i][j])
		find_pattern_phone_parantheses = re.findall(patten_phone_parantheses,datum[i][j])	
		find_slash = re.findall(pattern_slash,datum[i][j])	
		row_no_in_original_file += 1
		if len(find_phone) == 1 and len(find_integer) != 10 and not find_string and not find_hashtag and not find_pattern_phone_parantheses and not find_slash :
			with open('improperData.txt','a') as fp :
				defective_rows += 1
				if defective_rows == 1 :
					global func_count
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE IMPROPER INTEGER IS PRESENT IN COLUMN " + header[j] + " OF THE CSV FILE\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+	str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )
	return "inside function improper_integer_entries "	
def print_email_entries(self):
	defective_rows = row_no_in_original_file = 0
	for i in range(int(globvar),int(globar)):		
		find_email = re.findall(pattern_email,datum[i][j])
		find_dot = re.findall(pattern_dot,datum[i][j])
		find_space = re.findall(pattern_space,datum[i][j])
		row_no_in_original_file += 1							
		if find_email and find_dot and not find_space :
			with open('improperData.txt','a') as fp :
				defective_rows += 1
				if defective_rows == 1 :
					global func_count
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE A EMAIL IS PRESENT IN COLUMN " + header[j] + " OF THE CSV FILE\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+	str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )
	return "inside function print_email_entries "
def print_website_entries(self):
	defective_rows = row_no_in_original_file = 0	
	for i in range(int(globvar),int(globar)):		
		find_website = re.findall(pattern_website,datum[i][j])
		find_dot = re.findall(pattern_dot,datum[i][j])
		row_no_in_original_file += 1				
		if find_website and find_dot:
			with open('improperData.txt','a') as fp :
				defective_rows += 1
				if defective_rows == 1 : 
					global func_count
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE WEBSITE IS PRESENT IN COLUMN " + header[j] + " OF THE CSV FILE\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+	str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )
	return "inside function print_website_entries "	
def print_special_characters(self):
	defective_rows = row_no_in_original_file = 0	
	for i in range(int(globvar),int(globar)):
		find_special_characters=re.findall(pattern_special_characters,datum[i][j])
		row_no_in_original_file += 1
		if find_special_characters :
			with open('improperData.txt','a') as fp :
				defective_rows += 1
				if defective_rows == 1 : 
					global func_count
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE SPECIAL CHARACTERS ARE PRESENT IN COLUMN " + header[j] + " OF THE CSV FILE\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+	str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )
	return "inside function print_special_characters "	
def print_special_characters_phone(self):
	defective_rows = row_no_in_original_file = 0	
	for i in range(int(globvar),int(globar)):		
		find_special_characters_phone=re.findall(pattern_special_characters_phone,datum[i][j])
		row_no_in_original_file += 1
		if find_special_characters_phone :
			with open('improperData.txt','a') as fp :
				defective_rows += 1
				if defective_rows == 1 : 
					global func_count
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE SPECIAL CHARACTERS (unlikely for phone) ARE PRESENT IN COLUMN " + header[j] + " OF THE CSV FILE\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )	
	return "inside function  print_special_characters_phone"	
def print_special_characters_website(self):
	defective_rows = row_no_in_original_file = 0	
	for i in range(int(globvar),int(globar)):		
		find_special_characters_website=re.findall(pattern_special_characters_website,datum[i][j])
		row_no_in_original_file += 1
		if find_special_characters_website :
			with open('improperData.txt','a') as fp :
				defective_rows += 1
				if defective_rows == 1 : 
					global func_count
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE SPECIAL CHARACTERS (unlikely for website) IS PRESENT IN COLUMN " + header[j] + " OF THE CSV FILE\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+	str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )
	return "inside function print_special_characters_website "	
def print_hyphen(self):	
	defective_rows = row_no_in_original_file = 0	
	for i in range(int(globvar),int(globar)):			
		find_phone=re.findall(pattern_phone,datum[i][j])					
		row_no_in_original_file += 1
		if find_phone :
			with open('improperData.txt','a') as fp :
				defective_rows += 1
				if defective_rows == 1 : 
					global func_count
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE A HYPHEN IS PRESENT IN COLUMN " + header[j] + " OF THE CSV FILE\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+	str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )
	return "inside function print_hyphen  "	
def print_space_entries(self):
	defective_rows = row_no_in_original_file = 0	
	for i in range(int(globvar),int(globar)):		
		find_space = re.findall(pattern_space,datum[i][j])
		find_string = re.findall(pattern_string,datum[i][j])
		find_integer = re.findall(pattern_integer,datum[i][j])
		row_no_in_original_file += 1				
		if (find_string and find_space) or (find_integer and find_space):
			with open('improperData.txt','a') as fp :
				defective_rows += 1
				if defective_rows == 1 : 
					global func_count
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE SPACE IS PRESENT IN COLUMN " + header[j] + " OF THE CSV FILE\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+	str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )
	return "inside function print_space_entries "	
def print_no_dots(self):
	defective_rows = row_no_in_original_file = 0	
	for i in range(int(globvar),int(globar)):		
		find_string = re.findall(pattern_string,datum[i][j])
		find_dot = re.findall(pattern_dot,datum[i][j])
		row_no_in_original_file += 1				
		if (find_string and not find_dot) :
			with open('improperData.txt','a') as fp :
				defective_rows += 1
				if defective_rows == 1 : 
					global func_count
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE NO DOTS ARE PRESENT IN COLUMN " + header[j] + " OF THE CSV FILE\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+	str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )
	return "inside function print_no_dots "	
def print_pure_integer_not_zipcode(self):
	defective_rows = row_no_in_original_file = 0		
	for i in range(int(globvar),int(globar)):		
		find_integer = re.findall(pattern_integer,datum[i][j])
		find_string = re.findall(pattern_string,datum[i][j])
		find_phone = re.findall(pattern_phone,datum[i][j])
		find_zipcode_without_hyphen= re.findall(pattern_zipcode_without_hyphen,datum[i][j])	
		find_zipcode_four_digits=re.findall(patter_zipcode_four_digits,datum[i][j])	
		find_dot = re.findall(pattern_dot,datum[i][j])
		row_no_in_original_file += 1		
		if find_integer and not find_phone and not find_zipcode_without_hyphen and not find_zipcode_four_digits and not find_string and not find_dot:
			with open('improperData.txt','a') as fp :
				defective_rows += 1
				if defective_rows == 1 : 
					global func_count
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE PURE INTEGER(but not zipcode) IS PRESENT IN COLUMN " + header[j] + " OF THE CSV FILE\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+	str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )					
	return "inside function print_pure_integer_not_zipcode "	
def print_integer_more_than_string(self):
	defective_rows = row_no_in_original_file = 0	
	for i in range(int(globvar),int(globar)):		
		find_integer = re.findall(pattern_integer,datum[i][j])
		find_string = re.findall(pattern_string,datum[i][j])	
		find_website = re.findall(pattern_website,datum[i][j])				
		row_no_in_original_file += 1				
		if (len(find_integer) > len(find_string) and not find_website) :
			with open('improperData.txt','a') as fp :
				defective_rows += 1
				if defective_rows == 1 : 
					global func_count
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE INTEGERS DOMINATE STRING IN COLUMN " + header[j] + " OF THE CSV FILE\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+	str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )
	return "inside function print_integer_more_than_string "	
def print_string_more_than_integer(self):
	defective_rows = row_no_in_original_file = 0	
	for i in range(int(globvar),int(globar)):		
		find_integer = re.findall(pattern_integer,datum[i][j])
		find_string = re.findall(pattern_string,datum[i][j])					
		row_no_in_original_file += 1				
		if (len(find_string) > len(find_integer)) :
			with open('improperData.txt','a') as fp :
				defective_rows += 1
				if defective_rows == 1 : 
					global func_count
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE THE ENTRY IN COLUMN " + header[j] + " HAS MORE STRING THAN INTEGER\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+	str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )
	return "inside function print_string_more_than_integer"	
def print_not_state_code(self):
	defective_rows = row_no_in_original_file = 0	
	for i in range(int(globvar),int(globar)):		
		row_no_in_original_file += 1						
		if (datum[i][j] not in states) or (datum[i][j] not in lower_states) or (datum[i][j] not in upper_states) or (datum[i][j] != " ") or (datum[i][j] != "") :
			with open('improperData.txt','a') as fp :
				defective_rows+=1
				if defective_rows == 1 :
					global func_count
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE THE ENTRY IN COLUMN " + header[j] + " IS NOT A US STATE\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+	str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )
	return "inside function print_not_state_code "	
def print_symbols(self):
	return "inside function print_symbols"
	print_string_with_symbol_at_but_not_email()
	print_string_with_parantheses()
	print_integer_with_symbol_at_but_not_email()
	print_integer_with_symbol_at_and_dot()
	print_integer_with_parantheses()
	print_string_with_hashtag_without_space()
	print_integer_with_hashtag_without_space()			
def print_string_with_symbol_at_but_not_email (self):	
	defective_rows = row_no_in_original_file = 0
	for i in range(int(globvar),int(globar)):		
		row_no_in_original_file += 1
		global func_count
		find_string = re.findall(pattern_string,datum[i][j])
		find_at_the_rate=re.findall(pattern_at_the_rate,datum[i][j])
		find_dot = re.findall(pattern_dot,datum[i][j])					
		if find_string and find_at_the_rate and not find_dot :			
			with open('improperData.txt','a') as fp :
				defective_rows+=1
				if defective_rows == 1 :		 
					# global func_count
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE THE ENTRY IN COLUMN " + header[j] + " OF THE CSV FILE CONTAINS @ BUT IS NOT EMAIL\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+	str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )
	return "inside function print_string_with_symbol_at_but_not_email "	
def print_string_with_hashtag_without_space (self):	
	defective_rows = row_no_in_original_file = 0
	for i in range(int(globvar),int(globar)):		
		row_no_in_original_file += 1
		global func_count
		find_string = re.findall(pattern_string,datum[i][j])
		find_hashtag = re.findall(pattern_hashtag,datum[i][j])
		find_space = re.findall(pattern_space,datum[i][j])
		if find_string and find_hashtag and not find_space :
			with open('improperData.txt','a') as fp :
				defective_rows+=1
				if defective_rows == 1 :
					# global func_count
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE # IS FOUND ALONGSIDE STRINGS IN COLUMN " + header[j] + " OF THE CSV FILE\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+	str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )	
def print_integer_with_hashtag_without_space (self):				
	defective_rows = row_no_in_original_file = 0
	for i in range(int(globvar),int(globar)):		
		row_no_in_original_file += 1
		global func_count
		find_integer = re.findall(pattern_integer,datum[i][j])				
		find_hashtag = re.findall(pattern_hashtag,datum[i][j])
		find_space = re.findall(pattern_space,datum[i][j])
		if find_integer and find_hashtag and not find_space :	
			with open('improperData.txt','a') as fp :
				defective_rows+=1
				if defective_rows == 1 :
					# global func_count
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE # IS FOUND ALONGSIDE INTEGERS IN COLUMN " + header[j] + " OF THE CSV FILE\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+	str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )
	return "inside function print_integer_with_hashtag_without_space "					
def print_string_with_parantheses (self):	
	defective_rows = row_no_in_original_file = 0
	for i in range(int(globvar),int(globar)):		
		row_no_in_original_file += 1
		global func_count
		find_string = re.findall(pattern_string,datum[i][j])	
		find_open_parantheses=re.findall(pattern_open_parantheses,datum[i][j])
		find_close_paranthses=re.findall(pattern_close_parantheses,datum[i][j])
		if (find_string and find_open_parantheses) or (find_string and find_close_paranthses):		
			with open('improperData.txt','a') as fp :	
				defective_rows+=1
				if defective_rows == 1 :		
					# global func_count
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE PARANTHESES IS FOUND ALONGSIDE STRING IN COLUMN " + header[j] + " OF THE CSV FILE\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+	str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )
	return "inside function print_string_with_parantheses "
def print_integer_with_symbol_at_but_not_email (self):	
	defective_rows = row_no_in_original_file = 0
	for i in range(int(globvar),int(globar)):		
		row_no_in_original_file += 1
		global func_count
		find_integer = re.findall(pattern_integer,datum[i][j])		
		find_at_the_rate=re.findall(pattern_at_the_rate,datum[i][j])
		find_dot = re.findall(pattern_dot,datum[i][j])
		if find_integer and find_at_the_rate and not find_dot :			
			defective_rows+=1
			with open('improperData.txt','a') as fp :	
				if defective_rows == 1 :
					# global func_count
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE @ IS FOUND ALONGSIDE INTEGERS IN COLUMN " + header[j] + " OF THE CSV FILE\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+	str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )					
	return "inside function print_integer_with_symbol_at_but_not_email "	
def print_integer_with_symbol_at_and_dot (self):	
	defective_rows = row_no_in_original_file = 0
	for i in range(int(globvar),int(globar)):		
		row_no_in_original_file += 1
		global func_count
		find_integer = re.findall(pattern_integer,datum[i][j])			
		find_at_the_rate=re.findall(pattern_at_the_rate,datum[i][j])
		find_dot = re.findall(pattern_dot,datum[i][j])
		find_string = re.findall(pattern_string,datum[i][j])	
		if find_integer and find_at_the_rate and find_dot and not find_string:
			defective_rows+=1
			with open('improperData.txt','a') as fp :
				if defective_rows == 1 :
					# global func_count
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE @ IS FOUND ALONGSIDE DECIMAL INTEGERS IN COLUMN " + header[j] + " OF THE CSV FILE\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+	str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )
	return "inside function print_integer_with_symbol_at_and_dot "			
def print_integer_with_parantheses  (self):	
	defective_rows = row_no_in_original_file = 0
	for i in range(int(globvar),int(globar)):		
		row_no_in_original_file += 1
		global func_count
		find_integer = re.findall(pattern_integer,datum[i][j])
		find_open_parantheses=re.findall(pattern_open_parantheses,datum[i][j])
		find_close_paranthses=re.findall(pattern_close_parantheses,datum[i][j])
		if (find_integer and find_open_parantheses) or (find_integer and find_close_paranthses):	
			defective_rows+=1
			with open('improperData.txt','a') as fp :	
				if defective_rows == 1 :		 
					# global func_count
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE INTEGER WITH PARANTHESES IS PRESENT IN COLUMN " + header[j] + " OF THE CSV FILE\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+	str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )							
	return "inside function print_integer_with_parantheses "	
def print_decimal_values(self):	
	defective_rows = row_no_in_original_file = 0
	for i in range(int(globvar),int(globar)):		
		row_no_in_original_file += 1
		global func_count
		find_integer = re.findall(pattern_integer,datum[i][j])	
		find_zipcode_without_hyphen= re.findall(pattern_zipcode_without_hyphen,datum[i][j])
		find_zipcode_four_digits=re.findall(patter_zipcode_four_digits,datum[i][j])
		find_string = re.findall(pattern_string,datum[i][j])
		find_dot = re.findall(pattern_dot,datum[i][j])
		if find_integer and not find_zipcode_without_hyphen and not find_zipcode_four_digits and not find_string and find_dot:
			defective_rows+=1
			with open('improperData.txt','a') as fp :	
				if defective_rows == 1 :		
					# global func_count
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE DECIMAL INTEGER IS PRESENT IN COLUMN " + header[j] + " OF THE CSV FILE\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+	str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )	
	return "inside function print_decimal_values "	
def print_state_code(self):
	defective_rows = row_no_in_original_file = 0	
	for i in range(int(globvar),int(globar)):		
		row_no_in_original_file += 1						
		if (datum[i][j] in state_code_array) and (datum[i][j] not in states_and_cities) :	
			for j in range(i+1,len(row)):
				key = (datum[i][j], row[you[j]])
				if key[0] == key[1] :	
					with open('improperData.txt','a') as fp :
						defective_rows+=1
						if defective_rows == 1 : 
							global func_count
							func_count += 1	 							
							fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE THE ENTRY IN COLUMN " + header[j] + " OF THE CSV FILE IS A US STATE\n" + "_"*90 + "\n")
						new_row_no_in_original_file = row_no_in_original_file + 1
						fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+	str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )	
		else : 
			pass
	return "inside function print_state_code "	
def print_state_code_lowercase(self):
	defective_rows = row_no_in_original_file = 0							
	for i in range(int(globvar),int(globar)):
		row_no_in_original_file += 1
		find_lowercase = re.findall(pattern_lowercase,datum[i][j])			
		if (datum[i][j].upper() in state_code_array) and find_lowercase:
			with open('improperData.txt','a') as fp :
				defective_rows+=1
				if defective_rows == 1 : 
					global func_count
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE THE ENTRY IN COLUMN " + header[j] + " OF THE CSV FILE IS A US STATE IN LOWERCASE\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+	str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )	
		else : 
			pass
	return "inside function print_state_code_lowercase"	
def print_zip_code(self):
	defective_rows = row_no_in_original_file = 0	
	for i in range(int(globvar),int(globar)):		
		row_no_in_original_file += 1
		find_phone = re.findall(pattern_phone,datum[i][j])
		find_string = re.findall(pattern_string,datum[i][j])
		find_integer = re.findall(pattern_integer,datum[i][j])
		find_pattern_phone_parantheses = re.findall(patten_phone_parantheses,datum[i][j])
		find_successive_hyphens =re.findall(pattern_successive_hyphens,datum[i][j])
		find_hashtag = re.findall(pattern_hashtag,datum[i][j])
		find_slash = re.findall(pattern_slash,datum[i][j])
		find_space = re.findall(pattern_space,datum[i][j])
		find_dot = re.findall(pattern_dot,datum[i][j])
		if len(find_phone) == 1 and len(find_integer) < 10 and not find_string and not find_hashtag and not find_pattern_phone_parantheses and not find_slash and not find_space  :
			y = datum[i][j].split("-")[0]						
			for j in range(0,len(zipcodes)-1):
				if y == zipcodes[j] :
					if(len(y)>3):
						for k in range(0,len(you)-1):
							if zipcodes[j+3] == row[you[k]]:
								with open('improperData.txt','a') as fp :
									defective_rows+=1
									if defective_rows == 1 :
										global func_count
										func_count += 1							
										fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED THE ENTRY IN COLUMN " + header[j] + " OF THE CSV FILE IS POSSIBLY A ZIP CODE WITH HYPHEN\n" + "_"*90 + "\n")
									new_row_no_in_original_file = row_no_in_original_file + 1
									fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+"Zipcode" + str(datum[i][j]) + " " + "belongs to " + zipcodes[j+1] + " in the state of " + zipcodes[j+2] + "\n" + str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n")										
				else :
					pass
		elif len(find_integer) == 5 and not find_phone and not find_hashtag and not find_dot and not find_string and not find_space :
			for j in range(0,len(zipcodes)-1):
				if datum[i][j] == zipcodes[j] :
					for k in range(0,len(you)-1):
						if zipcodes[j+3] == row[you[k]]:
							defective_rows+=1
							with open('improperData.txt','a') as fp :
								if defective_rows == 1 :
									func_count += 1							
									fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED THE ENTRY IN COLUMN " + header[j] + " OF THE CSV FILE IS POSSIBLY A ZIP CODE \n" + "_"*90 + "\n")
								new_row_no_in_original_file = row_no_in_original_file + 1
								fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+	"Zipcode" + str(datum[i][j]) + " " + "belongs to " + zipcodes[j+1] + " in the state of " + zipcodes[j+2] + "\n" + str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n")
				else :
					pass
		elif len(find_integer) == 4 and not find_phone and not find_hashtag and not find_dot and not find_string and not find_space :
			c = "0" + datum[i][j]
			for j in range(0,len(zipcodes)-1):
				if c == zipcodes[j] :
					for k in range(0,len(you)-1):
						if zipcodes[j+3] == row[you[k]]:		
							defective_rows+=1
							with open('improperData.txt','a') as fp :
								if defective_rows == 1 :		
									func_count += 1							
									fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED THE ENTRY IN COLUMN " + header[j] + " OF THE CSV FILE IS POSSIBLY A ZIP CODE \n" + "_"*90 + "\n")
								new_row_no_in_original_file = row_no_in_original_file + 1
								fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+	"Zipcode" + str(datum[i][j]) + " " + "belongs to " + zipcodes[j+1] + " in the state of " + zipcodes[j+2] + "\n" + str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n")
				else: 
					pass
		else : 
			pass										
	return "inside function print_zip_code "
def print_duplicate_email_entries(self):
	defective_rows = row_no_in_original_file = 0		
	duplicate_emails = [k for k,v in Counter(email_array).items() if v>1]
	if len(duplicate_emails) > 0 :
		row_no_in_original_file += 1
		for x in range(0,len(duplicate_emails))	:
			if duplicate_emails[x] in str(row) :
				with open('improperData.txt','a') as fp :
					defective_rows += 1
					if defective_rows == 1 :
						global func_count
						func_count += 1	 							
						fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE EMAIL ENTRY IN COLUMN " + header[j] + " OF THE CSV FILE IS DUPLICATED\n" + "_"*90 + "\n")
					new_row_no_in_original_file = row_no_in_original_file + 1
					fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+	str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )	
	return "inside function  print_duplicate_email_entries"
def print_improper_email_entries(self):
	return "inside function print_improper_email_entries"
	print_email_with_more_than_one_at()
	print_email_with_space()
	print_email_without_dot()
	print_string_without_email()
def print_email_with_more_than_one_at(self):
	defective_rows = row_no_in_original_file = 0	
	global func_count
	for i in range(int(globvar),int(globar)):
		find_string = re.findall(pattern_string,datum[i][j])			
		find_space = re.findall(pattern_space,datum[i][j])
		find_dot = re.findall(pattern_dot,datum[i][j])
		find_email = re.findall(pattern_email,datum[i][j])
		row_no_in_original_file += 1	
		if len(find_email) >=2 :
			with open('improperData.txt','a') as fp :
				defective_rows += 1
				if defective_rows == 1 :		
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE @ OCCURS TWICE IN COLUMN " + header[j] + " OF THE CSV FILE\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+	str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )	
	return "inside function print_email_with_more_than_one_at "	
def print_email_with_space(self):
	defective_rows = row_no_in_original_file = 0		
	global func_count
	for i in range(int(globvar),int(globar)):	
		find_string = re.findall(pattern_string,datum[i][j])			
		find_space = re.findall(pattern_space,datum[i][j])
		find_dot = re.findall(pattern_dot,datum[i][j])
		find_email = re.findall(pattern_email,datum[i][j])
		row_no_in_original_file += 1
		if find_string and find_email and find_dot and find_space :
			with open('improperData.txt','a') as fp :
				defective_rows += 1
				if defective_rows == 1 :		
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE AN EMAIL WITH EMPTY SPACE IS PRESENT IN COLUMN " + header[j] + " OF THE CSV FILE\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+	str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )	
	return "inside function print_email_with_space "
def print_email_without_dot(self):
	defective_rows = row_no_in_original_file = 0		
	global func_count
	for i in range(int(globvar),int(globar)):	
		find_string = re.findall(pattern_string,datum[i][j])			
		find_space = re.findall(pattern_space,datum[i][j])
		find_dot = re.findall(pattern_dot,datum[i][j])
		find_email = re.findall(pattern_email,datum[i][j])
		row_no_in_original_file += 1
		if find_email and not find_dot :
			with open('improperData.txt','a') as fp :
				defective_rows += 1
				if defective_rows == 1 :
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE DOT IS NOT PRESENT IN COLUMN " + header[j] + " OF THE CSV FILE\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+	str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )	
	return "inside function print_email_without_dot"					
def print_string_without_email(self):
	defective_rows = row_no_in_original_file = 0		
	global func_count				
	for i in range(int(globvar),int(globar)):	
		find_string = re.findall(pattern_string,datum[i][j])			
		find_space = re.findall(pattern_space,datum[i][j])
		find_dot = re.findall(pattern_dot,datum[i][j])
		find_email = re.findall(pattern_email,datum[i][j])
		row_no_in_original_file += 1
		if find_string and not find_email :
			with open('improperData.txt','a') as fp :
				defective_rows += 1
				if defective_rows == 1 :		
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE @ IS NOT PRESENT IN COLUMN " + header[j] + " OF THE CSV FILE\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )	
	return "inside function print_string_without_email "	
def print_string_with_dots_not_email_not_website(self):
	defective_rows = row_no_in_original_file = 0		
	global func_count
	for i in range(int(globvar),int(globar)):	
		find_string = re.findall(pattern_string,datum[i][j])			
		find_space = re.findall(pattern_space,datum[i][j])
		find_dot = re.findall(pattern_dot,datum[i][j])
		find_email = re.findall(pattern_email,datum[i][j])
		find_integer = re.findall(pattern_integer,datum[i][j])
		find_empty = re.findall(pattern_empty,datum[i][j])
		find_no_entry = re.findall(pattern_no_entry,datum[i][j])
		find_website = re.findall(pattern_website,datum[i][j])
		row_no_in_original_file += 1
		if (find_string and find_integer and not find_empty and not find_no_entry  and find_dot and not find_email and not find_website) or (find_string and not find_integer and not find_empty and find_dot and not find_email and not find_website and not find_no_entry):
			with open('improperData.txt','a') as fp :
				defective_rows += 1
				if defective_rows == 1 :		
					func_count += 1	 							
					fp.write("_"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE DOT IS PRESENT IN COLUMN " + header[j] + " OF THE CSV FILE\n" + "_"*90 + "\n")
				new_row_no_in_original_file = row_no_in_original_file + 1
				fp.write(str(datum[i][j]) + " found in this row" + " contains uppercase\n" + str(datum[i])+	str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )	
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
					fp.write(str(new_row_no_in_original_file)+"\n" + "\n")				
			if (len(row.split(",")) == len(you)):				
				global counter
				counter+=1
def startTool(filesname):
	commaChecker(filesname)	
	if counter == row_no_in_original_file :
		you = get_mylist(filesname)
		datum = get_real_data(filesname)
		for i in range(1,len(datum)):
			for j in range(0,len(you)):
				regular_expressions(datum[i][j])
				purestringFunction(datum[i][j])
				stringFunction(datum[i][j])
				# pureStringWithSpacesFunction(datum[i][j])
				stringWithSpecialCharactersFunction(datum[i][j])
				websiteFunction(datum[i][j])
				websiteWithoutWWWFunction(datum[i][j])
				jug = emailFunction(datum[i][j])
				print "email_with_integeddsasdasdr is",jug
				zipcodeFunction(datum[i][j])
				phoneFunction(datum[i][j])
				integerFunction(datum[i][j])
				stateCodeFunction(datum[i][j])
				emptyFunction(datum[i][j])
				calculation()		
		observations()								
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
			# fix_file(filesname,start,end)
			startTool(filesname)
			else_count += 1
	if else_count == 0:
		print "header is not available"
	return "return from work_header"
def whole_file(filesname):
	you = get_mylist(filesname)
	datum = get_real_data(filesname)	
	with open(filesname,'rU') as data :		
		for variable in range(0,len(you)):
			start = variable
			end = variable+1
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
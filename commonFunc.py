""" This function is used while printing. This is where the dict in config.py comes in """

import config
from Reader import *

def print_in_improperTxt(datum,start,defective_rows,row_no_in_original_file,print_count,i,key_value,print_array):
	# print "key_value is",key_value	
	with open('improperData.txt','a') as fp :
		# defective_rows += 1
		if defective_rows == 1 :
			# print "print_count before incerement is",print_count
			print_count += 1
			# print "print_count after incerement is",print_count
			fp.write("*"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE " + (
				config.sortedDict[key_value][1] + " IS PRESENT IN COLUMN ") + (
				datum[0][start] + " OF THE CSV FILE\n" + "*"*90 + "\n"))	
		print_array.append(print_count)
		new_row_no_in_original_file = row_no_in_original_file + 1
		fp.write("\n"+str(datum[i][start]) + " found in this row contains " + (
			config.sortedDict[key_value][0] + " entries\n\n" + str(datum[i])+ "\n") + (
			"Defective row No:" + str(defective_rows) + "\n") + (
			"Row no in original file is " + str(new_row_no_in_original_file)+"\n\n" ))
	return print_count

def print_improper_comma(defective_rows,row_no_in_original_file,row):
	with open('improperData.txt','a') as fp :		
		if defective_rows == 1:							
			fp.write("_"*60 + "\n" + (
				"THESE ROWS ARE PRINTED BECAUSE THEY HAVE IMPERFECT COMMAS\n") +(
				"_"*60 + "\n" + str(row)+ "\n" + "Defective row No:") + (
				str(defective_rows) + "\n"))
		new_row_no_in_original_file = row_no_in_original_file + 1
		fp.write("Row no in original file is ")
		fp.write(str(row_no_in_original_file)+"\n" + "\n")	

# print datum[i][start] ,"belongs to",zipcodes[datum[i][start]][0],"in the state of",zipcodes[datum[i][start]][1]

def correct_place(datum):
	with open('improperData.txt','a') as fp :
		fp.write(datum + " belongs to " + zipcodes[datum][0] + (
			" in the state of " + zipcodes[datum][1] + "\n\n"))
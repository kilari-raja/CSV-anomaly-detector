import config
def print_in_improperTxt(datum,start,defective_rows,row_no_in_original_file,print_count,i,key_value):
	print "key_value is",key_value
	with open('improperData.txt','a') as fp :
		defective_rows += 1
		if defective_rows == 1 :
			print_count += 1
			fp.write("*"*90 + "\n" + "THIS ROW IS PRINTED BECAUSE " + config.sortedDict[key_value][1] + " IS PRESENT IN COLUMN " + datum[0][start] + " OF THE CSV FILE\n" + "*"*90 + "\n")
		new_row_no_in_original_file = row_no_in_original_file + 1
		fp.write(str(datum[i][start]) + " found in this row contains " + config.sortedDict[key_value][0] + " entries\n" + str(datum[i])+ "\n" + "Defective row No:" + str(defective_rows) + "\n" + "Row no in original file is " + str(new_row_no_in_original_file)+"\n" + "\n" )	
	return print_count

def print_improper_comma(defective_rows,row_no_in_original_file,row):
	with open('improperData.txt','a') as fp :		
		if defective_rows == 1:							
			fp.write("_"*60 + "\n" + "THESE ROWS ARE PRINTED BECAUSE THEY HAVE IMPERFECT COMMAS\n" + "_"*60 + "\n" + str(row)+ "\n" + "Defective row No:" + str(defective_rows) + "\n")
		new_row_no_in_original_file = row_no_in_original_file + 1
		fp.write("Row no in original file is ")
		fp.write(str(row_no_in_original_file)+"\n" + "\n")	
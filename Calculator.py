"""
This file ,based on the input, analyses the columns and decides which entry is anomalous and which isn't.
"""
from Classifier import *
from Reader import *
from DisplayerIII import *
count = 0
def calculation():
	if count > 0:
		print "***********************************************************"
		print "Your file has imperfect commas. Please open improperData.txt"
		print "*************************************************************"
	else:		
		global total_zipcode,total_phone,total_phone_only_integers,total_string,total_website,total_pure_string,total_special_characters, total_email
		total_zipcode = bdict['zipcode_with_two_not_successive_hyphens']+bdict['mostly_zipcode_with_one_hyphen']+bdict['mostly_zipcode_without_hyphen']+bdict['mostly_zipcode_with_two_hyphen']+bdict['mostly_zipcode_four_digits']
		total_phone = bdict['phone_no_two_hyphens']+bdict['phone_no_without_hyphen_or_alphabets']+bdict['phone_no_with_alphabets']+bdict['phone_no_with_parantheses']+bdict['phone_no_one_hyphen']+bdict['phone_no_with_only_open_parantheses']+bdict['phone_no_with_only_close_parantheses']+bdict['phone_three_parts_two_hyphens']+bdict['phone_three_parts_one_hyphen_one_parantheses']+bdict['phone_three_parts_plus_one']+bdict['phone_10_digits']
		total_phone_only_integers = bdict['phone_no_two_hyphens']+bdict['phone_no_without_hyphen_or_alphabets']+bdict['phone_no_with_parantheses']+bdict['phone_no_one_hyphen']+bdict['phone_no_with_only_open_parantheses']+bdict['phone_no_with_only_close_parantheses']
		total_string = bdict['string_with_space_no_integer']+bdict['string_with_integer_spaces']+bdict['pure_uppercase_string']+bdict['string_with_integer_hyphen']+bdict['string_without_integer_without_spaces']+bdict['string_with_symbol_instead_of_at']+bdict['two_letter_uppercase_string_not_state_code']+bdict['string_first_line_address']+bdict['string_with_dots_not_email_not_website']+bdict['two_letter_lowercase_string_not_state_code']+bdict['string_with_integer_without_spaces']
		total_website = bdict['website']+bdict['website_without_www']
		total_pure_string = bdict['string_without_integer_without_spaces']+bdict['string_with_space_no_integer']+bdict['pure_uppercase_string']+bdict['two_letter_uppercase_string_not_state_code']+bdict['email_without_integer']+bdict['state_code']
		total_special_characters = bdict['string_with_special_characters']+bdict['integer_with_special_characters']
		total_email = bdict['email_with_integer']+bdict['email_without_integer']		
		counter_decimal_integer = Counter(decimal_integer_lengths)
	return "return from calculation function"

def observations(filesname,start,end,counter):	
	print "\nOBSERVATIONS:"
	print "total_email is",total_email
	print "counter is",counter
	print "empty is",empty
	global special_characters_print
	if((total_email) > (9*(counter - empty))/10):		
		print "\tEmail dominates this column. Hence any other type of entries is considered a defective entry."
		print_improper_email_entries(filesname,start,end)		
		print_integer_only_entries(filesname,start,end)		
		print_integer_more_than_string(filesname,start,end)			
	if(empty) < (counter/10) and empty > 0 :
		print "\tMore than 90 percent of this column is filled with entries. Hence any empty entry is considered defective."
		# print_empty_entries(filesname,start,end)
		global print_empty_count
		print_empty_count+=1		
	if(state_code > (6*(counter - empty))/10):
		print "\tThis column is dominated by state codes. Hence integer dataypes are considered defective"		
		print_not_state_code(filesname,start,end)
		print_state_code_lowercase(filesname,start,end)	
	if(decimal_integer > (5*counter)/10) :
		print "\tDecimal integers dominate this column."
		# print_email_entries(filesname,start,end)
		print_symbols(filesname,start,end)
		print_string_entries(filesname,start,end)
		print_integer_only_entries(filesname,start,end)
		print_improper_decimal_integers(filesname,start,end)
	if(total_website > 5*(counter-empty)/10 ):
		print "total_website is",total_website
		print "couunter is",counter
		print "\tWebsite entries dominate more than half of the column."
		print_email_entries(filesname,start,end) 			
		print_integer_only_entries(filesname,start,end)		
		print_space_entries(filesname,start,end)
		print_no_dots(filesname,start,end)
		# print_integer_more_than_string(filesname,start,end)
		if special_characters_print == 0 :
			print_special_characters_website(filesname,start,end)
			# global special_characters_print
			special_characters_print+=1
		print_string_only_entries(filesname,start,end)
		# print_uppercase_entries(filesname,start,end)
		if(empty) < (counter/10) and empty > 0 :
			if print_empty_count == 0:
				print "\tCertain empty entries are found which are printed"
				# print_empty_entries(filesname,start,end)			

	if((total_pure_string) > (9*(counter - empty))/10):
		print "\tThis column is dominated by pure string entries. Hence any other datatype is considered defective "
		if(state_code > (6*(counter - empty))/10):
			print_integer_entries(filesname,start,end)
			print_email_entries(filesname,start,end)
			print_symbols(filesname,start,end)
		if(total_email > counter/2):
			print_integer_only_entries(filesname,start,end)
			print_space_entries(filesname,start,end)
			print_no_dots(filesname,start,end)
			print_symbols(filesname,start,end)
		else :								
			print_email_entries(filesname,start,end)
			print_state_code(filesname,start,end)
			if special_characters_print == 0:					
				print_special_characters(filesname,start,end)
				# global special_characters_print
				special_characters_print+=1
			print_hyphen(filesname,start,end)
			print_symbols(filesname,start,end)
			print_integer_entries(filesname,start,end)
			print_string_with_dots_not_email_not_website(filesname,start,end)
			global string_dots_no_email_or_website
			string_dots_no_email_or_website+=1	

	if(empty > (counter/3) ) :
		if(empty == counter):
			print "\tThis column is completely empty"
		else :
			print "\tMore than One third of this column is empty."
		if(website > (empty/2)) :
			print "\tHigh probability that this column represents website"
			if (email) :
				print "\tsome lines have email in the place of website."
	if((email_without_integer + email_with_integer) > (counter/2)) :
		print "\tVery high probability that this column represents email"
		global email_dominant_column
		email_dominant_column+=1
		print_improper_email_entries(filesname,start,end)
		# print_uppercase_entries(filesname,start,end)
		# print_duplicate_email_entries(filesname,start,end)
		if(empty):
			print "\tThere are empty records in this column"
	if (total_zipcode > 0) and (total_zipcode <= (counter/10)):				
			print_zip_code(filesname,start,end)
	if(total_phone_only_integers + pure_integer) > (5*counter)/10 :	
		print "\tPure integer occupy a large portion of this column. Hence any string entries are considered defective"
		print_string_without_hyphen_entries(filesname,start,end)
		if(total_phone) > (4*counter)/10 :
			if special_characters_print == 0:
				print_special_characters_phone(filesname,start,end)
				# global special_characters_print
				special_characters_print+=1
		else :
			if special_characters_print == 0:
				print_special_characters(filesname,start,end)
				# global special_characters_print
				special_characters_print+=1
		print_string_with_symbol_at_but_not_email(filesname,start,end)
		print_string_with_parantheses(filesname,start,end)
		print_integer_with_symbol_at_but_not_email(filesname,start,end)
		print_integer_with_symbol_at_and_dot(filesname,start,end)
		# print_integer_with_parantheses(filesname,start,end)
		print_string_with_hashtag_without_space(filesname,start,end)
		print_integer_with_hashtag_without_space(filesname,start,end)
		print_decimal_values(filesname,start,end)
	if(total_phone) > (4*counter)/10 :	
		print "\tPhone numbers occupy a large portion of this column. Hence any string integers are considered defective"
		print_string_entries(filesname,start,end)
		if special_characters_print == 0:
			print_special_characters_phone(filesname,start,end)
			# global special_characters_print
			special_characters_print+=1
	if(total_zipcode > (counter/2)) :
		print "\tHigh probability that this column represents zipcode"
		print_string_entries(filesname,start,end)
		print_email_entries(filesname,start,end)
		if special_characters_print == 0:
			print_special_characters(filesname,start,end)
			# global special_characters_print
			special_characters_print+=1
		print_pure_integer_not_zipcode(filesname,start,end)
	if(total_special_characters > 0) and (total_special_characters < (10*(counter-empty)/100)):
		print "\tthis column contains special characters"
		if special_characters_print == 0 and email_dominant_column == 0:
			print_special_characters(filesname,start,end)
			# global special_characters_print
			special_characters_print+=1	
	if(total_string > (9*counter)/10 or total_string > (counter - empty)/2 ) and (total_string > empty):
		print "\tThis column is definitely not email,website,zipcode or phone number"		
		global local_count
		local_count += 1
		if ((string_with_integer_spaces > (7*(counter-empty))/10)) :
			print "\tVery high probability that this is a line of address"				
			print_email_entries(filesname,start,end)					
		if (pure_integer != 0):						
			print_integer_only_entries(filesname,start,end)
		if(email !=0) :
			print_email_entries(filesname,start,end)
	if(total_pure_string < (10*(counter-empty)/100)) and total_pure_string !=0 :
		if(total_string > counter-empty/2):
			print "\tString with other datatypes dominate but pure strings are also present"
		if(total_website > 5*(counter-empty)/10 ):
			pass
		else :
			print "\tFew string entries are found. Hence printed"
			print_string_only_entries(filesname,start,end)
	if string_with_dots_not_email_not_website > 0 :
		if total_website > 5*(counter-empty)/10 :
			print "\tThis column is dominated by website entries"
		elif total_email > 5*(counter-empty)/10 :
			print "\tThis column is dominated by email entries"
		elif ((string_with_integer_spaces > (7*(counter-empty))/10)) :
			print "\tCould be a line of address"
		else :
			print "\tthis column is dominated by string with dots but they are not email or website"
			if string_dots_no_email_or_website == 0 :
				print_string_with_dots_not_email_not_website(filesname,start,end)
	if (state_code > (9*counter)/10) :
		if(local_count == 0):
			print "\tHigh probability that this column represents state code"
	if(uncertain_entries):
		if(local_count == 0):
			print "\tThis column contains entries which seem anamalous."		
		improper_integer_entries(filesname,start,end)
	if(func_count != 0):
		print "****************************"
		print "PLEASE OPEN improperData.txt"
		print "****************************"
	else:
		print "****************************"
		print "This column appears bug free"
		print "****************************"
	return "return from observation function"

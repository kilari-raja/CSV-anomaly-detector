"""
This file ,based on the input, analyses the columns and decides which entry is anomalous and which isn't.
"""

from Classifier import *
# from Reader import *
# from Displayer import *
count = 0
def calculation():	
	if count > 0:
		print "***********************************************************"
		print "Your file has imperfect commas. Please open improperData.txt"
		print "*************************************************************"
	else:
		print "email_with_integesdfsdfsdfsdfsdfsdfsdfsdr is",email_with_integer
		global total_zipcode,total_phone,total_phone_only_integers,total_string,total_website,total_pure_string,total_special_characters, total_email
		total_zipcode =  valid_verified_zipcode_without_hyphen + valid_verified_zipcode_with_two_hyphen + zipcode_with_two_not_successive_hyphens + valid_verified_zipcode_with_one_hyphen + mostly_zipcode_with_one_hyphen + mostly_zipcode_without_hyphen + mostly_zipcode_with_two_hyphen + mostly_zipcode_four_digits			
		total_phone = phone_no_two_hyphens + phone_no_without_hyphen_or_alphabets + phone_no_with_alphabets + phone_no_with_parantheses + phone_no_one_hyphen + phone_no_with_only_open_parantheses + phone_no_with_only_close_parantheses + phone_three_parts_two_hyphens + phone_three_parts_one_hyphen_one_parantheses + phone_three_parts_plus_one + phone_10_digits
		total_phone_only_integers = phone_no_two_hyphens + phone_no_without_hyphen_or_alphabets + phone_no_with_parantheses + phone_no_one_hyphen + phone_no_with_only_open_parantheses + phone_no_with_only_close_parantheses			
		total_string = string_with_space_no_integer + string_with_integer_spaces + pure_uppercase_string + string_with_integer_hyphen + string_without_integer_without_spaces + string_with_symbol_instead_of_at + two_letter_uppercase_string_not_state_code + string_first_line_address + string_with_dots_not_email_not_website + two_letter_lowercase_string_not_state_code + string_with_integer_without_spaces
		total_website = website + website_without_www
		total_pure_string = string_without_integer_without_spaces + string_with_space_no_integer + pure_uppercase_string + two_letter_uppercase_string_not_state_code + email_without_integer+state_code
		total_special_characters = string_with_special_characters + integer_with_special_characters		
		total_email = email_with_integer + email_without_integer
		print "total_email is",total_email
		counter_decimal_integer = Counter(decimal_integer_lengths)

	return "return from calculation function"

def observations():
	print "\nOBSERVATIONS:"
	print "total_email is",total_email	
	global special_characters_print
	if((email) > (9*(counter - empty))/10):		
		print "\tEmail dominates this column. Hence any other type of entries is considered a defective entry."
		InstanceExecuteProgram.print_improper_email_entries()		
		InstanceExecuteProgram.print_integer_only_entries()		
		InstanceExecuteProgram.print_integer_more_than_string()		
	if(empty) < (counter/10) and empty > 0 :
		print "\tMore than 90 percent of this column is filled with entries. Hence any empty entry is considered defective."
		# print_empty_entries()
		global print_empty_count
		print_empty_count+=1		
	if(state_code > (6*(counter - empty))/10):
		print "\tThis column is dominated by state codes. Hence integer dataypes are considered defective"		
		InstanceExecuteProgram.print_not_state_code()
		InstanceExecuteProgram.print_state_code_lowercase()	
	if(decimal_integer > (5*counter)/10) :
		print "\tDecimal integers dominate this column."
		# print_email_entries()
		InstanceExecuteProgram.print_symbols()
		InstanceExecuteProgram.print_string_entries()
		InstanceExecuteProgram.print_integer_only_entries()
		InstanceExecuteProgram.print_improper_decimal_integers()
	if(total_website > 5*(counter-empty)/10 ):
		print "\tWebsite entries dominate more than half of the column."		
		InstanceExecuteProgram.print_email_entries() 
		InstanceExecuteProgram.print_integer_only_entries()
		InstanceExecuteProgram.print_space_entries()
		InstanceExecuteProgram.print_no_dots()
		# print_integer_more_than_string()
		if special_characters_print == 0 :
			InstanceExecuteProgram.print_special_characters_website()
			# global special_characters_print
			special_characters_print+=1
		InstanceExecuteProgram.print_string_only_entries()
		# print_uppercase_entries()
		if(empty) < (counter/10) and empty > 0 :
			if print_empty_count == 0:
				print "\tCertain empty entries are found which are printed"
				# print_empty_entries()			

	if((total_pure_string) > (9*(counter - empty))/10):
		print "\tThis column is dominated by pure string entries. Hence any other datatype is considered defective "
		if(state_code > (6*(counter - empty))/10):
			InstanceExecuteProgram.print_integer_entries()
			InstanceExecuteProgram.print_email_entries()
			InstanceExecuteProgram.print_symbols()
		if(total_email > counter/2):
			InstanceExecuteProgram.print_integer_only_entries()
			InstanceExecuteProgram.print_space_entries()
			InstanceExecuteProgram.print_no_dots()
			InstanceExecuteProgram.print_symbols()
		else :								
			InstanceExecuteProgram.print_email_entries()
			InstanceExecuteProgram.print_state_code()
			if special_characters_print == 0:					
				InstanceExecuteProgram.print_special_characters()
				# global special_characters_print
				special_characters_print+=1
			InstanceExecuteProgram.print_hyphen()
			InstanceExecuteProgram.print_symbols()
			InstanceExecuteProgram.print_integer_entries()
			InstanceExecuteProgram.print_string_with_dots_not_email_not_website()
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
		InstanceExecuteProgram.print_improper_email_entries()
		# print_uppercase_entries()
		# print_duplicate_email_entries()
		if(empty):
			print "\tThere are empty records in this column"
	if (total_zipcode > 0) and (total_zipcode <= (counter/10)):				
			InstanceExecuteProgram.print_zip_code()
	if(total_phone_only_integers + pure_integer) > (5*counter)/10 :	
		print "\tPure integer occupy a large portion of this column. Hence any string entries are considered defective"
		InstanceExecuteProgram.print_string_without_hyphen_entries()
		if(total_phone) > (4*counter)/10 :
			if special_characters_print == 0:
				InstanceExecuteProgram.print_special_characters_phone()
				# global special_characters_print
				special_characters_print+=1
		else :
			if special_characters_print == 0:
				InstanceExecuteProgram.print_special_characters()
				# global special_characters_print
				special_characters_print+=1
		InstanceExecuteProgram.print_string_with_symbol_at_but_not_email()
		InstanceExecuteProgram.print_string_with_parantheses()
		InstanceExecuteProgram.print_integer_with_symbol_at_but_not_email()
		InstanceExecuteProgram.print_integer_with_symbol_at_and_dot()
		# print_integer_with_parantheses()
		InstanceExecuteProgram.print_string_with_hashtag_without_space()
		InstanceExecuteProgram.print_integer_with_hashtag_without_space()
		InstanceExecuteProgram.print_decimal_values()
	if(total_phone) > (4*counter)/10 :	
		print "\tPhone numbers occupy a large portion of this column. Hence any string integers are considered defective"
		InstanceExecuteProgram.print_string_entries()
		if special_characters_print == 0:
			InstanceExecuteProgram.print_special_characters_phone()
			# global special_characters_print
			special_characters_print+=1
	if(total_zipcode > (counter/2)) :
		print "\tHigh probability that this column represents zipcode"
		InstanceExecuteProgram.print_string_entries()
		InstanceExecuteProgram.print_email_entries()
		if special_characters_print == 0:
			InstanceExecuteProgram.print_special_characters()
			# global special_characters_print
			special_characters_print+=1
		InstanceExecuteProgram.print_pure_integer_not_zipcode()
	if(total_special_characters > 0) and (total_special_characters < (10*(counter-empty)/100)):
		print "\tthis column contains special characters"
		if special_characters_print == 0 and email_dominant_column == 0:
			InstanceExecuteProgram.print_special_characters()
			# global special_characters_print
			special_characters_print+=1	
	if(total_string > (9*counter)/10 or total_string > (counter - empty)/2 ) and (total_string > empty):
		print "\tThis column is definitely not email,website,zipcode or phone number"		
		global local_count
		local_count += 1
		if ((string_with_integer_spaces > (7*(counter-empty))/10)) :
			print "\tVery high probability that this is a line of address"				
			InstanceExecuteProgram.print_email_entries()					
		if (pure_integer != 0):						
			InstanceExecuteProgram.print_integer_only_entries()
		if(email !=0) :
			InstanceExecuteProgram.print_email_entries()
	if(total_pure_string < (10*(counter-empty)/100)) and total_pure_string !=0 :
		if(total_string > counter-empty/2):
			print "\tString with other datatypes dominate but pure strings are also present"
		if(total_website > 5*(counter-empty)/10 ):
			pass
		else :
			print "\tFew string entries are found. Hence printed"
			InstanceExecuteProgram.print_string_only_entries()
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
				InstanceExecuteProgram.print_string_with_dots_not_email_not_website()
	if (state_code > (9*counter)/10) :
		if(local_count == 0):
			print "\tHigh probability that this column represents state code"
	if(uncertain_entries):
		if(local_count == 0):
			print "\tThis column contains entries which seem anamalous."		
		InstanceExecuteProgram.improper_integer_entries()
	if(func_count != 0):
		print "****************************"
		print "PLEASE OPEN improperData.txt"
		print "****************************"
	else:
		print "****************************"
		print "This column appears bug free"
		print "****************************"
	return "return from observation function"
from TEST import *
import csv,unittest

class TestFunctions(unittest.TestCase):
	
	def test_website(self):
		self.assertEqual(websiteFunction("www.rajkumar.com"),'is possible website')
		self.assertEqual(websiteFunction("www.rr.com"),'is possible website')
		self.assertEqual(websiteFunction("www.r.com"),'single character domain name')
		self.assertEqual(websiteFunction("http://www.rajkumar.com"),'is possible website with http and slash')
		self.assertEqual(websiteWithoutWWWFunction("rajkumar.co.in"),'is possible website but without www (2 dot) and without slashes')
		self.assertEqual(websiteWithoutWWWFunction("rajkumar.com"),'is possible website but without www (1 dot)')
		self.assertEqual(websiteWithoutWWWFunction("raj.k.mar"),'is string with more than one dot but not website')

	def test_email(self):
		self.assertEqual(emailFunction("raj49@gmail.com"),'is possible email with integer')
		self.assertEqual(emailFunction("raj@gmail.com"),'is possible email but without integer')
	
	def test_string(self):
		self.assertEqual(purestringFunction("rajkumar"),'is string without integer and without spaces')
		self.assertEqual(purestringFunction("Rajkumar"),'is string with single caps with no integer or spaces')
		self.assertEqual(purestringFunction("R"),'is string of unit length with single caps')
		self.assertEqual(purestringFunction("RAJKUMAR"),'is pure uppercase string with more than 2 characters')
		self.assertEqual(purestringFunction("rAjkuMar"),'is string with capital letters but not state code nor pure uppercase')
		self.assertEqual(stringFunction("Raj.kumar"),'is string with dot but not email')
		self.assertEqual(stringFunction("raj.kumar"),'is string with dot but not email')  #full lowercase
		self.assertEqual(stringFunction("Raj@kumar"),'is string with @ instead of at')
		self.assertEqual(stringFunction("raj@kumar"),'is string with @ instead of at')  #full lowercase
		self.assertEqual(pureStringWithSpacesFunction("Raj kumar"),'is a pure string with spaces')
		self.assertEqual(pureStringWithSpacesFunction("raj kumar"),'is a pure string with spaces')
		self.assertEqual(pureStringWithSpacesFunction("RAJ KUMAR"),'is a pure string with spaces')
		self.assertEqual(stringWithSpecialCharactersFunction("Raj/kumar"),'is string with special characters')
		self.assertEqual(stringWithSpecialCharactersFunction("Raj[kumar"),'is string with special characters')
		self.assertEqual(stringWithSpecialCharactersFunction("Raj!kumar"),'is string with special characters')
		self.assertEqual(stringWithSpecialCharactersFunction("Raj$kumar"),'is string with special characters')
		self.assertEqual(stringWithSpecialCharactersFunction("Raj_kumar"),'is string with special characters')
		self.assertEqual(stringWithSpecialCharactersFunction("Raj\kumar"),'is string with special characters')
		self.assertEqual(stringWithSpecialCharactersFunction("Raj=kumar"),'is string with special characters')
		self.assertEqual(stringWithSpecialCharactersFunction("Raj:kumar"),'is string with special characters')
		self.assertEqual(stringWithSpecialCharactersFunction("Raj*kumar"),'is string with special characters')
		self.assertEqual(stringWithSpecialCharactersFunction("Raj~kumar"),'is string with special characters')
		self.assertEqual(stringWithSpecialCharactersFunction("Raj?kumar"),'is string with special characters')
		self.assertEqual(stringWithSpecialCharactersFunction("Raj<kumar"),'is string with special characters')
		self.assertEqual(stringWithSpecialCharactersFunction("Raj^kumar"),'is string with special characters')
		self.assertEqual(stringWithSpecialCharactersFunction("Raj%kumar"),'is string with special characters')

	def test_phone(self):
		self.assertEqual(phoneFunction("1800-AMY-4567"),'is possible phone no but with alphabets')
		self.assertEqual(phoneFunction("180/458-4567"),'is possible phone no but with slash instead of one of the hyphens')
		self.assertEqual(phoneFunction("180-874/4567"),'is possible phone no but with slash instead of one of the hyphens')
		self.assertEqual(phoneFunction("1800-874/4567"),'not phone no because more than ten integers with slash instead of one of the hyphens')
		self.assertEqual(phoneFunction("1800/874-4567"),'not phone no because more than ten integers with slash instead of one of the hyphens')
		self.assertEqual(phoneFunction("1800-125-4567"),'more than 10 integers and thus not a phone no')
		self.assertEqual(phoneFunction("(180)1254567"),'is phone no with parantheses')
		self.assertEqual(phoneFunction("180-254-5607"),'is phone with two hyphens')
		self.assertEqual(phoneFunction("(180) 254-5607"),'is phone no with three parts with one hyphen and a parantheseses')
		self.assertEqual(phoneFunction("(180 254-5607"),'is phone no with only open parantheses')
		self.assertEqual(phoneFunction("180) 254-5607"),'is phone no with only close parantheses')
		self.assertEqual(phoneFunction("180/874-467"),'not phone no because of less than ten integers but with slash instead of one of the hyphens')
		self.assertEqual(phoneFunction("180-874/567"),'not phone no because of less than ten integers but with slash instead of one of the hyphens')

	def test_zipcode(self):
		self.assertEqual(zipcodeFunction("83025-4567"),'is Most probably a zipcode with one hyphen')
		self.assertEqual(zipcodeFunction("82999-4567"),'has one hyphen but is not a zipcode')
		self.assertEqual(zipcodeFunction("83025--4567"),'is Most probably a zipcode with two hyphen')
		self.assertEqual(zipcodeFunction("82999--4567"),'has two hyphen but is not a zipcode')
		self.assertEqual(zipcodeFunction("83025-456-7"),'is possible zip codes but with two but not succesive hyphens')
		self.assertEqual(zipcodeFunction("82999-456-7"),'integer with two hyphens but not zipcode')
		self.assertEqual(zipcodeFunction("829-456-7"),'is integers separated by hyphen but not zipcode or phone number')

	def test_integer(self):
		self.assertEqual(integerFunction("raj567kumar"),'is string with integer without spaces')
		self.assertEqual(integerFunction("raj 567kumar"),'is string with integer and spaces')
		self.assertEqual(integerFunction("raj- 567kumar"),'is Mixture of string integer and hyphen and spaces')
		self.assertEqual(integerFunction("raj-567kumar"),'is Mixture of string integer and hyphen but not spaces')
		self.assertEqual(integerFunction("83025"),'is most probably a zipcode (without hyphen)')		
		self.assertEqual(integerFunction("6404"),'is most probably a zipcode (four digits)')
		self.assertEqual(integerFunction("82999"),'is not a Zipcode')
		self.assertEqual(integerFunction("9854"),'is a four digit integer')		
		self.assertEqual(integerFunction("82.96"),'is Integer with decimals')
		self.assertEqual(integerFunction("826"),'is Pure integer')
		self.assertEqual(integerFunction("1234567890"),'is 10 digit phone no')
		self.assertEqual(integerFunction("+1 123 456 7890"),'is phone with four parts containing three spaces and +1')
		self.assertEqual(integerFunction("11234567890"),'is 11 digit phone no i.e starts with 1 followed by 10 digits')
		self.assertEqual(integerFunction("21234567890"),'11 digit number but not phone no')
		self.assertEqual(integerFunction("-526"),'is Negative integer without decimals')
		self.assertEqual(integerFunction("-526.20"),'is Negative integer with decimals')
		self.assertEqual(integerFunction("-526."),'is decimal integer with misplaced dot')
		self.assertEqual(integerFunction("26*20"),'is integer with special characters')
		self.assertEqual(integerFunction("26/20"),'is integer with special characters')
		self.assertEqual(integerFunction("26_20"),'is integer with special characters')
		self.assertEqual(integerFunction("26?20"),'is integer with special characters')
		self.assertEqual(integerFunction("-26*20"),'is Negative integer with special characters')
		self.assertEqual(integerFunction("-26^20"),'is Negative integer with special characters')
		self.assertEqual(integerFunction("-26<20"),'is Negative integer with special characters')
		self.assertEqual(integerFunction("-26~20"),'is Negative integer with special characters')

	def test_statecode(self):
		self.assertEqual(stateCodeFunction("PA"),'is possible state code')
		self.assertEqual(stateCodeFunction("AB"),'is two lettered uppercase string not state code')
		self.assertEqual(stateCodeFunction("pa"),'is possible state code in lowercase')
		self.assertEqual(stateCodeFunction("ab"),'is two lettered lowercase string not state code')
		self.assertEqual(stateCodeFunction("ALASKA"),'is possible state name in capital letters')
		self.assertEqual(stateCodeFunction("alaska"),'is possible state name in lowercase')
		self.assertEqual(stateCodeFunction("tamilnadu"),'is not state name')
		self.assertEqual(stateCodeFunction("INDIA"),'is uppercase string')

	def test_empty(self):
		self.assertEqual(emptyFunction(""),"is empty")
		self.assertEqual(emptyFunction(" "),"is empty")

	def test_print_functions(self):
		self.assertEqual(InstanceExecuteProgram.print_uppercase_entries(),"inside function print_uppercase_entries ")
		self.assertEqual(InstanceExecuteProgram.print_empty_entries(),"inside function print_empty_entries ")
		self.assertEqual(InstanceExecuteProgram.print_string_entries(),"inside function print_string_entries ")
		self.assertEqual(InstanceExecuteProgram.print_string_without_hyphen_entries(),"inside function print_string_without_hyphen_entries ")
		self.assertEqual(InstanceExecuteProgram.print_string_only_entries(),"inside function print_string_only_entries ")
		self.assertEqual(InstanceExecuteProgram.print_string_with_integer_and_space_entries(),"inside function print_string_with_integer_and_space_entries ")
		self.assertEqual(InstanceExecuteProgram.print_integer_entries(),"inside function print_integer_entries ")
		self.assertEqual(InstanceExecuteProgram.print_integer_only_entries(),"inside function print_integer_only_entries ")
		self.assertEqual(InstanceExecuteProgram.print_improper_decimal_integers(),"inside function print_improper_decimal_integers")
		self.assertEqual(InstanceExecuteProgram.improper_integer_entries(),"inside function improper_integer_entries ")
		self.assertEqual(InstanceExecuteProgram.print_email_entries(),"inside function print_email_entries ")
		self.assertEqual(InstanceExecuteProgram.print_website_entries(),"inside function print_website_entries ")
		self.assertEqual(InstanceExecuteProgram.print_special_characters(),"inside function print_special_characters ")
		self.assertEqual(InstanceExecuteProgram.print_special_characters_phone(),"inside function  print_special_characters_phone")
		self.assertEqual(InstanceExecuteProgram.print_special_characters_website(),"inside function print_special_characters_website ")
		self.assertEqual(InstanceExecuteProgram.print_hyphen (),"inside function print_hyphen  ")
		self.assertEqual(InstanceExecuteProgram.print_space_entries (),"inside function print_space_entries ")
		self.assertEqual(InstanceExecuteProgram.print_no_dots(),"inside function print_no_dots ")
		self.assertEqual(InstanceExecuteProgram.print_pure_integer_not_zipcode(),"inside function print_pure_integer_not_zipcode ")
		self.assertEqual(InstanceExecuteProgram.print_integer_more_than_string(),"inside function print_integer_more_than_string ")
		self.assertEqual(InstanceExecuteProgram.print_string_more_than_integer(),"inside function print_string_more_than_integer")
		self.assertEqual(InstanceExecuteProgram.print_not_state_code(),"inside function print_not_state_code ")
		self.assertEqual(InstanceExecuteProgram.print_symbols(),"inside function print_symbols")
		self.assertEqual(InstanceExecuteProgram.print_string_with_symbol_at_but_not_email(),"inside function print_string_with_symbol_at_but_not_email ")
		self.assertEqual(InstanceExecuteProgram.print_string_with_hashtag_without_space (),"inside function print_string_with_hashtag_without_space ")
		self.assertEqual(InstanceExecuteProgram.print_integer_with_hashtag_without_space(),"inside function print_integer_with_hashtag_without_space ")
		self.assertEqual(InstanceExecuteProgram.print_string_with_parantheses(),"inside function print_string_with_parantheses ")
		self.assertEqual(InstanceExecuteProgram.print_integer_with_symbol_at_but_not_email(),"inside function print_integer_with_symbol_at_but_not_email ")
		self.assertEqual(InstanceExecuteProgram.print_integer_with_symbol_at_and_dot(),"inside function print_integer_with_symbol_at_and_dot ")
		self.assertEqual(InstanceExecuteProgram.print_integer_with_parantheses(),"inside function print_integer_with_parantheses ")
		self.assertEqual(InstanceExecuteProgram.print_decimal_values(),"inside function print_decimal_values ")
		self.assertEqual(InstanceExecuteProgram.print_state_code(),"inside function print_state_code ")
		self.assertEqual(InstanceExecuteProgram.print_state_code_lowercase (),"inside function print_state_code_lowercase")
		self.assertEqual(InstanceExecuteProgram.print_zip_code(),"inside function print_zip_code ")
		self.assertEqual(InstanceExecuteProgram.print_duplicate_email_entries(),"inside function  print_duplicate_email_entries")
		self.assertEqual(InstanceExecuteProgram.print_improper_email_entries(),"inside function print_improper_email_entries")
		self.assertEqual(InstanceExecuteProgram.print_email_with_more_than_one_at(),"inside function print_email_with_more_than_one_at ")
		self.assertEqual(InstanceExecuteProgram.print_email_with_space(),"inside function print_email_with_space ")
		self.assertEqual(InstanceExecuteProgram.print_email_without_dot(),"inside function print_email_without_dot")
		self.assertEqual(InstanceExecuteProgram.print_string_without_email(),"inside function print_string_without_email ")
		self.assertEqual(InstanceExecuteProgram.print_string_with_dots_not_email_not_website(),"inside function print_string_with_dots_not_email_not_website ")

	def test_startTool(self):		
		self.assertEqual(InstanceExecuteProgram.startTool(),"return from startTool")

	def test_observations(self):
		calculation()
		self.assertEqual(observations(),"return from observation function")

	def test_work_header(self):
		self.assertEqual(work_header('mock.csv','email'),"return from work_header")

	def test_sample_header(self):
		self.assertEqual(sample_header('mock.csv','id'),"return from sample_header function")

	def test_count_rows(self):
		self.assertEqual(count_rows('mock.csv'),"return from row count")

	def test_ten_rows(self):
		self.assertEqual(ten_rows('mock.csv'),"return from ten_rows")

	def test_printHeader(self):
		self.assertEqual(printHeader('mock.csv'),"inside printHeader function")

	def test_whole_file(self):
		self.assertEqual(whole_file('mock.csv'),"return from whole_file")

	def test_fix_file(self):
		self.assertEqual(InstanceExecuteProgram.fix_file('mock.csv','0','1'),"inside fix_File function")

if __name__ == '__main__' :
	unittest.main(exit=False)	




# import re
# pattern_string = re.compile("[a-zA-Z]+")
# pattern_caps = re.compile("[A-Z]")
# pattern_small = re.compile("[a-z]")
# pattern_integer = re.compile("[0-9]")
# pattern_email = re.compile("[\w+|\W+]@[\w+|\W+]")
# pattern_phone = re.compile("-")
# pattern_phone_three_parts_two_hyphens=re.compile("\d{3}-\d{3}-\d{4}")
# pattern_phone_three_parts_one_hyphen_one_parantheses=re.compile("\(\d{3}\) \d{3}-\d{4}")
# pattern_phone_three_parts_plus_one=re.compile("\+1 \d{3} \d{3} \d{4}")
# pattern_phone_11_digits=re.compile("\d{11}")
# pattern_phone_10_digits=re.compile("\d{10}")
# pattern_empty = re.compile("^\s*$")
# pattern_no_entry = re.compile("^(?![\s\S])")
# pattern_website = re.compile("www+|WWW+")
# pattern_dot = re.compile("[.]")
# pattern_word_after_dot = re.compile("[.][a-zA-Z]")
# pattern_http = re.compile("http")
# pattern_space = re.compile("[\w+|\W+]\s[\w+|\W+]")
# pattern_hashtag = re.compile("#")
# pattern_comma = re.compile(",")
# pattern_successive_hyphens = re.compile("--")
# patten_phone_parantheses = re.compile("\(\d+\)|\(\d+|\d+\)|\d+\(\d+\)")
# pattern_slash = re.compile("[\w+|\W+]/[\w+|\W+]")
# pattern_zipcode_one_hyphen = re.compile('^\d{5}-\d{4}$')
# pattern_zipcode_without_hyphen = re.compile('^\d{5}$')
# patter_zipcode_four_digits = re.compile('^\d{4}$')
# pattern_zipcode_two_hyphen = re.compile('^\d{5}--\d{4}$')
# pattern_special_characters = re.compile("[!|$|\\\\|/|%|^|+|=|_|*|}|~|\[|\]|:|?|`|<|>|{]")
# pattern_special_characters_website = re.compile("[\\\\|%|^|\||}|`|<|>|{]")
# pattern_special_characters_phone = re.compile("[!|$|\\\\|/|%|^|=|_|*|}|~|\[|\]|:|?|`|<|>|{]")
# pattern_open_parantheses =  re.compile("[()]")
# pattern_close_parantheses = re.compile("[)]")
# pattern_at_the_rate = re.compile("@")
# pattern_uppercase = re.compile("[A-Z]")
# pattern_lowercase = re.compile("[a-z]")

# adict = {}
# # class firstclass():
# def firstobject(entry):
# 	find_string = re.findall(pattern_string,entry)
# 	adict['find_string'] = find_string
# 	find_integer = re.findall(pattern_integer,entry)
# 	adict['find_integer'] = find_integer
# 	find_email = re.findall(pattern_email,entry)
# 	adict['find_email'] = find_email
# 	find_phone = re.findall(pattern_phone,entry)
# 	adict['find_phone'] = find_phone
# 	find_phone_three_parts_two_hyphens = re.findall(pattern_phone_three_parts_two_hyphens,entry)
# 	adict['find_phone_three_parts_two_hyphens'] = find_phone_three_parts_two_hyphens
# 	find_phone_three_parts_one_hyphen_one_parantheses = re.findall(pattern_phone_three_parts_one_hyphen_one_parantheses,entry)
# 	adict['find_phone_three_parts_one_hyphen_one_parantheses'] = find_phone_three_parts_one_hyphen_one_parantheses
# 	find_pattern_phone_three_parts_plus_one=re.findall(pattern_phone_three_parts_plus_one,entry)
# 	adict['find_pattern_phone_three_parts_plus_one'] = find_pattern_phone_three_parts_plus_one
# 	find_pattern_phone_11_digits = re.findall(pattern_phone_11_digits,entry)
# 	adict['find_pattern_phone_11_digits'] = find_pattern_phone_11_digits
# 	find_pattern_phone_10_digits = re.findall(pattern_phone_10_digits,entry)
# 	adict['find_pattern_phone_10_digits'] = find_pattern_phone_10_digits
# 	find_empty = re.findall(pattern_empty,entry)
# 	adict['find_empty'] = find_empty
# 	find_no_entry = re.findall(pattern_no_entry,entry)						
# 	adict['find_no_entry'] = find_no_entry 
# 	find_website = re.findall(pattern_website,entry)
# 	adict['find_website'] = find_website
# 	find_dot = re.findall(pattern_dot,entry)
# 	adict['find_dot'] = find_dot
# 	find_http = re.findall(pattern_http,entry)
# 	adict['find_http'] = find_http
# 	find_space = re.findall(pattern_space,entry)
# 	adict['find_space'] = find_space
# 	find_caps = re.findall(pattern_caps,entry)
# 	adict['find_caps'] =find_caps 
# 	find_word_after_dot = re.findall(pattern_word_after_dot,entry)
# 	adict['find_word_after_dot'] = find_word_after_dot
# 	find_hashtag = re.findall(pattern_hashtag,entry)
# 	adict['find_hashtag'] = find_hashtag
# 	find_comma = re.findall(pattern_comma,entry)
# 	adict['find_comma'] = find_comma
# 	find_successive_hyphens =re.findall(pattern_successive_hyphens,entry)
# 	adict['find_successive_hyphens'] = find_successive_hyphens
# 	find_pattern_phone_parantheses = re.findall(patten_phone_parantheses,entry)
# 	adict['find_pattern_phone_parantheses'] = find_pattern_phone_parantheses
# 	find_slash = re.findall(pattern_slash,entry)
# 	adict['find_slash'] = find_slash
# 	find_small = re.findall(pattern_small,entry)
# 	adict['find_small'] = find_small
# 	find_zipcode_one_hyphen=re.findall(pattern_zipcode_one_hyphen,entry)
# 	adict['find_zipcode_one_hyphen'] = find_zipcode_one_hyphen
# 	find_zipcode_without_hyphen= re.findall(pattern_zipcode_without_hyphen,entry)
# 	adict['find_zipcode_without_hyphen'] = find_zipcode_without_hyphen
# 	find_zipcode_two_hyphen=re.findall(pattern_zipcode_two_hyphen,entry)
# 	adict['find_zipcode_two_hyphen'] = find_zipcode_two_hyphen
# 	find_zipcode_four_digits=re.findall(patter_zipcode_four_digits,entry)
# 	adict['find_zipcode_four_digits'] = find_zipcode_four_digits
# 	find_special_characters=re.findall(pattern_special_characters,entry)
# 	adict['find_special_characters'] = find_special_characters 
# 	find_special_characters_phone=re.findall(pattern_special_characters_phone,entry)
# 	adict['find_special_characters_phone'] = find_special_characters_phone
# 	find_special_characters_website=re.findall(pattern_special_characters_website,entry)
# 	adict['find_special_characters_website'] = find_special_characters_website
# 	find_open_parantheses=re.findall(pattern_open_parantheses,entry)
# 	adict['find_open_parantheses'] = find_open_parantheses
# 	find_close_paranthses=re.findall(pattern_close_parantheses,entry)
# 	adict['find_close_paranthses'] = find_close_paranthses 
# 	find_at_the_rate=re.findall(pattern_at_the_rate,entry)
# 	adict['find_at_the_rate'] = find_at_the_rate
# 	find_uppercase = re.findall(pattern_uppercase,entry)
# 	adict['find_uppercase'] = find_uppercase
# 	find_lowercase = re.findall(pattern_lowercase,entry)
# 	adict['find_lowercase'] = find_lowercase

# 	return adict

# # class firstclass():
# def purestring(entry):
# 	firstobject(entry)
# 	print "adict is",adict
# 	if (adict['find_string']):
# 		print "The given entry ",adict['find_string'] , "contains string"
# 		return "string entry"
# 	c = purestring(b)

# def nocomma(entry):
# 	if (adict['find_comma']):
# 		return "comma is present"
# 	else :
# 		return "comman not present"
# 		pass
# 	d = nocomma(b)
# 	print "d is",d

# # b = firstobject('rajkumar')
# c = purestring('rajkumar')
# # d = nocomma(b)
# if c :
# 	print c
# if d :
# 	print d



from Classifier import *
from Calculator import *
from DisplayerIII import *
from trigger import *
from starter import *
import csv,unittest
bdict={}
bdict[' valid_verified_zipcode_without_hyphen']=bdict['valid_verified_zipcode_with_two_hyphen']=bdict['zipcode_with_two_not_successive_hyphens']=bdict['valid_verified_zipcode_with_one_hyphen']=bdict['mostly_zipcode_with_one_hyphen']=bdict['mostly_zipcode_without_hyphen']=bdict['mostly_zipcode_with_two_hyphen']=bdict['mostly_zipcode_four_digits']=bdict['phone_no_two_hyphens']=bdict['phone_no_without_hyphen_or_alphabets']=bdict['phone_no_with_alphabets']=bdict['phone_no_with_parantheses']=bdict['phone_no_one_hyphen']=bdict['phone_no_with_only_open_parantheses']=bdict['phone_no_with_only_close_parantheses']=bdict['phone_three_parts_two_hyphens']=bdict['phone_three_parts_one_hyphen_one_parantheses']=bdict['phone_three_parts_plus_one']=bdict['phone_10_digits']=bdict['phone_no_two_hyphens']=bdict['phone_no_without_hyphen_or_alphabets']=bdict['phone_no_with_parantheses']=bdict['phone_no_one_hyphen']=bdict['phone_no_with_only_open_parantheses']=bdict['phone_no_with_only_close_parantheses']=bdict['string_with_space_no_integer']=bdict['string_with_integer_spaces']=bdict['pure_uppercase_string']=bdict['string_with_integer_hyphen']=bdict['string_without_integer_without_spaces']=bdict['string_with_symbol_instead_of_at']=bdict['two_letter_uppercase_string_not_state_code']=bdict['string_first_line_address']=bdict['string_with_dots_not_email_not_website']=bdict['two_letter_lowercase_string_not_state_code']=bdict['string_with_integer_without_spaces']=bdict['website']=bdict['website_without_www']=bdict['string_without_integer_without_spaces']=bdict['string_with_space_no_integer']=bdict['pure_uppercase_string']=bdict['two_letter_uppercase_string_not_state_code']=bdict['email_without_integer']=bdict['state_code']=bdict['string_with_special_characters']=bdict['integer_with_special_characters']=bdict['email_with_integer']=bdict['email_without_integer']=bdict['decimal_integer'] = bdict['integer_with_at'] = bdict['pure_integer'] = 0
bdictReturn = {'string_with_symbol_instead_of_at': 0, 'integer_with_special_characters': 0, 'phone_10_digits': 0, 'valid_verified_zipcode_with_two_hyphen': 0, 'string_with_dots_not_email_not_website': 0, 'pure_integer': 0, 'phone_three_parts_plus_one': 0, 'phone_no_one_hyphen': 0, 'two_letter_uppercase_string_not_state_code': 0, 'mostly_zipcode_with_two_hyphen': 0, 'phone_no_with_parantheses': 0, 'phone_three_parts_two_hyphens': 0, 'string_with_special_characters': 0, ' valid_verified_zipcode_without_hyphen': 0, 'phone_no_with_alphabets': 0, 'email_with_integer': 0, 'decimal_integer': 0, 'zipcode_with_two_not_successive_hyphens': 0, 'website': 0, 'phone_no_with_only_open_parantheses': 0, 'mostly_zipcode_with_one_hyphen': 0, 'string_with_integer_without_spaces': 0, 'string_without_integer_without_spaces': 0, 'pure_uppercase_string': 0, 'phone_no_with_only_close_parantheses': 0, 'mostly_zipcode_without_hyphen': 0, 'valid_verified_zipcode_with_one_hyphen': 0, 'two_letter_lowercase_string_not_state_code': 0, 'phone_three_parts_one_hyphen_one_parantheses': 0, 'state_code': 0, 'integer_with_at': 0, 'string_first_line_address': 0, 'string_with_space_no_integer': 0, 'mostly_zipcode_four_digits': 0, 'string_with_integer_hyphen': 0, 'email_without_integer': 0, 'string_with_integer_spaces': 0, 'website_without_www': 0, 'phone_no_two_hyphens': 0, 'phone_no_without_hyphen_or_alphabets': 0}

datum  = get_real_data('test.csv')

class TestFunctions(unittest.TestCase):
	
	def test_website(self):
		regular_expressions("www.rajkumar.com")
		self.assertEqual(websiteFunction("www.rajkumar.com",bdict),'possible website')
		regular_expressions("www.rr.com")
		self.assertEqual(websiteFunction("www.rr.com",bdict),'possible website')
		regular_expressions("www.r.com")
		self.assertEqual(websiteFunction("www.r.com",bdict),'single character domain name')
		regular_expressions("http://www.rajkumar.com")
		self.assertEqual(websiteFunction("http://www.rajkumar.com",bdict),'possible website with http and slash')
		regular_expressions("rajkumar.co.in")
		self.assertEqual(websiteWithoutWWWFunction("rajkumar.co.in",bdict),'possible website but without www (2 dot) and without slashes')
		regular_expressions("rajkumar.com")
		self.assertEqual(websiteWithoutWWWFunction("rajkumar.com",bdict),'possible website but without www (1 dot)')
		regular_expressions("raj.k.mar")
		self.assertEqual(websiteWithoutWWWFunction("raj.k.mar",bdict),'string with more than one dot but not website')		

	def test_email(self):
		regular_expressions("raj49@gmail.com")
		self.assertEqual(emailFunction("raj49@gmail.com",[],bdict),['raj49@gmail.com'])
		regular_expressions("raj@gmail.com")
		self.assertEqual(emailFunction("raj@gmail.com",[],bdict),['raj@gmail.com'])
		regular_expressions("rajgmail.com")
		self.assertEqual(emailFunction("rajgmail.com",[],bdict),[])
		regular_expressions("raj@@gmail.com")
		self.assertEqual(emailFunction("raj@@gmail.com",[],bdict),['multiple @'])
	
	def test_string(self):
		regular_expressions("rajkumar")
		self.assertEqual(purestringFunction("rajkumar",bdict),'string without integer and without spaces')
		regular_expressions("rAjkumar")
		self.assertEqual(purestringFunction("Rajkumar",bdict),'string with single caps with no integer or spaces')
		regular_expressions("R")
		self.assertEqual(purestringFunction("R",bdict),'string of unit length with single caps')
		regular_expressions("RAJKUMAR")
		self.assertEqual(purestringFunction("RAJKUMAR",bdict),'pure uppercase string with more than 2 characters')
		regular_expressions("rAjkuMar")
		self.assertEqual(purestringFunction("rAjkuMar",bdict),'string with capital letters but not state code nor pure uppercase')
		regular_expressions("Raj.kumar")
		self.assertEqual(stringFunction("Raj.kumar",bdict),'string with dot but not email')
		regular_expressions("raj.kumar")
		self.assertEqual(stringFunction("raj.kumar",bdict),'string with dot but not email')  #full lowercase
		regular_expressions("Raj@kumar")
		self.assertEqual(stringFunction("Raj@kumar",bdict),'string with @ instead of at')
		regular_expressions("raj@kumar")
		self.assertEqual(stringFunction("raj@kumar",bdict),'string with @ instead of at')  #full lowercase
		regular_expressions("M S Dhoni")
		self.assertEqual(pureStringWithSpacesFunction("M S Dhoni",bdict),'string with spaces but no integer')
		regular_expressions("raj kumar")
		self.assertEqual(pureStringWithSpacesFunction("raj kumar",bdict),'a pure string with spaces')
		regular_expressions("RAJ KUMAR")
		self.assertEqual(pureStringWithSpacesFunction("RAJ KUMAR",bdict),'a pure string with spaces')
		regular_expressions("Raj/kumar")
		self.assertEqual(stringWithSpecialCharactersFunction("Raj/kumar",bdict),'string with special characters')
		regular_expressions("Raj[kumar")
		self.assertEqual(stringWithSpecialCharactersFunction("Raj[kumar",bdict),'string with special characters')
		regular_expressions("Raj!kumar")
		self.assertEqual(stringWithSpecialCharactersFunction("Raj!kumar",bdict),'string with special characters')
		regular_expressions("Raj$kumar")
		self.assertEqual(stringWithSpecialCharactersFunction("Raj$kumar",bdict),'string with special characters')
		regular_expressions("Raj_kumar")
		self.assertEqual(stringWithSpecialCharactersFunction("Raj_kumar",bdict),'string with special characters')
		regular_expressions("Raj\kumar")
		self.assertEqual(stringWithSpecialCharactersFunction("Raj\kumar",bdict),'string with special characters')
		regular_expressions("Raj=kumar")
		self.assertEqual(stringWithSpecialCharactersFunction("Raj=kumar",bdict),'string with special characters')
		regular_expressions("Raj:kumar")
		self.assertEqual(stringWithSpecialCharactersFunction("Raj:kumar",bdict),'string with special characters')
		regular_expressions("Raj*kumar")
		self.assertEqual(stringWithSpecialCharactersFunction("Raj*kumar",bdict),'string with special characters')
		regular_expressions("Raj~kumar")
		self.assertEqual(stringWithSpecialCharactersFunction("Raj~kumar",bdict),'string with special characters')
		regular_expressions("Raj?kumar")
		self.assertEqual(stringWithSpecialCharactersFunction("Raj?kumar",bdict),'string with special characters')
		regular_expressions("Raj<kumar")
		self.assertEqual(stringWithSpecialCharactersFunction("Raj<kumar",bdict),'string with special characters')
		regular_expressions("Raj^kumar")
		self.assertEqual(stringWithSpecialCharactersFunction("Raj^kumar",bdict),'string with special characters')
		regular_expressions("Raj%kumar")
		self.assertEqual(stringWithSpecialCharactersFunction("Raj%kumar",bdict),'string with special characters')

	def test_phone(self):
		regular_expressions("1800-AMY-4567")
		self.assertEqual(phoneFunction("1800-AMY-4567",bdict),'possible phone no but with alphabets')
		regular_expressions("180/458-4567")
		self.assertEqual(phoneFunction("180/458-4567",bdict),'possible phone no but with slash instead of one of the hyphens')
		regular_expressions("180-874/4567")
		self.assertEqual(phoneFunction("180-874/4567",bdict),'possible phone no but with slash instead of one of the hyphens')
		regular_expressions("1800-874/4567")
		self.assertEqual(phoneFunction("1800-874/4567",bdict),'not phone no because more than ten integers with slash instead of one of the hyphens')
		regular_expressions("1800/874-4567")
		self.assertEqual(phoneFunction("1800/874-4567",bdict),'not phone no because more than ten integers with slash instead of one of the hyphens')
		regular_expressions("1800-125-4567")
		self.assertEqual(phoneFunction("1800-125-4567",bdict),'more than 10 integers and thus not a phone no')
		regular_expressions("(180)1254567")
		self.assertEqual(phoneFunction("(180)1254567",bdict),'phone no with parantheses')
		regular_expressions("180-254-5607")
		self.assertEqual(phoneFunction("180-254-5607",bdict),'phone with two hyphens')
		regular_expressions("(180) 254-5607")
		self.assertEqual(phoneFunction("(180) 254-5607",bdict),'phone no with three parts with one hyphen and a parantheseses')
		regular_expressions("(180 254-5607")
		self.assertEqual(phoneFunction("(180 254-5607",bdict),'phone no with only open parantheses')
		regular_expressions("180) 254-5607")
		self.assertEqual(phoneFunction("180) 254-5607",bdict),'phone no with only close parantheses')
		regular_expressions("180/874-467")
		self.assertEqual(phoneFunction("180/874-467",bdict),'not phone no because of less than ten integers but with slash instead of one of the hyphens')
		regular_expressions("180-874/567")
		self.assertEqual(phoneFunction("180-874/567",bdict),'not phone no because of less than ten integers but with slash instead of one of the hyphens')

	def test_zipcode(self):
		regular_expressions("83025-4567")
		self.assertEqual(zipcodeFunction("83025-4567",bdict),'Most probably a zipcode with one hyphen')
		regular_expressions("82999-4567")
		self.assertEqual(zipcodeFunction("82999-4567",bdict),'has one hyphen but is not a zipcode')
		regular_expressions("83025--4567")
		self.assertEqual(zipcodeFunction("83025--4567",bdict),'Most probably a zipcode with two hyphen')
		regular_expressions("82999--4567")
		self.assertEqual(zipcodeFunction("82999--4567",bdict),'has two hyphen but is not a zipcode')
		regular_expressions("83025-456-7")
		self.assertEqual(zipcodeFunction("83025-456-7",bdict),'possible zip codes but with two but not succesive hyphens')
		regular_expressions("82999-456-7")
		self.assertEqual(zipcodeFunction("82999-456-7",bdict),'integer with two hyphens but not zipcode or phone')
		regular_expressions("829-456-7")
		self.assertEqual(zipcodeFunction("829-456-7",bdict),'integers separated by hyphen but not zipcode or phone number')

	def test_integer(self):
		regular_expressions("raj567kumar")
		self.assertEqual(integerFunction("raj567kumar",bdict),'string with integer without spaces')
		regular_expressions("raj 567kumar")
		self.assertEqual(integerFunction("raj 567kumar",bdict),'string with integer and spaces')
		regular_expressions("raj- 567kumar")
		self.assertEqual(integerFunction("raj- 567kumar",bdict),'Mixture of string integer and hyphen and spaces')
		regular_expressions("raj-567kumar")
		self.assertEqual(integerFunction("raj-567kumar",bdict),'Mixture of string integer and hyphen but not spaces')
		regular_expressions("83025")
		self.assertEqual(integerFunction("83025",bdict),'most probably a zipcode (without hyphen)')		
		regular_expressions("6404")
		self.assertEqual(integerFunction("6404",bdict),'most probably a zipcode (four digits)')
		regular_expressions("82999")
		self.assertEqual(integerFunction("82999",bdict),'not a Zipcode')
		regular_expressions("9854")
		self.assertEqual(integerFunction("9854",bdict),'a four digit integer')
		regular_expressions("82.96")
		self.assertEqual(integerFunction("82.96",bdict),'Integer with decimals')
		regular_expressions("826")
		self.assertEqual(integerFunction("826",bdict),'Pure integer')
		regular_expressions("1234567890")
		self.assertEqual(integerFunction("1234567890",bdict),'10 digit phone no')
		regular_expressions("+1 123 456 7890")
		self.assertEqual(integerFunction("+1 123 456 7890",bdict),'phone with four parts containing three spaces and +1')
		regular_expressions("11234567890")
		self.assertEqual(integerFunction("11234567890",bdict),'11 digit phone no i.e starts with 1 followed by 10 digits')
		regular_expressions("21234567890")
		self.assertEqual(integerFunction("21234567890",bdict),'11 digit number but not phone no')
		regular_expressions("-526")
		self.assertEqual(integerFunction("-526",bdict),'Negative integer without decimals')
		regular_expressions("-526.20")
		self.assertEqual(integerFunction("-526.20",bdict),'Negative integer with decimals')
		regular_expressions("-526.")
		self.assertEqual(integerFunction("-526.",bdict),'decimal integer with misplaced dot')
		regular_expressions("26*20")
		self.assertEqual(integerFunction("26*20",bdict),'integer with special characters')
		regular_expressions("26/20")
		self.assertEqual(integerFunction("26/20",bdict),'integer with special characters')
		regular_expressions("26_20")
		self.assertEqual(integerFunction("26_20",bdict),'integer with special characters')
		regular_expressions("26?20")
		self.assertEqual(integerFunction("26?20",bdict),'integer with special characters')
		regular_expressions("-26*20")
		self.assertEqual(integerFunction("-26*20",bdict),'Negative integer with special characters')
		regular_expressions("-26^20")
		self.assertEqual(integerFunction("-26^20",bdict),'Negative integer with special characters')
		regular_expressions("-26<20")
		self.assertEqual(integerFunction("-26<20",bdict),'Negative integer with special characters')
		regular_expressions("-26~20")
		self.assertEqual(integerFunction("-26~20",bdict),'Negative integer with special characters')
		regular_expressions("26@20")
		self.assertEqual(integerFunction("26@20",bdict),'integer with @')

	def test_statecode(self):
		regular_expressions("PA")
		self.assertEqual(stateCodeFunction("PA",bdict),'possible state code')
		regular_expressions("AB")
		self.assertEqual(stateCodeFunction("AB",bdict),'two lettered uppercase string not state code')
		regular_expressions("pa")
		self.assertEqual(stateCodeFunction("pa",bdict),'possible state code in lowercase')
		regular_expressions("ab")
		self.assertEqual(stateCodeFunction("ab",bdict),'two lettered lowercase string not state code')
		regular_expressions("ALASKA")
		self.assertEqual(stateCodeFunction("ALASKA",bdict),'possible state name in capital letters')
		regular_expressions("alaska")
		self.assertEqual(stateCodeFunction("alaska",bdict),'possible state name in lowercase')
		regular_expressions("tamilnadu")
		self.assertEqual(stateCodeFunction("tamilnadu",bdict),'not state name')
		regular_expressions("INDIA")
		self.assertEqual(stateCodeFunction("INDIA",bdict),'uppercase string')

	def test_empty(self):
		regular_expressions("")
		self.assertEqual(emptyFunction("",bdict),"empty")
		regular_expressions(" ")
		self.assertEqual(emptyFunction(" ",bdict),"empty")

	def test_print_functions(self):
		# print "datum is",datum
		self.assertEqual(print_uppercase_entries('test.csv',1,2,datum,[]),[1,0,0,0,0,0,0,0,0,0])
		self.assertEqual(print_empty_entries('test.csv',2,3,datum,[]),[1,0,0])
		self.assertEqual(print_string_entries('test.csv',1,2,datum,[]),[1,0,0,0,0,0,0,0,0,0])		
		self.assertEqual(print_string_only_entries('test.csv',1,2,datum,[]),[1,0,0,0,0,0,0,0,0])
		self.assertEqual(print_string_with_integer_and_space_entries('test.csv',1,2,datum,[]),[])
		self.assertEqual(print_integer_entries('test.csv',4,5,datum,[]),[1,0])
		self.assertEqual(print_integer_only_entries('test.csv',0,1,datum,[]),[1,0,0,0,0,0,0,0,0])
		# self.assertEqual(print_improper_decimal_integers('test.csv',5,6,datum,[]),[1])
		self.assertEqual(improper_integer_entries('test.csv',0,1,datum,[]),[1])
		self.assertEqual(print_email_entries('test.csv',3,4,datum,[]),[1,0,0,0,0,0,0,0])
		self.assertEqual(print_website_entries('test.csv',1,2,datum,[]),[])
		self.assertEqual(print_special_characters('test.csv',1,2,datum,[]),[1])
		self.assertEqual(print_special_characters_phone('test.csv',1,2,datum,[]),[1])
		self.assertEqual(print_special_characters_website('test.csv',1,2,datum,[]),[1])
		self.assertEqual(print_hyphen ('test.csv',0,1,datum,[]),[1])
		self.assertEqual(print_space_entries ('test.csv',2,3,datum,[]),[1])
		self.assertEqual(print_no_dots('test.csv',5,6,datum,[]),[])
		self.assertEqual(print_pure_integer_not_zipcode('test.csv',0,1,datum,[]),[1,0,0,0,0,0,0,0])
		self.assertEqual(print_integer_more_than_string('test.csv',1,2,datum,[]),[])
		self.assertEqual(print_string_more_than_integer('test.csv',3,4,datum,[]),[1,0,0,0,0,0,0,0,0,0])
		self.assertEqual(print_not_state_code('test.csv',1,2,datum,[]),[1,0,0,0,0,0,0,0,0,0])
		self.assertEqual(print_symbols('test.csv',1,2,datum,[]),[1])
		self.assertEqual(print_decimal_values('test.csv',5,6,datum,[]),[1,0,0,0,0,0,0,0,0,0])
		self.assertEqual(print_state_code('test.csv',1,2,datum,[]),[])
		self.assertEqual(print_state_code_lowercase ('test.csv',1,2,datum,[]),[])
		# self.assertEqual(print_zip_code('test.csv',0,1,datum,[]),[1])		
		self.assertEqual(print_email_with_more_than_one_at('test.csv',3,4,datum,[]),[1])
		self.assertEqual(print_email_with_space('test.csv',3,4,datum,[]),[1])
		self.assertEqual(print_email_without_dot('test.csv',3,4,datum,[]),[1])
		self.assertEqual(print_string_without_email('test.csv',1,2,datum,[]),[1,0,0,0,0,0,0,0,0,0])
		self.assertEqual(print_string_with_dots_not_email_not_website('test.csv',2,3,datum,[]),[1])
	
	def test_startTool(self):
		self.assertEqual(startTool('test.csv',0,1,11,11),"return from startTool")

	# def test_observations(self):
	# 	self.assertEqual(observations('test.csv',2,3,23,datum,bdictReturn,[]),"return from observation function")
	#The function "observations" can't be tested seperately cos it depends on inputs from startool. Hence when, startool is tested successfully it is implied that observations also works.

	def test_work_header(self):
		self.assertEqual(work_header('test.csv','email'),"return from work_header")

	def test_sample_header(self):
		self.assertEqual(sample_header('test.csv','id'),"return from sample_header function")

	def test_count_rows(self):
		self.assertEqual(count_rows('test.csv'),11)

	def test_ten_rows(self):
		self.assertEqual(ten_rows('test.csv'),"return from ten_rows")

	def test_printHeader(self):
		self.assertEqual(printHeader('test.csv'),"inside printHeader function")

	def test_whole_file(self):
		self.assertEqual(whole_file('test.csv'),"return from whole_file")

if __name__ == '__main__' :
	unittest.main(exit=False)	

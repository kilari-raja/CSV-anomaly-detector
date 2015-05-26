#!/usr/bin/env python

import re,csv,sys,requests,compago
from collections import Counter
app = compago.Application()
# class testclass(object):
# 	def printNumber(self,number):
# 		print "Print number",number
# 		class printAgain(object):
# 			print "Inside class",number

# instance = testclass()
# instance.printNumber(2)

two_letter_lowercase_string_not_state_code = string_with_integer_spaces = email = website = string_with_space_no_integer = phone_no_with_alphabets = website_without_www = state_code = pure_uppercase_string = phone_no_two_hyphens = phone_no_with_parantheses = phone_no_without_hyphen_or_alphabets = valid_verified_zipcode_without_hyphen = empty = valid_verified_zipcode_with_two_hyphen = string_with_integer_without_spaces = pure_integer =  valid_verified_zipcode_with_one_hyphen = two_letter_uppercase_string_not_state_code = zipcode_with_two_not_successive_hyphens = string_without_integer_without_spaces = string_with_symbol_instead_of_at = string_first_line_address = integer_seperated_by_hyphen_not_zip_or_phone =  phone_no_one_hyphen = phone_no_with_only_open_parantheses = phone_no_with_only_close_parantheses = uncertain_entries = string_with_dots_not_email_not_website = mostly_zipcode_with_one_hyphen = mostly_zipcode_without_hyphen = mostly_zipcode_with_two_hyphen = mostly_zipcode_four_digits = requests_made = decimal_integer = string_with_integer_hyphen = string_with_special_characters = integer_with_special_characters = email_with_integer = email_without_integer = print_empty_count = string_dots_no_email_or_website = special_characters_print =email_dominant_column= phone_three_parts_two_hyphens= phone_three_parts_one_hyphen_one_parantheses=phone_three_parts_plus_one=phone_11_digits=phone_10_digits=row_count=0

states = [ "AK","Alaska","AL","Alabama","AR","Arkansas","AS","American Samoa","AZ","Arizona","CA","California","CO","Colorado","CT","Connecticut","DC","District of Columbia","DE","Delaware","FL","Florida","GA","Georgia","GU","Guam","HI","Hawaii","IA","Iowa","ID","Idaho","IL","Illinois","IN","Indiana","KS","Kansas","KY","Kentucky","LA","Louisiana","MA","Massachusetts","MD","Maryland","ME","Maine","MI","Michigan","MN","Minnesota","MO","Missouri","MS","Mississippi","MT","Montana","NC","North Carolina","ND","North Dakota","NE","Nebraska","NH","New Hampshire","NJ","New Jersey","NM","New Mexico","NV","Nevada","NY","New York","OH","Ohio","OK","Oklahoma","OR","Oregon","PA","Pennsylvania","PR","Puerto Rico","RI","Rhode Island","SC","South Carolina","SD","South Dakota","TN","Tennessee","TX","Texas","UT","Utah","VA","Virginia","VI","Virgin Islands","VT","Vermont","WA","Washington","WI","Wisconsin","WV","West Virginia","WY","Wyoming" ]		
state_code_array = ["AK","AL","AR","AS","AZ","CA","CO","CT","DC","DE","FL","GA","GU","HI","IA","ID","IL","IN","KS","KY","LA","MA","MD","ME","MI","MN","MO","MS","MT","NC","ND","NE","NH","NJ","NM","NV","NY","OH","OK","OR","PA","PR","RI","SC","SD","TN","TX","UT","VA","VI","VT","WA","WI","WV","WY"]
states_and_cities = ["Wyoming","Minnesota","California","Georgia","Kansas","Vermont","Indiana","Pennsylvania","Alabama","New York","Florida","Ohio","Texas","Maryland","Louisiana","Missouri","WY","MN","CA","GA","KS","VT","IN","PA","AL","NY","FL","OH","TX","MD","LA"]
lower_states = []
upper_states = []
decimal_integer_lengths=[]
counter_decimal_integer = Counter(decimal_integer_lengths)
else_count = 0
func_count = 0
local_count = 0
for t in range(0,len(states)-1):
	lower_states.append(states[t].lower())
for t in range(0,len(states)-1):
	upper_states.append(states[t].upper())

count = 0
counter = 0

arr=[]
zipcode_array =[]
email_array = []

globvar = 0
globar = 1

purestring = pureStringWithSpaces = 0
adict={}

pattern_string = re.compile("[a-zA-Z]")
pattern_caps = re.compile("[A-Z]")
pattern_small = re.compile("[a-z]")
pattern_integer = re.compile("[0-9]")
pattern_email = re.compile("[\w+|\W+]@[\w+|\W+]")
pattern_phone = re.compile("-")
pattern_phone_three_parts_two_hyphens=re.compile("\d{3}-\d{3}-\d{4}")
pattern_phone_three_parts_one_hyphen_one_parantheses=re.compile("\(\d{3}\) \d{3}-\d{4}")
pattern_phone_three_parts_plus_one=re.compile("\+1 \d{3} \d{3} \d{4}")
pattern_phone_11_digits=re.compile("\d{11}")
pattern_phone_10_digits=re.compile("\d{10}")
pattern_empty = re.compile("^\s*$")
pattern_no_entry = re.compile("^(?![\s\S])")
pattern_website = re.compile("www+|WWW+")
pattern_dot = re.compile("[.]")
pattern_word_after_dot = re.compile("[.][a-zA-Z]")
pattern_http = re.compile("http")
pattern_space = re.compile("[\w+|\W+]\s[\w+|\W+]")
pattern_hashtag = re.compile("#")
pattern_comma = re.compile(",")
pattern_successive_hyphens = re.compile("--")
patten_phone_parantheses = re.compile("\(\d+\)|\(\d+|\d+\)|\d+\(\d+\)")
pattern_slash = re.compile("[\w+|\W+]/[\w+|\W+]")
pattern_zipcode_one_hyphen = re.compile('^\d{5}-\d{4}$')
pattern_zipcode_without_hyphen = re.compile('^\d{5}$')
patter_zipcode_four_digits = re.compile('^\d{4}$')
pattern_zipcode_two_hyphen = re.compile('^\d{5}--\d{4}$')
pattern_special_characters = re.compile("[!|$|\\\\|/|%|^|+|=|_|*|}|~|\[|\]|:|?|`|<|>|{]")
pattern_special_characters_website = re.compile("[\\\\|%|^|\||}|`|<|>|{]")
pattern_special_characters_phone = re.compile("[!|$|\\\\|/|%|^|=|_|*|}|~|\[|\]|:|?|`|<|>|{]")
pattern_open_parantheses =  re.compile("[()]")
pattern_close_parantheses = re.compile("[)]")
pattern_at_the_rate = re.compile("@")
pattern_uppercase = re.compile("[A-Z]")
pattern_lowercase = re.compile("[a-z]")
pattern_decimal = re.compile("\d\.\d")


def regular_expressions(entry):
	find_string = re.findall(pattern_string,entry)
	adict['find_string'] = find_string
	find_integer = re.findall(pattern_integer,entry)
	adict['find_integer'] = find_integer
	find_email = re.findall(pattern_email,entry)
	adict['find_email'] = find_email
	find_phone = re.findall(pattern_phone,entry)
	adict['find_phone'] = find_phone
	find_phone_three_parts_two_hyphens = re.findall(pattern_phone_three_parts_two_hyphens,entry)
	adict['find_phone_three_parts_two_hyphens'] = find_phone_three_parts_two_hyphens
	find_phone_three_parts_one_hyphen_one_parantheses = re.findall(pattern_phone_three_parts_one_hyphen_one_parantheses,entry)
	adict['find_phone_three_parts_one_hyphen_one_parantheses'] = find_phone_three_parts_one_hyphen_one_parantheses
	find_pattern_phone_three_parts_plus_one=re.findall(pattern_phone_three_parts_plus_one,entry)
	adict['find_pattern_phone_three_parts_plus_one'] = find_pattern_phone_three_parts_plus_one
	find_pattern_phone_11_digits = re.findall(pattern_phone_11_digits,entry)
	adict['find_pattern_phone_11_digits'] = find_pattern_phone_11_digits
	find_pattern_phone_10_digits = re.findall(pattern_phone_10_digits,entry)
	adict['find_pattern_phone_10_digits'] = find_pattern_phone_10_digits
	find_empty = re.findall(pattern_empty,entry)
	adict['find_empty'] = find_empty
	find_no_entry = re.findall(pattern_no_entry,entry)						
	adict['find_no_entry'] = find_no_entry 
	find_website = re.findall(pattern_website,entry)
	adict['find_website'] = find_website
	find_dot = re.findall(pattern_dot,entry)
	adict['find_dot'] = find_dot
	find_http = re.findall(pattern_http,entry)
	adict['find_http'] = find_http
	find_space = re.findall(pattern_space,entry)
	adict['find_space'] = find_space
	find_caps = re.findall(pattern_caps,entry)
	adict['find_caps'] =find_caps 
	find_word_after_dot = re.findall(pattern_word_after_dot,entry)
	adict['find_word_after_dot'] = find_word_after_dot
	find_hashtag = re.findall(pattern_hashtag,entry)
	adict['find_hashtag'] = find_hashtag
	find_comma = re.findall(pattern_comma,entry)
	adict['find_comma'] = find_comma
	find_successive_hyphens =re.findall(pattern_successive_hyphens,entry)
	adict['find_successive_hyphens'] = find_successive_hyphens
	find_pattern_phone_parantheses = re.findall(patten_phone_parantheses,entry)
	adict['find_pattern_phone_parantheses'] = find_pattern_phone_parantheses
	find_slash = re.findall(pattern_slash,entry)
	adict['find_slash'] = find_slash
	find_small = re.findall(pattern_small,entry)
	adict['find_small'] = find_small
	find_zipcode_one_hyphen=re.findall(pattern_zipcode_one_hyphen,entry)
	adict['find_zipcode_one_hyphen'] = find_zipcode_one_hyphen
	find_zipcode_without_hyphen= re.findall(pattern_zipcode_without_hyphen,entry)
	adict['find_zipcode_without_hyphen'] = find_zipcode_without_hyphen
	find_zipcode_two_hyphen=re.findall(pattern_zipcode_two_hyphen,entry)
	adict['find_zipcode_two_hyphen'] = find_zipcode_two_hyphen
	find_zipcode_four_digits=re.findall(patter_zipcode_four_digits,entry)
	adict['find_zipcode_four_digits'] = find_zipcode_four_digits
	find_special_characters=re.findall(pattern_special_characters,entry)
	adict['find_special_characters'] = find_special_characters 
	find_special_characters_phone=re.findall(pattern_special_characters_phone,entry)
	adict['find_special_characters_phone'] = find_special_characters_phone
	find_special_characters_website=re.findall(pattern_special_characters_website,entry)
	adict['find_special_characters_website'] = find_special_characters_website
	find_open_parantheses=re.findall(pattern_open_parantheses,entry)
	adict['find_open_parantheses'] = find_open_parantheses
	find_close_paranthses=re.findall(pattern_close_parantheses,entry)
	adict['find_close_paranthses'] = find_close_paranthses 
	find_at_the_rate=re.findall(pattern_at_the_rate,entry)
	adict['find_at_the_rate'] = find_at_the_rate
	find_uppercase = re.findall(pattern_uppercase,entry)
	adict['find_uppercase'] = find_uppercase
	find_lowercase = re.findall(pattern_lowercase,entry)
	adict['find_lowercase'] = find_lowercase
	find_decimal=re.findall(pattern_decimal,entry)
	adict['find_decimal'] = find_decimal

	return adict

def purestringFunction(entry):
	regular_expressions(entry)
	if adict['find_string'] and not adict['find_integer'] and not adict['find_empty'] and not adict['find_no_entry'] and not adict['find_email'] and not adict['find_http'] and not adict['find_dot'] and not adict['find_caps'] and adict['find_string'] not in lower_states and adict['find_string'] not in upper_states :		
		global string_without_integer_without_spaces
		string_without_integer_without_spaces+=1
		return "is string without integer and without spaces"

	elif len(adict['find_caps']) == 1 and not adict['find_integer'] and not adict['find_empty'] and not adict['find_no_entry'] and not adict['find_dot'] and not adict['find_slash'] and len(adict['find_string']) > 1:		
		# global string_without_integer_without_spaces
		string_without_integer_without_spaces += 1	
		return "is string with single caps with no integer or spaces"

	elif len(adict['find_caps']) == 1 and not adict['find_integer'] and not adict['find_empty'] and not adict['find_no_entry'] and not adict['find_dot'] and not adict['find_slash'] and len(adict['find_string']) == 1:		
		# global string_without_integer_without_spaces
		string_without_integer_without_spaces += 1
		return "is string of unit length with single caps"

	elif len(adict['find_string']) > 2 and len(adict['find_caps']) == len(adict['find_string']) and not adict['find_integer'] and not adict['find_empty'] and not adict['find_no_entry'] and not adict['find_dot'] and not adict['find_slash']:		
		global pure_uppercase_string
		pure_uppercase_string+=1
		return "is pure uppercase string with more than 2 characters"

	elif adict['find_caps'] and len(adict['find_caps']) != len(adict['find_string']) and not adict['find_integer'] and not adict['find_empty'] and not adict['find_no_entry'] and not adict['find_dot'] and not adict['find_slash'] and not adict['find_space']:
		# global string_without_integer_without_spaces
		string_without_integer_without_spaces += 1		
		return "is string with capital letters but not state code nor pure uppercase"

def stringFunction(entry) :
	regular_expressions(entry)
	if (adict['find_string'] and adict['find_integer'] and not adict['find_empty'] and not adict['find_http']  and not adict['find_no_entry'] and adict['find_dot'] and not adict['find_email']) or (adict['find_string'] and not adict['find_integer'] and not adict['find_empty'] and adict['find_dot'] and not adict['find_email'] and not adict['find_website'] and not adict['find_http']) :		
		global string_with_dots_not_email_not_website
		string_with_dots_not_email_not_website += 1
		return "is string with dot but not email"

	elif adict['find_string'] and adict['find_email'] and not adict['find_dot'] :		
		global string_with_symbol_instead_of_at
		string_with_symbol_instead_of_at+=1
		return "is string with @ instead of at"

	elif (len(adict['find_phone']) == 1 and len(adict['find_integer']) != 10 and not adict['find_string'] and adict['find_hashtag']) or (adict['find_string'] and adict['find_integer'] and len(adict['find_space']) > 1 and len(adict['find_string']) > len(adict['find_integer'])):		
		global string_first_line_address
		string_first_line_address += 1	
		return "is possible line1 of address"

def pureStringWithSpacesFunction(entry):
	regular_expressions(entry)
	if (adict['find_space']) and (len(adict['find_string']) + len(adict['find_space']) == len(entry)):		
		global pureStringWithSpaces
		pureStringWithSpaces+=1	
		return "is a pure string with spaces"

	elif adict['find_space'] and adict['find_string'] and not adict['find_integer'] :		
		global string_with_space_no_integer
		string_with_space_no_integer+=1	
		return "is string with spaces but no integer"

def stringWithSpecialCharactersFunction(entry):
	regular_expressions(entry)
	if (adict['find_string'] and adict['find_special_characters']) and (len(adict['find_string'])+ len(adict['find_special_characters']) == len(entry)):
		global string_with_special_characters
		string_with_special_characters+=1
		return "is string with special characters"

def websiteFunction(entry):
	regular_expressions(entry)
	if (adict['find_string'] and adict['find_http'] and adict['find_slash'] and adict['find_dot']) or (adict['find_string'] and adict['find_http'] and adict['find_slash'] and adict['find_dot'] and adict['find_integer']):		
		global website
		website+=1
		return "is possible website with http and slash"

	elif (adict['find_string'] and adict['find_website'] and adict['find_dot'] and adict['find_word_after_dot'] and not adict['find_space']) or (adict['find_string'] and adict['find_word_after_dot'] and adict['find_http'] and adict['find_dot'] and not adict['find_space'] and len(adict['find_dot']) > 1) :
		x = [j for j,val in enumerate(entry) if val=="."]
		if((x[len(x)-1]-x[0]) >= 3) :			
			# global website
			website+=1
			return "is possible website"
		else :
			return "single character domain name"
					
def websiteWithoutWWWFunction(entry):
	regular_expressions(entry)
	if adict['find_string'] and adict['find_dot'] and not adict['find_website'] and not adict['find_email'] and  adict['find_word_after_dot'] and not adict['find_slash'] and not adict['find_space'] and not adict['find_hashtag'] and not adict['find_comma'] and (len(adict['find_string']) > 5):								
		if len(adict['find_dot']) > 1 :
			x = [j for j,val in enumerate(entry) if val=="."]
			if((x[len(x)-1]-x[0]) >= 3) :
				global website_without_www
				website_without_www+=1
				return "is possible website but without www (2 dot) and without slashes"
			else :				
				#there can't be a single character domain name
				global string_with_dots_not_email_not_website
				string_with_dots_not_email_not_website+=1
				return "is string with more than one dot but not website"

		elif len(adict['find_dot']) <= 1 :
			x = [j for j,val in enumerate(entry) if val=="."]
			if(len(entry)-x[0] > 4):				
				# global string_with_dots_not_email_not_website
				string_with_dots_not_email_not_website+=1
				return "is string with one dot but one website"
			else :				
				# global website_without_www
				website_without_www+=1
				return "is possible website but without www (1 dot)"

		else :			
			# global website_without_www
			website_without_www+=1 
			return "is possible website but without www (1 dot) and without slashes"


	elif adict['find_string'] and adict['find_slash'] and adict['find_dot'] and not adict['find_website'] and adict['find_word_after_dot'] and not adict['find_space'] and not adict['find_hashtag'] and not adict['find_comma'] and (len(adict['find_string']) > 5):						
		x = [j for j,val in enumerate(entry) if val=="."]
		if((x[len(x)-1]-x[0]) >= 3) :
			return "is possible website but without www and with slashes"
			# global website_without_www
			website_without_www+=1

def emailFunction(entry):
	regular_expressions(entry)		
	if adict['find_string'] and adict['find_dot'] and adict['find_integer'] and adict['find_email'] and not adict['find_empty'] and not adict['find_no_entry']:		
		global email_with_integer
		email_with_integer+=1
		email_array.append(entry)
		return "is possible email with integer"
	elif adict['find_string'] and adict['find_email'] and adict['find_dot'] and not adict['find_empty'] and not adict['find_integer'] and not adict['find_no_entry']:		
		global email_without_integer
		email_without_integer+=1
		email_array.append(entry)	
		return "is possible email but without integer"

def phoneFunction(entry):
	regular_expressions(entry)
	# if len(adict['find_phone']) == 2 and len(adict['find_integer']) == 10 and not adict['find_successive_hyphens'] and len(adict['find_integer']) > len(adict['find_string']):
	# 		return "is possible phone no because of two hyphens"
	# 		phone_no_two_hyphens+=1	
	if adict['find_string'] and adict['find_phone'] and not adict['find_slash']  and adict['find_integer'] and not adict['find_dot'] and len(adict['find_integer']) >= 6 :								
		global phone_no_with_alphabets
		phone_no_with_alphabets+=1
		return "is possible phone no but with alphabets"

	if len(adict['find_phone']) == 1 and len(adict['find_integer']) == 10 and not adict['find_successive_hyphens'] and len(adict['find_integer']) > len(adict['find_string']) and adict['find_slash']:
			global phone_no_one_hyphen
			phone_no_one_hyphen+=1
			return "is possible phone no but with slash instead of one of the hyphens"

	if len(adict['find_phone']) == 1 and len(adict['find_integer']) < 10 and not adict['find_successive_hyphens'] and len(adict['find_integer']) > len(adict['find_string']) and adict['find_slash']:
			# global phone_no_one_hyphen
			# phone_no_one_hyphen+=1	
			return "not phone no because of less than ten integers but with slash instead of one of the hyphens"

	if len(adict['find_phone']) == 1 and len(adict['find_integer']) > 10 and not adict['find_successive_hyphens'] and len(adict['find_integer']) > len(adict['find_string']) and adict['find_slash']:			
			return "not phone no because more than ten integers with slash instead of one of the hyphens"
			# global phone_no_one_hyphen
			# phone_no_one_hyphen+=1											
		
	if len(adict['find_phone']) == 1 and len(adict['find_integer']) == 10 and not adict['find_string'] and not adict['find_hashtag'] and adict['find_pattern_phone_parantheses'] :
		if adict['find_phone_three_parts_one_hyphen_one_parantheses'] and not adict['find_string'] :			
			global phone_three_parts_one_hyphen_one_parantheses
			phone_three_parts_one_hyphen_one_parantheses +=1
			return "is phone no with three parts with one hyphen and a parantheseses"

		else :
			open_brace = [phone for phone,val in enumerate(entry) if val=="("]
			close_brace = [phone for phone,val in enumerate(entry) if val==")"]
			# if open_brace and close_brace :
			# 	return "is phone no with parantheses"					
			# 	phone_no_with_parantheses+=1
			if open_brace and not close_brace :				
				global phone_no_with_only_open_parantheses
				phone_no_with_only_open_parantheses+=1
				return "is phone no with only open parantheses"
			if close_brace and not open_brace :				
				global phone_no_with_only_close_parantheses
				phone_no_with_only_close_parantheses+=1
				return "is phone no with only close parantheses"

	if adict['find_pattern_phone_parantheses'] and not adict['find_website'] and not adict['find_string'] and len(adict['find_integer']) == 10 and not adict['find_pattern_phone_10_digits'] and not adict['find_phone_three_parts_two_hyphens'] and not adict['find_phone_three_parts_one_hyphen_one_parantheses'] and not adict['find_pattern_phone_three_parts_plus_one'] and not adict['find_pattern_phone_11_digits'] :		
		global phone_no_with_parantheses
		phone_no_with_parantheses+=1
		return "is phone no with parantheses"

	if adict['find_phone_three_parts_two_hyphens'] and not adict['find_string'] and len(adict['find_integer']) == 10 :		
		global phone_three_parts_two_hyphens
		phone_three_parts_two_hyphens+=1
		return  "is phone with two hyphens"

	if adict['find_phone_three_parts_two_hyphens'] and not adict['find_string'] and len(adict['find_integer']) >= 10 :
		return "more than 10 integers and thus not a phone no"

	# if adict['find_phone_three_parts_one_hyphen_one_parantheses'] and not adict['find_string'] :
	# 	return  "is phone with one hyphen and one parantheses"
	# 	phone_three_parts_one_hyphen_one_parantheses+=1

def zipcodeFunction(entry):
	regular_expressions(entry)

	if adict['find_integer'] :
		if adict['find_phone'] :
			if(adict['find_zipcode_one_hyphen']):
				c = entry.split("-")
				if c[0] in zipcodes :					
					# zipcode_array.append(entry)
					global mostly_zipcode_with_one_hyphen
					mostly_zipcode_with_one_hyphen += 1	
					return  "is Most probably a zipcode with one hyphen"
				else :					
					global pure_integer
					pure_integer += 1
					return  "has one hyphen but is not a zipcode"

			if(adict['find_zipcode_two_hyphen']) :
				c = entry.split("--")
				if c[0] in zipcodes :					
					global mostly_zipcode_with_two_hyphen
					mostly_zipcode_with_two_hyphen += 1
					return  "is Most probably a zipcode with two hyphen"
				else :					
					# global pure_integer
					pure_integer += 1
					return  "has two hyphen but is not a zipcode"

	if len(adict['find_phone']) == 2 and len(adict['find_integer']) != 10 and not adict['find_successive_hyphens'] and not adict['find_string'] :
		y = entry.split("-")
		if(len(y[0])>3):			
			if y[0] in zipcodes :
				global zipcode_with_two_not_successive_hyphens
				zipcode_with_two_not_successive_hyphens+=1
				return  "is possible zip codes but with two but not succesive hyphens"
			else :
				return "integer with two hyphens but not zipcode"
		else :			
			global integer_seperated_by_hyphen_not_zip_or_phone
			integer_seperated_by_hyphen_not_zip_or_phone+=1	
			return "is integers separated by hyphen but not zipcode or phone number"

def integerFunction(entry):
	regular_expressions(entry)
	if adict['find_string'] and not adict['find_space'] and adict['find_integer'] and not adict['find_email'] and not adict['find_website'] and not adict['find_dot'] and not adict['find_phone']:		
		global string_with_integer_without_spaces
		string_with_integer_without_spaces+=1
		return "is string with integer without spaces"

	if adict['find_string'] and adict['find_space'] and adict['find_integer'] and not adict['find_email'] and not adict['find_website'] and not adict['find_dot'] and not adict['find_phone']:		
		global string_with_integer_spaces
		string_with_integer_spaces+=1
		return "is string with integer and spaces"

	if adict['find_string'] and adict['find_phone'] and adict['find_integer'] and not adict['find_dot'] and len(adict['find_integer']) < 6 and adict['find_space']:		
		global string_with_integer_hyphen
		string_with_integer_hyphen += 1
		return "is Mixture of string integer and hyphen and spaces"

	if adict['find_string'] and adict['find_phone'] and adict['find_integer'] and not adict['find_dot'] and len(adict['find_integer']) < 6 and not adict['find_space']:		
		# global string_with_integer_hyphen
		string_with_integer_hyphen += 1
		return "is Mixture of string integer and hyphen but not spaces"

	if adict['find_integer'] and not adict['find_phone'] :
		if(adict['find_zipcode_without_hyphen']):
			if entry in zipcodes :
				# for j in range(0,len(zipcodes)-1):
					# a = a.split("-")[0]
					# if entry == zipcodes[j] :				
						# zipcode_array.append(entry)
				global mostly_zipcode_without_hyphen
				mostly_zipcode_without_hyphen += 1
				return  "is most probably a zipcode (without hyphen)" 
			else :				
				global pure_integer
				pure_integer += 1
				zipcode_array.append(entry)
				return  "is not a Zipcode"
		if(adict['find_zipcode_four_digits']):
			c = "0" + entry
			if c in zipcodes :
				# for j in range(0,len(zipcodes)-1):
					# a = a.split("-")[0]
					# if c == zipcodes[j] :													
						# zipcode_array.append(entry)
				global mostly_zipcode_four_digits
				mostly_zipcode_four_digits += 1
				return  "is most probably a zipcode (four digits)" 
			else :				
				# global pure_integer
				pure_integer += 1
				return  "is a four digit integer"

		if not adict['find_zipcode_without_hyphen'] and not adict['find_zipcode_four_digits'] and not adict['find_string'] and adict['find_dot']:			
			global decimal_integer
			decimal_integer += 1
			# print "no of dots is",len(adict['find_dot'])
			global decimal_integer_lengths
			decimal_integer_lengths.append(len(adict['find_dot']))
			# print "decimal_integer_lengths is",decimal_integer_lengths
			return "is Integer with decimals"
		
		if not adict['find_zipcode_without_hyphen'] and not adict['find_zipcode_four_digits'] and not adict['find_string'] and not adict['find_dot'] and not adict['find_pattern_phone_10_digits'] and not adict['find_phone_three_parts_two_hyphens'] and not adict['find_phone_three_parts_one_hyphen_one_parantheses'] and not adict['find_pattern_phone_three_parts_plus_one'] and not adict['find_pattern_phone_11_digits'] and not adict['find_special_characters'] :		
			# global pure_integer
			pure_integer += 1
			return "is Pure integer"

		if not adict['find_zipcode_without_hyphen'] and not adict['find_zipcode_four_digits'] and not adict['find_string'] and not adict['find_dot'] and adict['find_pattern_phone_10_digits'] and not adict['find_pattern_phone_11_digits'] and not adict['find_string']:			
			global phone_10_digits
			phone_10_digits += 1
			return "is 10 digit phone no"

		if adict['find_pattern_phone_three_parts_plus_one'] and not adict['find_string'] :	
			global phone_three_parts_plus_one
			phone_three_parts_plus_one+=1
			return "is phone with four parts containing three spaces and +1"

		if adict['find_pattern_phone_11_digits'] and not adict['find_string'] :
			if entry[0]=="1":				
				global phone_11_digits
				phone_11_digits+=1
				return  "is 11 digit phone no i.e starts with 1 followed by 10 digits"
			else :				
				# global pure_integer
				pure_integer+=1
				return "11 digit number but not phone no"

		# if adict['find_pattern_phone_10_digits'] and not adict['find_string'] :
		# 	# global phone_10_digits
		# 	phone_10_digits+=1

	if adict['find_decimal'] and adict['find_phone'] and not adict['find_string'] and entry[0] == "-" :		
		# global decimal_integer
		decimal_integer += 1
		# print "no of dots is",len(adict['find_dot'])
		# global decimal_integer_lengths
		decimal_integer_lengths.append(len(adict['find_dot']))
		return "is Negative integer with decimals"

	if adict['find_integer'] and not adict['find_dot'] and adict['find_phone'] and not adict['find_string'] and entry[0] == "-" and not adict['find_special_characters']:		
		# global pure_integer
		pure_integer += 1
		return "is Negative integer without decimals"

	if adict['find_integer'] and not adict['find_dot'] and adict['find_phone'] and not adict['find_string'] and entry[0] == "-" and adict['find_special_characters']:		
		pure_integer+=1
		return "is Negative integer with special characters"

	if adict['find_integer'] and adict['find_dot'] and adict['find_phone'] and not adict['find_string'] and entry[0] == "-" and not adict['find_decimal']:		
		decimal_integer+=1
		return "is decimal integer with misplaced dot"

	if adict['find_integer'] and adict['find_special_characters'] and (len(adict['find_integer'])+len(adict['find_special_characters']) == len(entry)):		
		global integer_with_special_characters
		integer_with_special_characters+=1
		return "is integer with special characters"

def stateCodeFunction(entry):
	regular_expressions(entry)
	if len(adict['find_caps']) and len((adict['find_string'])) == 2 and not adict['find_integer'] and not adict['find_empty'] and not adict['find_no_entry']  and not adict['find_dot'] and not adict['find_slash'] and not adict['find_small']:		
		matching = [s for s in states if entry == s] 		
		if matching  :					
			global state_code 
			state_code+=1
			return "is possible state code"
		else :			
			global two_letter_uppercase_string_not_state_code
			two_letter_uppercase_string_not_state_code += 1
			return "is two lettered uppercase string not state code"

	if len(adict['find_small']) and len((adict['find_string'])) == 2 and not adict['find_integer'] and not adict['find_empty'] and not adict['find_dot'] and not adict['find_no_entry'] and not adict['find_slash']:			
		matching_lower = [s for s in lower_states if entry == s]
		if matching_lower :					
			# global state_code
			state_code+=1
			return "is possible state code in lowercase"
		else :			
			global two_letter_lowercase_string_not_state_code
			two_letter_lowercase_string_not_state_code += 1
			return "is two lettered lowercase string not state code"

	if len(adict['find_small']) and len((adict['find_string'])) > 2 and not adict['find_integer'] and not adict['find_empty'] and not adict['find_dot'] and not adict['find_no_entry'] and not adict['find_slash']:			
		matching_lower = [s for s in lower_states if entry == s]
		if matching_lower :
			# global state_code
			state_code+=1
			return "is possible state name in lowercase"
		else :			
			# global two_letter_lowercase_string_not_state_code
			two_letter_lowercase_string_not_state_code += 1
			return "is not state name"

	if len(adict['find_caps']) == len(adict['find_string']) and len(adict['find_string']) > 2 and not adict['find_integer'] and not adict['find_empty'] and not adict['find_no_entry'] and not adict['find_dot'] and not adict['find_slash']:			
		matching_upper = [s for s in upper_states if entry == s]

		if matching_upper :
			# global state_code
			state_code+=1
			return "is possible state name in capital letters"
		else :			
			global pure_uppercase_string
			pure_uppercase_string += 1
			return "is uppercase string"

def emptyFunction(entry):
	regular_expressions(entry)
	if adict['find_empty'] :
		# print "empty entries are",adict['find_empty']		
		global empty
		empty+=1
		return "is empty"

def functioncalls():
	purestringReturn = purestring(regexes)
	if purestringReturn:
	    print purestringReturn

	stringReturn= purestring(regexes)
	if stringReturn:
	    print stringReturn

	pureStringWithSpacesReturn = pureStringWithSpaces(regexes)
	if pureStringWithSpacesReturn:
	    print pureStringWithSpacesReturn

	stringWithSpecialCharactersReturn = stringWithSpecialCharacters(regexes)
	if stringWithSpecialCharactersReturn:
	    print stringWithSpecialCharactersReturn

	websiteReturn = website(regexes)
	if websiteReturn:
	    print websiteReturn

	websiteWithoutWWWReturn = websiteWithoutWWW(regexes)
	if websiteWithoutWWWReturn:
	    print websiteWithoutWWWReturn

	emailReturn = email(regexes)
	if emailReturn:
	    print emailReturn

	phoneReturn = phone(regexes)
	if phoneReturn:
	    print phoneReturn

	integerReturn = integer(regexes)
	if integerReturn:
	    print integerReturn

	stateCodeReturn  = stateCode(regexes)
	if stateCodeReturn:
	    print stateCodeReturn
	    
	emptyReturn = empty(regexes)
	if emptyReturn:
	    print emptyReturn

def calculation():
	if count > 0:
		print "***********************************************************"
		print "Your file has imperfect commas. Please open improperData.txt"
		print "*************************************************************"
	else:
		global total_zipcode,total_phone,total_phone_only_integers,total_string,total_website,total_pure_string,total_special_characters, total_email
		total_zipcode =  valid_verified_zipcode_without_hyphen + valid_verified_zipcode_with_two_hyphen + zipcode_with_two_not_successive_hyphens + valid_verified_zipcode_with_one_hyphen + mostly_zipcode_with_one_hyphen + mostly_zipcode_without_hyphen + mostly_zipcode_with_two_hyphen + mostly_zipcode_four_digits			
		total_phone = phone_no_two_hyphens + phone_no_without_hyphen_or_alphabets + phone_no_with_alphabets + phone_no_with_parantheses + phone_no_one_hyphen + phone_no_with_only_open_parantheses + phone_no_with_only_close_parantheses + phone_three_parts_two_hyphens + phone_three_parts_one_hyphen_one_parantheses + phone_three_parts_plus_one + phone_10_digits                                                            
		total_phone_only_integers = phone_no_two_hyphens + phone_no_without_hyphen_or_alphabets + phone_no_with_parantheses + phone_no_one_hyphen + phone_no_with_only_open_parantheses + phone_no_with_only_close_parantheses			
		total_string = string_with_space_no_integer + string_with_integer_spaces + pure_uppercase_string + string_with_integer_hyphen + string_without_integer_without_spaces + string_with_symbol_instead_of_at + two_letter_uppercase_string_not_state_code + string_first_line_address + string_with_dots_not_email_not_website + two_letter_lowercase_string_not_state_code + string_with_integer_without_spaces							
		total_website = website + website_without_www
		total_pure_string = string_without_integer_without_spaces + string_with_space_no_integer + pure_uppercase_string + two_letter_uppercase_string_not_state_code + email_without_integer+state_code			
		total_special_characters = string_with_special_characters + integer_with_special_characters		
		total_email = email_with_integer + email_without_integer

		counter_decimal_integer = Counter(decimal_integer_lengths)
	return "return from calculation function"

def observations():
	print "\nOBSERVATIONS:"	

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
			else :
				pass
		else :
			pass

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

	# if(empty > (9.5*counter)/10):
	# 	print "\tThis column is predominantly empty. Hence any rows where data is present is considered defective."
	# 	print_integer_only_entries()
	# 	print_email_entries()
	# 	print_website_entries()
	# 	print_state_code()

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
			# print "\tSome Zipcodes have been wrongly placed in this column"
			# if ((string_with_integer_spaces > (7*(counter-empty))/10)) :
			# 	print "\tSince this column seems to be dominated by one of the lines of address it is hard to distinguish between door no and zipcode. Hence such rows are not flaged here."
			# 	pass
			# else :	
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

	# if(total_phone > (counter/2)) :
	# 	print "\tHigh probability that this column represents phone no"

	# if (total_website > (counter/3)):
	# 	print "\tThis column could be website "

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
		else :
			pass
	if(email == 0) :
		if(local_count == 0):
			print "\tThis column is definitely not email"
		else :
			pass	
	if(total_website == 0) :
		if(local_count == 0):
			print "\tThis column is definitely not website"
		else :
			pass
	if(total_phone == 0) :
		if(local_count == 0):
			print "\tThis column is definitely not phone"		
		else :
			pass
	if(total_zipcode == 0) :
		if(local_count == 0):
			print "\tThis column is definitely not zipcode"
		else :
			pass					
	if(two_letter_uppercase_string_not_state_code > (counter-empty)/10 ) :
		if(local_count == 0):
			print "\tThis column is definitely not state code"
		else :
			pass
	if(uncertain_entries):
		if(local_count == 0):
			print "\tThis column contains entries which seem anamalous."
		else :
			pass
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

class ExecuteProgram(object):
	
	def __init__(self,filesname,alpha,beta):
		self.globvar = alpha
		self.globar = beta
		self.filename = filesname

	def fix_file(self,filesname,alpha,beta):	
		global globvar
		global globar
		global filename
		globvar = alpha
		globar = beta
		filename = filesname
		return "inside fix_File function"
		
	def print_uppercase_entries(self):
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			# r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
			real_data = csv.DictReader(data)
			defective_rows = 0
			row_no_in_original_file = 0
			for row in real_data :
				for i in range(int(globvar),int(globar)):
					find_uppercase = re.findall(pattern_uppercase,row[mylist[i]])
					row_no_in_original_file += 1
					if find_uppercase :
						with open('improperData.txt','a') as fp :
							defective_rows+=1
							if defective_rows == 1 : 
								global func_count
								func_count += 1							
								fp.write("***************************************************************************************\n")
								fp.write("THIS ROW IS PRINTED BECAUSE THERE IS UPPERCASE ENTRY IN COLUMN ") 
								fp.write(mylist[i])
								fp.write(" OF THE CSV FILE\n")
								fp.write("***************************************************************************************\n")
							fp.write(str(row)+ "\n")
							fp.write("Defective row No:")
							fp.write(str(defective_rows) + "\n")
							new_row_no_in_original_file = row_no_in_original_file + 1
							fp.write("Row no in original file is ")
							fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
		return "inside function print_uppercase_entries "

	def print_empty_entries(self):
			
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
			real_data = csv.DictReader(data)
			defective_rows = 0
			row_no_in_original_file = 0				
			for element in line1:
				mylist = element.split(',')
	        
			for row in real_data :
				for i in range(int(globvar),int(globar)):
					find_empty = re.findall(pattern_empty,row[mylist[i]])
					find_no_entry = re.findall(pattern_no_entry,row[mylist[i]])
					row_no_in_original_file += 1							
					if find_empty or find_no_entry :					
						with open('improperData.txt','a') as fp :
							defective_rows+=1
							if defective_rows == 1 : 
								global func_count
								func_count += 1							
								fp.write("***************************************************************************************\n")
								fp.write("THIS ROW IS PRINTED BECAUSE THERE IS NO ENTRY IN COLUMN ") 
								fp.write(mylist[i])
								fp.write(" OF THE CSV FILE\n")
								fp.write("***************************************************************************************\n")
							fp.write(str(row)+ "\n")
							fp.write("Defective row No:")
							fp.write(str(defective_rows) + "\n")
							new_row_no_in_original_file = row_no_in_original_file + 1
							fp.write("Row no in original file is ")
							fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
		return "inside function print_empty_entries "

	def print_string_entries(self):
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)
			defective_rows = 0
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        
			for row in real_data :
				for i in range(int(globvar),int(globar)):
					find_string = re.findall(pattern_string,row[mylist[i]])
					row_no_in_original_file += 1				
					if find_string :
						with open('improperData.txt','a') as fp :
							defective_rows+=1
							if defective_rows == 1 :
								global func_count
								func_count += 1	 							
								fp.write("***************************************************************************************\n")
								fp.write("THIS ROW IS PRINTED BECAUSE A STRING IS PRESENT IN PLACE OF INTEGER IN COLUMN ") 
								fp.write(mylist[i])
								fp.write(" OF THE CSV FILE\n")
								fp.write("***************************************************************************************\n")
							fp.write(str(row)+ "\n")
							fp.write("Defective row No:")
							fp.write(str(defective_rows) + "\n")
							new_row_no_in_original_file = row_no_in_original_file + 1
							fp.write("Row no in original file is ")
							fp.write(str(new_row_no_in_original_file)+"\n" + "\n")	
		return "inside function print_string_entries "	

	def print_string_without_hyphen_entries(self):
		
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)
			defective_rows = 0
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        
			for row in real_data :
				for i in range(int(globvar),int(globar)):
					find_string = re.findall(pattern_string,row[mylist[i]])
					find_phone = re.findall(pattern_phone,row[mylist[i]])
					row_no_in_original_file += 1				
					if find_string and not find_phone :
						with open('improperData.txt','a') as fp :
							defective_rows+=1
							if defective_rows == 1 :
								global func_count
								func_count += 1	 							
								fp.write("***************************************************************************************\n")
								fp.write("THIS ROW IS PRINTED BECAUSE A STRING (WITHOUT HYPHEN) IS PRESENT IN COLUMN ") 
								fp.write(mylist[i])
								fp.write(" OF THE CSV FILE\n")
								fp.write("***************************************************************************************\n")
							fp.write(str(row)+ "\n")
							fp.write("Defective row No:")
							fp.write(str(defective_rows) + "\n")
							new_row_no_in_original_file = row_no_in_original_file + 1
							fp.write("Row no in original file is ")
							fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
		return "inside function print_string_without_hyphen_entries "	

	def print_string_only_entries(self):
		
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)
			defective_rows = 0
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        
			for row in real_data :
				for i in range(int(globvar),int(globar)):
					find_string = re.findall(pattern_string,row[mylist[i]])
					row_no_in_original_file += 1				
					if find_string and len(find_string) == len(row[mylist[i]]) :
						with open('improperData.txt','a') as fp :
							defective_rows+=1
							if defective_rows == 1 : 
								global func_count
								func_count += 1								
								fp.write("***************************************************************************************\n")
								fp.write("THIS ROW IS PRINTED BECAUSE ONLY STRING IS PRESENT IN COLUMN ") 
								fp.write(mylist[i])
								fp.write(" OF THE CSV FILE\n")
								fp.write("***************************************************************************************\n")
							fp.write(str(row)+ "\n")
							fp.write("Defective row No:")
							fp.write(str(defective_rows) + "\n")
							new_row_no_in_original_file = row_no_in_original_file + 1
							fp.write("Row no in original file is ")
							fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
		return "inside function print_string_only_entries "	

	def print_string_with_integer_and_space_entries(self):
		
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)
			defective_rows = 0
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        
			for row in real_data :
				for i in range(int(globvar),int(globar)):
					find_string = re.findall(pattern_string,row[mylist[i]])
					row_no_in_original_file += 1				
					if find_string and find_integer and find_space :
						with open('improperData.txt','a') as fp :
							defective_rows+=1
							if defective_rows == 1 : 
								global func_count
								func_count += 1								
								fp.write("***************************************************************************************\n")
								fp.write("THIS ROW IS PRINTED BECAUSE A STRING WITH INTEGER AND SPACE IS PRESENT IN COLUMN ") 
								fp.write(mylist[i])
								fp.write(" OF THE CSV FILE\n")
								fp.write("***************************************************************************************\n")
							fp.write(str(row)+ "\n")
							fp.write("Defective row No:")
							fp.write(str(defective_rows) + "\n")
							new_row_no_in_original_file = row_no_in_original_file + 1
							fp.write("Row no in original file is ")
							fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
		return "inside function print_string_with_integer_and_space_entries "	

	def print_integer_entries(self):
		
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)	
			defective_rows = 0
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        
			for row in real_data :			
				for i in range(int(globvar),int(globar)):				
					find_integer = re.findall(pattern_integer,row[mylist[i]])
					row_no_in_original_file += 1								
					if find_integer and len(find_integer)!=len(row[mylist[i]]):
						with open('improperData.txt','a') as fp :
							defective_rows += 1
							if defective_rows == 1 : 
								global func_count
								func_count += 1										
								fp.write("***************************************************************************************\n")
								fp.write("THIS ROW IS PRINTED BECAUSE AN INTEGER(BUT NOT ONLY INTEGER) IS PRESENT IN COLUMN ")
								fp.write(mylist[i])
								fp.write(" OF THE CSV FILE\n")
								fp.write("***************************************************************************************\n")
							fp.write(str(row)+ "\n")
							fp.write("Defective row No:")
							fp.write(str(defective_rows) + "\n")
							new_row_no_in_original_file = row_no_in_original_file + 1
							fp.write("Row no in original file is ")
							fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
		return "inside function print_integer_entries "	

	def print_integer_only_entries(self):
		
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)		
			real_data = csv.DictReader(data)	
			defective_rows = 0
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        
			for row in real_data :			
				for i in range(int(globvar),int(globar)):				
					find_integer = re.findall(pattern_integer,row[mylist[i]])
					find_string = re.findall(pattern_string,row[mylist[i]])
					row_no_in_original_file += 1								
					if find_integer and not find_string and len(find_integer)==len(row[mylist[i]]) :
						with open('improperData.txt','a') as fp :
							defective_rows += 1
							if defective_rows == 1 : 
								global func_count
								func_count += 1								
								fp.write("***************************************************************************************\n")
								fp.write("THIS ROW IS PRINTED BECAUSE A PURE INTEGER IS PRESENT IN THE COLUMN ")
								fp.write(mylist[i])
								fp.write(" OF THE CSV FILE\n")
								fp.write("***************************************************************************************\n")
							fp.write(str(row)+ "\n")
							fp.write("Defective row No:")
							fp.write(str(defective_rows) + "\n")
							new_row_no_in_original_file = row_no_in_original_file + 1
							fp.write("Row no in original file is ")
							fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
		return "inside function print_integer_only_entries "	

	def print_improper_decimal_integers(self):
		
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)		
			real_data = csv.DictReader(data)	
			defective_rows = 0
			row_no_in_original_file = 0	
			line1=r.next()
			counter_decimal_integer = Counter(decimal_integer_lengths)
			for element in line1:
				mylist = element.split(',')
	        
			for row in real_data :			
				for i in range(int(globvar),int(globar)):				
					find_integer = re.findall(pattern_integer,row[mylist[i]])
					find_string = re.findall(pattern_string,row[mylist[i]])
					find_dot = re.findall(pattern_dot,row[mylist[i]])
					row_no_in_original_file += 1

					if find_integer and not find_string and len(decimal_integer_lengths) > 0  and len(find_dot) != counter_decimal_integer.most_common(1)[0][0]:
						with open('improperData.txt','a') as fp :
							defective_rows += 1
							if defective_rows == 1 : 
								global func_count
								func_count += 1								
								fp.write("***************************************************************************************\n")
								fp.write("THIS ROW IS PRINTED BECAUSE IMPROPER DECIMAL INTEGER IS PRESENT IN THE COLUMN ")
								fp.write(mylist[i])
								fp.write(" OF THE CSV FILE\n")
								fp.write("***************************************************************************************\n")
							fp.write(str(row)+ "\n")
							fp.write("Defective row No:")
							fp.write(str(defective_rows) + "\n")
							new_row_no_in_original_file = row_no_in_original_file + 1
							fp.write("Row no in original file is ")
							fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
		return "inside function print_improper_decimal_integers"													

	def improper_integer_entries(self):
		
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)	
			defective_rows = 0
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        
			for row in real_data :			
				for i in range(int(globvar),int(globar)):
					find_space = re.findall(pattern_space,row[mylist[i]])
					find_empty = re.findall(pattern_empty,row[mylist[i]])
					find_phone = re.findall(pattern_phone,row[mylist[i]])
					find_integer = re.findall(pattern_integer,row[mylist[i]])
					find_string = re.findall(pattern_string,row[mylist[i]])
					find_hashtag = re.findall(pattern_hashtag,row[mylist[i]])
					find_pattern_phone_parantheses = re.findall(patten_phone_parantheses,row[mylist[i]])	
					find_slash = re.findall(pattern_slash,row[mylist[i]])	
					row_no_in_original_file += 1													
					if len(find_phone) == 1 and len(find_integer) != 10 and not find_string and not find_hashtag and not find_pattern_phone_parantheses and not find_slash :
						with open('improperData.txt','a') as fp :
							defective_rows += 1
							if defective_rows == 1 :
								global func_count
								func_count += 1								
								fp.write("***************************************************************************************\n")
								fp.write("THIS ROW IS PRINTED BECAUSE AN UNCERTAIN INTEGER ENTRY IS PRESENT  IN THE COLUMN ")
								fp.write(mylist[i])
								fp.write(" OF THE CSV FILE\n")
								fp.write("***************************************************************************************\n")
							fp.write(str(row)+ "\n")
							fp.write("Defective row No:")
							fp.write(str(defective_rows) + "\n")
							new_row_no_in_original_file = row_no_in_original_file + 1
							fp.write("Row no in original file is ")
							fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
		return "inside function improper_integer_entries "	

	def print_email_entries(self):
		
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)				
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        
			defective_rows = 0	
			for row in real_data :							
				for i in range(int(globvar),int(globar)):				
					find_email = re.findall(pattern_email,row[mylist[i]])
					find_dot = re.findall(pattern_dot,row[mylist[i]])
					find_space = re.findall(pattern_space,row[mylist[i]])
					row_no_in_original_file += 1
													
					if find_email and find_dot and not find_space :
						with open('improperData.txt','a') as fp :
							defective_rows += 1
							if defective_rows == 1 :
								global func_count									
								func_count += 1	
								fp.write("***************************************************************************************\n")
								fp.write("THIS ROW IS PRINTED BECAUSE AN EMAIL IS PRESENT IN PLACE OF STRING IN THE COLUMN ")
								fp.write(mylist[i])
								fp.write(" OF THE CSV FILE\n")
								fp.write("***************************************************************************************\n")
							fp.write(str(row)+ "\n")
							fp.write("Defective row No:")
							fp.write(str(defective_rows) + "\n")
							new_row_no_in_original_file = row_no_in_original_file + 1
							fp.write("Row no in original file is ")
							fp.write(str(new_row_no_in_original_file)+"\n" + "\n")						
		return "inside function print_email_entries "	

	def print_website_entries(self):
		
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)	
			defective_rows = 0
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        
			for row in real_data :			
				for i in range(int(globvar),int(globar)):				
					find_website = re.findall(pattern_website,row[mylist[i]])
					find_dot = re.findall(pattern_dot,row[mylist[i]])
					row_no_in_original_file += 1								
					if find_website and find_dot:
						with open('improperData.txt','a') as fp :
							defective_rows += 1
							if defective_rows == 1 : 
								global func_count
								func_count += 1	
								fp.write("***************************************************************************************\n")
								fp.write("THIS ROW IS PRINTED BECAUSE A WEBSITE IS PRESENT IN THE COLUMN ")
								fp.write(mylist[i])
								fp.write(" OF THE CSV FILE\n")
								fp.write("***************************************************************************************\n")
							fp.write(str(row)+ "\n")
							fp.write("Defective row No:")
							fp.write(str(defective_rows) + "\n")
							new_row_no_in_original_file = row_no_in_original_file + 1
							fp.write("Row no in original file is ")
							fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
		return "inside function print_website_entries "	

	def print_special_characters(self):
		
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)	
			defective_rows = 0
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        
			for row in real_data :			
				for i in range(int(globvar),int(globar)):				
					find_special_characters=re.findall(pattern_special_characters,row[mylist[i]])
					row_no_in_original_file += 1
					if find_special_characters :
						with open('improperData.txt','a') as fp :
							defective_rows += 1
							if defective_rows == 1 : 
								global func_count
								func_count += 1	
								fp.write("***************************************************************************************\n")
								fp.write("THIS ROW IS PRINTED BECAUSE A SPECIAL CHARACTER IS PRESENT IN THE COLUMN ")
								fp.write(mylist[i])
								fp.write(" OF THE CSV FILE\n")
								fp.write("***************************************************************************************\n")
							fp.write(str(row)+ "\n")
							fp.write("Defective row No:")
							fp.write(str(defective_rows) + "\n")
							new_row_no_in_original_file = row_no_in_original_file + 1
							fp.write("Row no in original file is ")
							fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
		return "inside function print_special_characters "	

	def print_special_characters_phone(self):
		
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)	
			defective_rows = 0
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        
			for row in real_data :			
				for i in range(int(globvar),int(globar)):				
					find_special_characters_phone=re.findall(pattern_special_characters_phone,row[mylist[i]])
					row_no_in_original_file += 1
					if find_special_characters_phone :
						with open('improperData.txt','a') as fp :
							defective_rows += 1
							if defective_rows == 1 : 
								global func_count
								func_count += 1	
								fp.write("***************************************************************************************\n")
								fp.write("THIS ROW IS PRINTED BECAUSE A SPECIAL CHARACTER (unlikely for telephone no) IS PRESENT IN THE COLUMN ")
								fp.write(mylist[i])
								fp.write(" OF THE CSV FILE\n")
								fp.write("***************************************************************************************\n")
							fp.write(str(row)+ "\n")
							fp.write("Defective row No:")
							fp.write(str(defective_rows) + "\n")
							new_row_no_in_original_file = row_no_in_original_file + 1
							fp.write("Row no in original file is ")
							fp.write(str(new_row_no_in_original_file)+"\n" + "\n")	
		return "inside function  print_special_characters_phone"	

	def print_special_characters_website(self):
		
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)	
			defective_rows = 0
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        
			for row in real_data :			
				for i in range(int(globvar),int(globar)):				
					find_special_characters_website=re.findall(pattern_special_characters_website,row[mylist[i]])
					row_no_in_original_file += 1
					if find_special_characters_website :
						with open('improperData.txt','a') as fp :
							defective_rows += 1
							if defective_rows == 1 : 
								global func_count
								func_count += 1	
								fp.write("***************************************************************************************\n")
								fp.write("THIS ROW IS PRINTED BECAUSE A SPECIAL CHARACTER (unlikely for website) IS PRESENT IN THE COLUMN ")
								fp.write(mylist[i])
								fp.write(" OF THE CSV FILE\n")
								fp.write("***************************************************************************************\n")
							fp.write(str(row)+ "\n")
							fp.write("Defective row No:")
							fp.write(str(defective_rows) + "\n")
							new_row_no_in_original_file = row_no_in_original_file + 1
							fp.write("Row no in original file is ")
							fp.write(str(new_row_no_in_original_file)+"\n" + "\n")															
		return "inside function print_special_characters_website "	

	def print_hyphen(self):
		
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)
			defective_rows = 0
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')		
	        
			for row in real_data :				
				for i in range(int(globvar),int(globar)):					
					find_phone=re.findall(pattern_phone,row[mylist[i]])					
					row_no_in_original_file += 1
					if find_phone :
						with open('improperData.txt','a') as fp :
							defective_rows += 1
							if defective_rows == 1 : 
								global func_count
								func_count += 1	
								fp.write("***************************************************************************************\n")
								fp.write("THIS ROW IS PRINTED BECAUSE A HYPHEN IS PRESENT IN THE COLUMN ")
								fp.write(mylist[i])
								fp.write(" OF THE CSV FILE\n")
								fp.write("***************************************************************************************\n")
							fp.write(str(row)+ "\n")
							fp.write("Defective row No:")
							fp.write(str(defective_rows) + "\n")
							new_row_no_in_original_file = row_no_in_original_file + 1
							fp.write("Row no in original file is ")
							fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
		return "inside function print_hyphen  "	
		# return func_count								

	def print_space_entries(self):
		
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)	
			defective_rows = 0
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        
			for row in real_data :			
				for i in range(int(globvar),int(globar)):				
					find_space = re.findall(pattern_space,row[mylist[i]])
					find_string = re.findall(pattern_string,row[mylist[i]])
					find_integer = re.findall(pattern_integer,row[mylist[i]])
					row_no_in_original_file += 1								
					if (find_string and find_space) or (find_integer and find_space):
						with open('improperData.txt','a') as fp :
							defective_rows += 1
							if defective_rows == 1 : 
								global func_count
								func_count += 1	
								fp.write("***************************************************************************************\n")
								fp.write("THIS ROW IS PRINTED BECAUSE SPACE IS PRESENT IN THE COLUMN ")
								fp.write(mylist[i])
								fp.write(" OF THE CSV FILE\n")
								fp.write("***************************************************************************************\n")
							fp.write(str(row)+ "\n")
							fp.write("Defective row No:")
							fp.write(str(defective_rows) + "\n")
							new_row_no_in_original_file = row_no_in_original_file + 1
							fp.write("Row no in original file is ")
							fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
		return "inside function print_space_entries "	

	def print_no_dots(self):
		
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)	
			defective_rows = 0
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        
			for row in real_data :			
				for i in range(int(globvar),int(globar)):				
					find_string = re.findall(pattern_string,row[mylist[i]])
					find_dot = re.findall(pattern_dot,row[mylist[i]])
					row_no_in_original_file += 1								
					if (find_string and not find_dot) :
						with open('improperData.txt','a') as fp :
							defective_rows += 1
							if defective_rows == 1 : 
								global func_count
								func_count += 1	
								fp.write("***************************************************************************************\n")
								fp.write("THIS ROW IS PRINTED BECAUSE NO DOTS WERE PRESENT IN THE COLUMN ")
								fp.write(mylist[i])
								fp.write(" OF THE CSV FILE\n")
								fp.write("***************************************************************************************\n")
							fp.write(str(row)+ "\n")
							fp.write("Defective row No:")
							fp.write(str(defective_rows) + "\n")
							new_row_no_in_original_file = row_no_in_original_file + 1
							fp.write("Row no in original file is ")
							fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
		return "inside function print_no_dots "	

	def print_pure_integer_not_zipcode(self):
		
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)	
			defective_rows = 0
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        

			for row in real_data :			
				for i in range(int(globvar),int(globar)):				
					find_integer = re.findall(pattern_integer,row[mylist[i]])
					find_string = re.findall(pattern_string,row[mylist[i]])
					find_phone = re.findall(pattern_phone,row[mylist[i]])
					find_zipcode_without_hyphen= re.findall(pattern_zipcode_without_hyphen,row[mylist[i]])	
					find_zipcode_four_digits=re.findall(patter_zipcode_four_digits,row[mylist[i]])				
					find_dot = re.findall(pattern_dot,row[mylist[i]])

					row_no_in_original_file += 1						
					if find_integer and not find_phone and not find_zipcode_without_hyphen and not find_zipcode_four_digits and not find_string and not find_dot:
						# print "ERERERWE"
						with open('improperData.txt','a') as fp :
							defective_rows += 1
							if defective_rows == 1 : 
								global func_count
								func_count += 1	
								fp.write("***************************************************************************************\n")
								fp.write("THIS ROW IS PRINTED BECAUSE PURE INTEGER (but not zipcode) IS PRESENT IN THE COLUMN ")
								fp.write(mylist[i])
								fp.write(" OF THE CSV FILE\n")
								fp.write("***************************************************************************************\n")
							fp.write(str(row)+ "\n")
							fp.write("Defective row No:")
							fp.write(str(defective_rows) + "\n")
							new_row_no_in_original_file = row_no_in_original_file + 1
							fp.write("Row no in original file is ")
							fp.write(str(new_row_no_in_original_file)+"\n" + "\n")								
		return "inside function print_pure_integer_not_zipcode "	

	def print_integer_more_than_string(self):
		
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)	
			defective_rows = 0
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        
			for row in real_data :			
				for i in range(int(globvar),int(globar)):				
					find_integer = re.findall(pattern_integer,row[mylist[i]])
					find_string = re.findall(pattern_string,row[mylist[i]])	
					find_website = re.findall(pattern_website,row[mylist[i]])				
					row_no_in_original_file += 1								
					if (len(find_integer) > len(find_string) and not find_website) :
						with open('improperData.txt','a') as fp :
							defective_rows += 1
							if defective_rows == 1 : 
								global func_count
								func_count += 1	
								fp.write("***************************************************************************************\n")
								fp.write("THIS ROW IS PRINTED BECAUSE INTEGERS DOMINATE STRING IN THE COLUMN ")
								fp.write(mylist[i])
								fp.write(" OF THE CSV FILE\n")
								fp.write("***************************************************************************************\n")
							fp.write(str(row)+ "\n")
							fp.write("Defective row No:")
							fp.write(str(defective_rows) + "\n")
							new_row_no_in_original_file = row_no_in_original_file + 1
							fp.write("Row no in original file is ")
							fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
		return "inside function print_integer_more_than_string "	

	def print_string_more_than_integer(self):
		
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)	
			defective_rows = 0
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        
			for row in real_data :			
				for i in range(int(globvar),int(globar)):				
					find_integer = re.findall(pattern_integer,row[mylist[i]])
					find_string = re.findall(pattern_string,row[mylist[i]])					
					row_no_in_original_file += 1								
					if (len(find_string) > len(find_integer)) :
						with open('improperData.txt','a') as fp :
							defective_rows += 1
							if defective_rows == 1 : 
								global func_count
								func_count += 1	
								fp.write("***************************************************************************************\n")
								fp.write("THIS ROW IS PRINTED BECAUSE STRING DOMINATE INTEGER IN THE COLUMN ")
								fp.write(mylist[i])
								fp.write(" OF THE CSV FILE\n")
								fp.write("***************************************************************************************\n")
							fp.write(str(row)+ "\n")
							fp.write("Defective row No:")
							fp.write(str(defective_rows) + "\n")
							new_row_no_in_original_file = row_no_in_original_file + 1
							fp.write("Row no in original file is ")
							fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
		return "inside function print_string_more_than_integer"	

	def print_not_state_code(self):
		
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)
			defective_rows = 0
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        
			for row in real_data :
				for i in range(int(globvar),int(globar)):				
					row_no_in_original_file += 1										
					if (row[mylist[i]] in states) or (row[mylist[i]] in lower_states) or (row[mylist[i]] in upper_states)or (row[mylist[i]] == " ") or (row[mylist[i]] == "") :
						pass					
					else :
						with open('improperData.txt','a') as fp :
							defective_rows+=1
							if defective_rows == 1 :
								# print "Defective",row[mylist[i]] 
								global func_count
								func_count += 1	
								fp.write("***************************************************************************************\n")
								fp.write("THIS ROW IS PRINTED BECAUSE THE ENTRY IN THE COLUMN ")
								fp.write(mylist[i])
								fp.write(" OF THE CSV FILE IS NOT A US STATE\n")
								fp.write("***************************************************************************************\n")
							fp.write(str(row)+ "\n")
							fp.write("Defective row No:")
							fp.write(str(defective_rows) + "\n")
							new_row_no_in_original_file = row_no_in_original_file + 1
							fp.write("Row no in original file is ")
							fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
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
		
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)				
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        
			defective_rows = 0
			for row in real_data :					
				for i in range(int(globvar),int(globar)):				
					row_no_in_original_file += 1
					global func_count
					find_string = re.findall(pattern_string,row[mylist[i]])
					find_at_the_rate=re.findall(pattern_at_the_rate,row[mylist[i]])
					find_dot = re.findall(pattern_dot,row[mylist[i]])
					
					if find_string and find_at_the_rate and not find_dot :							
						#print "defective_rowspoi:,",defective_rows
						with open('improperData.txt','a') as fp :
							defective_rows+=1
							if defective_rows == 1 :
								# print "Defective",row[mylist[i]] 
								# global func_count
								func_count += 1	
								fp.write("***************************************************************************************\n")
								fp.write("THIS ROW IS PRINTED BECAUSE @ IS FOUND (alongside strings) IN THE COLUMN ")
								fp.write(mylist[i])
								fp.write(" OF THE CSV FILE \n")
								fp.write("***************************************************************************************\n")								
							fp.write(str(row)+ "\n")
							fp.write("Defective row No:")
							fp.write(str(defective_rows) + "\n")
							new_row_no_in_original_file = row_no_in_original_file + 1
							fp.write("Row no in original file is ")
							fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
		return "inside function print_string_with_symbol_at_but_not_email "	

	def print_string_with_hashtag_without_space (self):
		
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)				
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        
			defective_rows = 0
			for row in real_data :					
				for i in range(int(globvar),int(globar)):				
					row_no_in_original_file += 1
					global func_count
					find_string = re.findall(pattern_string,row[mylist[i]])
					find_hashtag = re.findall(pattern_hashtag,row[mylist[i]])
					find_space = re.findall(pattern_space,row[mylist[i]])						

					if find_string and find_hashtag and not find_space :							
						#print "defective_rowspoi:,",defective_rows
						with open('improperData.txt','a') as fp :
							defective_rows+=1
							if defective_rows == 1 :
								# print "Defective",row[mylist[i]] 
								# global func_count
								func_count += 1	
								fp.write("***************************************************************************************\n")
								fp.write("THIS ROW IS PRINTED BECAUSE # IS FOUND (alongside strings) IN THE COLUMN ")
								fp.write(mylist[i])
								fp.write(" OF THE CSV FILE \n")
								fp.write("***************************************************************************************\n")								
							fp.write(str(row)+ "\n")
							fp.write("Defective row No:")
							fp.write(str(defective_rows) + "\n")
							new_row_no_in_original_file = row_no_in_original_file + 1
							fp.write("Row no in original file is ")
							fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
		return "inside function print_string_with_hashtag_without_space "	

	def print_integer_with_hashtag_without_space (self):
			
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)				
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
			defective_rows = 0
			for row in real_data :					
				for i in range(int(globvar),int(globar)):				
					row_no_in_original_file += 1
					global func_count
					find_integer = re.findall(pattern_integer,row[mylist[i]])						
					find_hashtag = re.findall(pattern_hashtag,row[mylist[i]])
					find_space = re.findall(pattern_space,row[mylist[i]])						

					if find_integer and find_hashtag and not find_space :							
						#print "defective_rowspoi:,",defective_rows
						with open('improperData.txt','a') as fp :
							defective_rows+=1
							if defective_rows == 1 :
								# print "Defective",row[mylist[i]] 
								# global func_count
								func_count += 1	
								fp.write("***************************************************************************************\n")
								fp.write("THIS ROW IS PRINTED BECAUSE # IS FOUND (alongside integers) IN THE COLUMN ")
								fp.write(mylist[i])
								fp.write(" OF THE CSV FILE \n")
								fp.write("***************************************************************************************\n")								
							fp.write(str(row)+ "\n")
							fp.write("Defective row No:")
							fp.write(str(defective_rows) + "\n")
							new_row_no_in_original_file = row_no_in_original_file + 1
							fp.write("Row no in original file is ")
							fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
		return "inside function print_integer_with_hashtag_without_space "
					
	def print_string_with_parantheses (self):
			
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)				
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        
			defective_rows = 0
			for row in real_data :					
				for i in range(int(globvar),int(globar)):				
					row_no_in_original_file += 1
					global func_count
					find_string = re.findall(pattern_string,row[mylist[i]])						
					find_open_parantheses=re.findall(pattern_open_parantheses,row[mylist[i]])
					find_close_paranthses=re.findall(pattern_close_parantheses,row[mylist[i]])							

					if (find_string and find_open_parantheses) or (find_string and find_close_paranthses):							
						#print "defective_rows:,",defective_rows							
						with open('improperData.txt','a') as fp :								
							defective_rows+=1
							if defective_rows == 1 :									
								# print "Defective",row[mylist[i]] 
								# global func_count
								func_count += 1	
								fp.write("***************************************************************************************\n")
								fp.write("THIS ROW IS PRINTED BECAUSE PARANTHESES IS FOUND (alongside strings) IN THE COLUMN ")
								fp.write(mylist[i])
								fp.write(" OF THE CSV FILE \n")
								fp.write("***************************************************************************************\n")
							fp.write(str(row)+ "\n")
							fp.write("Defective row No:")
							fp.write(str(defective_rows) + "\n")
							new_row_no_in_original_file = row_no_in_original_file + 1
							fp.write("Row no in original file is ")
							fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
		return "inside function print_string_with_parantheses "

	def print_integer_with_symbol_at_but_not_email (self):
		
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)				
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        
			defective_rows = 0
			for row in real_data :					
				for i in range(int(globvar),int(globar)):				
					row_no_in_original_file += 1
					global func_count
					find_integer = re.findall(pattern_integer,row[mylist[i]])						
					find_at_the_rate=re.findall(pattern_at_the_rate,row[mylist[i]])
					find_dot = re.findall(pattern_dot,row[mylist[i]])						

					if find_integer and find_at_the_rate and not find_dot :															
						defective_rows+=1
						with open('improperData.txt','a') as fp :
							
							if defective_rows == 1 :
								# print "Defective",row[mylist[i]] 
								# global func_count
								func_count += 1	
								fp.write("***************************************************************************************\n")
								fp.write("THIS ROW IS PRINTED BECAUSE @ IS FOUND (alongside integers) IN THE COLUMN ")
								fp.write(mylist[i])
								fp.write(" OF THE CSV FILE \n")
								fp.write("***************************************************************************************\n")								
							fp.write(str(row)+ "\n")
							fp.write("Defective row No:")
							fp.write(str(defective_rows) + "\n")
							new_row_no_in_original_file = row_no_in_original_file + 1
							fp.write("Row no in original file is ")
							fp.write(str(new_row_no_in_original_file)+"\n" + "\n")

					# print "defective_rows:,",defective_rows
		return "inside function print_integer_with_symbol_at_but_not_email "	

	def print_integer_with_symbol_at_and_dot (self):
		
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)				
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        
			defective_rows = 0
			for row in real_data :					
				for i in range(int(globvar),int(globar)):				
					row_no_in_original_file += 1
					global func_count
					find_integer = re.findall(pattern_integer,row[mylist[i]])			
					find_at_the_rate=re.findall(pattern_at_the_rate,row[mylist[i]])
					find_dot = re.findall(pattern_dot,row[mylist[i]])
					find_string = re.findall(pattern_string,row[mylist[i]])				

					if find_integer and find_at_the_rate and find_dot and not find_string :													
						defective_rows+=1
						with open('improperData.txt','a') as fp :						
							if defective_rows == 1 :
								# print "Defective",row[mylist[i]] 
								# global func_count
								func_count += 1	
								fp.write("***************************************************************************************\n")
								fp.write("THIS ROW IS PRINTED BECAUSE @ IS FOUND (alongside decimal integers) IN THE COLUMN ")
								fp.write(mylist[i])
								fp.write(" OF THE CSV FILE \n")
								fp.write("***************************************************************************************\n")								
							fp.write(str(row)+ "\n")
							fp.write("Defective row No:")
							fp.write(str(defective_rows) + "\n")
							new_row_no_in_original_file = row_no_in_original_file + 1
							fp.write("Row no in original file is ")
							fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
		return "inside function print_integer_with_symbol_at_and_dot "			

	def print_integer_with_parantheses  (self):
		
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)				
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        
			defective_rows = 0
			for row in real_data :					
				for i in range(int(globvar),int(globar)):				
					row_no_in_original_file += 1
					global func_count
					find_integer = re.findall(pattern_integer,row[mylist[i]])						
					find_open_parantheses=re.findall(pattern_open_parantheses,row[mylist[i]])
					find_close_paranthses=re.findall(pattern_close_parantheses,row[mylist[i]])

					if (find_integer and find_open_parantheses) or (find_integer and find_close_paranthses):							
						defective_rows+=1
						with open('improperData.txt','a') as fp :															
							if defective_rows == 1 :									
								# print "Defective",row[mylist[i]] 
								# global func_count
								func_count += 1	
								fp.write("***************************************************************************************\n")
								fp.write("THIS ROW IS PRINTED BECAUSE PARANTHESES IS FOUND (alongside integers) IN THE COLUMN ")
								fp.write(mylist[i])
								fp.write(" OF THE CSV FILE \n")
								fp.write("***************************************************************************************\n")
							fp.write(str(row)+ "\n")
							fp.write("Defective row No:")
							fp.write(str(defective_rows) + "\n")
							new_row_no_in_original_file = row_no_in_original_file + 1
							fp.write("Row no in original file is ")
							fp.write(str(new_row_no_in_original_file)+"\n" + "\n")							
		return "inside function print_integer_with_parantheses "	

	def print_decimal_values(self):
		
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)				
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        
			defective_rows = 0
			for row in real_data :					
				for i in range(int(globvar),int(globar)):				
					row_no_in_original_file += 1
					global func_count
					find_integer = re.findall(pattern_integer,row[mylist[i]])												
					find_zipcode_without_hyphen= re.findall(pattern_zipcode_without_hyphen,row[mylist[i]])
					find_zipcode_four_digits=re.findall(patter_zipcode_four_digits,row[mylist[i]])
					find_string = re.findall(pattern_string,row[mylist[i]])
					find_dot = re.findall(pattern_dot,row[mylist[i]])

					if find_integer and not find_zipcode_without_hyphen and not find_zipcode_four_digits and not find_string and find_dot:
						defective_rows+=1
						with open('improperData.txt','a') as fp :															
							if defective_rows == 1 :									
								# print "Defective",row[mylist[i]] 
								# global func_count
								func_count += 1	
								fp.write("***************************************************************************************\n")
								fp.write("THIS ROW IS PRINTED BECAUSE DECIMAL INTEGER IS FOUND IN THE COLUMN ")
								fp.write(mylist[i])
								fp.write(" OF THE CSV FILE \n")
								fp.write("***************************************************************************************\n")
							fp.write(str(row)+ "\n")
							fp.write("Defective row No:")
							fp.write(str(defective_rows) + "\n")
							new_row_no_in_original_file = row_no_in_original_file + 1
							fp.write("Row no in original file is ")
							fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
		return "inside function print_decimal_values "	

	def print_state_code(self):
		
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)
			defective_rows = 0
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        
			for row in real_data :
				for i in range(int(globvar),int(globar)):				
					row_no_in_original_file += 1										
					if (row[mylist[i]] in state_code_array) and (row[mylist[i]] not in states_and_cities) :	
						for j in range(i+1,len(row)):
							key = (row[mylist[i]], row[mylist[j]])
							if key[0] == key[1] :	
								with open('improperData.txt','a') as fp :
									defective_rows+=1
									if defective_rows == 1 : 
										global func_count
										func_count += 1	
										fp.write("***************************************************************************************\n")
										fp.write("THIS ROW IS PRINTED BECAUSE THE ENTRY IN THE COLUMN ") 
										fp.write(mylist[i])
										fp.write(" OF THE CSV FILE IS A US STATE\n")
										fp.write("***************************************************************************************\n")
									fp.write(str(row)+ "\n")
									fp.write("Defective row No:")
									fp.write(str(defective_rows) + "\n")
									new_row_no_in_original_file = row_no_in_original_file + 1
									fp.write("Row no in original file is ")
									fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
					else : 
						pass
		return "inside function print_state_code "	

	def print_state_code_lowercase(self):
		
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)
			defective_rows = 0
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        
			for row in real_data :					
				for i in range(int(globvar),int(globar)):										
					row_no_in_original_file += 1
					find_lowercase = re.findall(pattern_lowercase,row[mylist[i]])						
					if (row[mylist[i]].upper() in state_code_array) and find_lowercase:
						print "HERE"
						# for j in range(i+1,len(row)):
						# 	key = (row[mylist[i]], row[mylist[j]])
						# 	print "key is",key
						# 	if key[0] == key[1] :	
						with open('improperData.txt','a') as fp :
							defective_rows+=1
							if defective_rows == 1 : 
								global func_count
								func_count += 1	
								fp.write("***************************************************************************************\n")
								fp.write("THIS ROW IS PRINTED BECAUSE THE ENTRY IN THE COLUMN ") 
								fp.write(mylist[i])
								fp.write(" OF THE CSV FILE IS A US STATE ,BUT IN LOWERCASE\n")
								fp.write("***************************************************************************************\n")
							fp.write(str(row)+ "\n")
							fp.write("Defective row No:")
							fp.write(str(defective_rows) + "\n")
							new_row_no_in_original_file = row_no_in_original_file + 1
							fp.write("Row no in original file is ")
							fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
					else : 
						pass
		return "inside function print_state_code_lowercase"								
		
	def print_zip_code(self):
		
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)
			defective_rows = 0
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        	
			for row in real_data :
				for i in range(int(globvar),int(globar)):				
					row_no_in_original_file += 1
					find_phone = re.findall(pattern_phone,row[mylist[i]])
					find_string = re.findall(pattern_string,row[mylist[i]])
					find_integer = re.findall(pattern_integer,row[mylist[i]])
					find_pattern_phone_parantheses = re.findall(patten_phone_parantheses,row[mylist[i]])
					find_successive_hyphens =re.findall(pattern_successive_hyphens,row[mylist[i]])
					find_hashtag = re.findall(pattern_hashtag,row[mylist[i]])
					find_slash = re.findall(pattern_slash,row[mylist[i]])
					find_space = re.findall(pattern_space,row[mylist[i]])
					find_dot = re.findall(pattern_dot,row[mylist[i]])				

					if len(find_phone) == 1 and len(find_integer) < 10 and not find_string and not find_hashtag and not find_pattern_phone_parantheses and not find_slash and not find_space  :
						
						y = row[mylist[i]].split("-")[0]
						
						for j in range(0,len(zipcodes)-1):						
							if y == zipcodes[j] :
								if(len(y)>3):
									for k in range(0,len(mylist)-1):
										if zipcodes[j+3] == row[mylist[k]]:
											with open('improperData.txt','a') as fp :
												defective_rows+=1
												if defective_rows == 1 :
													global func_count
													func_count += 1	 								
													fp.write("***************************************************************************************\n")
													fp.write("THIS ROW IS PRINTED BECAUSE THE ENTRY IN THE COLUMN ") 
													fp.write(mylist[i])
													fp.write(" OF THE CSV FILE IS POSSIBLY A ZIP CODE WITH A HYPHEN\n")
													fp.write("***************************************************************************************\n")
												fp.write(str(row)+ "\n" + "\n")
												fp.write("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
												fp.write("Zipcode ")
												fp.write(str(row[mylist[i]]) + " ")
												fp.write("belongs to ")
												fp.write(zipcodes[j+1])
												fp.write(" in the state of ")
												fp.write(zipcodes[j+2] + "\n")
												fp.write("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
												fp.write("Defective row No:")
												fp.write(str(defective_rows) + "\n")
												new_row_no_in_original_file=row_no_in_original_file + 1
												fp.write("Row no in original file is ")
												fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
							else :
								pass

					elif len(find_integer) == 5 and not find_phone and not find_hashtag and not find_dot and not find_string and not find_space :
						for j in range(0,len(zipcodes)-1):
							if row[mylist[i]] == zipcodes[j] :
								for k in range(0,len(mylist)-1):
									if zipcodes[j+3] == row[mylist[k]]:							
										defective_rows+=1
										with open('improperData.txt','a') as fp :
											if defective_rows == 1 :											
												func_count += 1										
												fp.write("***************************************************************************************\n")			
												fp.write("THIS ROW IS PRINTED BECAUSE THE ENTRY IN THE COLUMN ") 
												fp.write(mylist[i])
												fp.write(" OF THE CSV FILE IS POSSIBLY A ZIP CODE \n")
												fp.write("***************************************************************************************\n")			
											fp.write(str(row)+ "\n" + "\n")
											fp.write("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
											fp.write("Zipcode ")
											fp.write(str(row[mylist[i]]) + " ")
											fp.write("belongs to ")
											fp.write(zipcodes[j+1])
											fp.write(" in the state of ")
											fp.write(zipcodes[j+2] + "\n")
											fp.write("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
											fp.write("Defective row No:")
											fp.write(str(defective_rows) + "\n")
											new_row_no_in_original_file = row_no_in_original_file + 1
											fp.write("Row no in original file is ")
											fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
							else :
								pass
					elif len(find_integer) == 4 and not find_phone and not find_hashtag and not find_dot and not find_string and not find_space :
						c = "0" + row[mylist[i]]
						for j in range(0,len(zipcodes)-1):
							if c == zipcodes[j] :
								for k in range(0,len(mylist)-1):
									if zipcodes[j+3] == row[mylist[k]]:											
										defective_rows+=1
										with open('improperData.txt','a') as fp :
											if defective_rows == 1 :											
												func_count += 1										
												fp.write("***************************************************************************************\n")			
												fp.write("THIS ROW IS PRINTED BECAUSE THE ENTRY IN THE COLUMN ") 
												fp.write(mylist[i])
												fp.write(" OF THE CSV FILE IS POSSIBLY A ZIP CODE \n")
												fp.write("***************************************************************************************\n")			
											fp.write(str(row)+ "\n" + "\n")
											fp.write("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
											fp.write("Zipcode ")
											fp.write(str(row[mylist[i]]) + " ")
											fp.write("belongs to ")
											fp.write(zipcodes[j+1])
											fp.write(" in the state of ")
											fp.write(zipcodes[j+2] + "\n")
											fp.write("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
											fp.write("Defective row No:")
											fp.write(str(defective_rows) + "\n")
											new_row_no_in_original_file = row_no_in_original_file + 1
											fp.write("Row no in original file is ")
											fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
							else: 
								pass

					else : 
						pass										
		return "inside function print_zip_code "

	def print_duplicate_email_entries(self):
		# print "email_array is :",email_array			
		
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)	
			defective_rows = 0
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        
			duplicate_emails = [k for k,v in Counter(email_array).items() if v>1]							
			# print "*************************************************************"
			# print "Duplicate emails are:",duplicate_emails
			# print "*************************************************************"
			# for i in range(int(globvar),int(globar)):
			if len(duplicate_emails) > 0 :							
				for row in real_data :
					row_no_in_original_file += 1
					for x in range(0,len(duplicate_emails))	:
						if duplicate_emails[x] in str(row) :						
							with open('improperData.txt','a') as fp :							
								defective_rows += 1
								if defective_rows == 1 :
									global func_count
									func_count += 1								
									fp.write("***************************************************************************************\n")
									fp.write("THIS ROW IS PRINTED BECAUSE THE EMAIL ENTRY IN THE COLUMN ")
									fp.write(mylist[i])
									fp.write(" IS DUPLICATED \n")
									fp.write("***************************************************************************************\n")
								fp.write(str(row)+ "\n")
								fp.write("Defective row No:")
								fp.write(str(defective_rows) + "\n")
								new_row_no_in_original_file = row_no_in_original_file + 1
								fp.write("Row no in original file is ")
								fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
		return "inside function  print_duplicate_email_entries"

	def print_improper_email_entries(self):
		return "inside function print_improper_email_entries"
		print_email_with_more_than_one_at()
		print_email_with_space()
		print_email_without_dot()
		print_string_without_email()

	def print_email_with_more_than_one_at(self):
		
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)	
			defective_rows = 0
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        
			global func_count
			for row in real_data :			
				for i in range(int(globvar),int(globar)):	
					find_string = re.findall(pattern_string,row[mylist[i]])			
					find_space = re.findall(pattern_space,row[mylist[i]])
					find_dot = re.findall(pattern_dot,row[mylist[i]])
					find_email = re.findall(pattern_email,row[mylist[i]])
					row_no_in_original_file += 1
					# print "find_email length:", len(find_email)
					if len(find_email) >=2 :
						with open('improperData.txt','a') as fp :
							defective_rows += 1
							if defective_rows == 1 :
								
								func_count += 1								
								fp.write("***************************************************************************************\n")
								fp.write("THIS ROW IS PRINTED BECAUSE @ OCCURS TWICE IN THE COLUMN ")
								fp.write(mylist[i])
								fp.write(" OF THE CSV FILE\n")
								fp.write("***************************************************************************************\n")
							fp.write(str(row)+ "\n")
							fp.write("Defective row No:")
							fp.write(str(defective_rows) + "\n")
							new_row_no_in_original_file = row_no_in_original_file + 1
							fp.write("Row no in original file is ")
							fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
		return "inside function print_email_with_more_than_one_at "	

	def print_email_with_space(self):
		
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)	
			defective_rows = 0
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        
			global func_count
			for row in real_data :			
				for i in range(int(globvar),int(globar)):	
					find_string = re.findall(pattern_string,row[mylist[i]])			
					find_space = re.findall(pattern_space,row[mylist[i]])
					find_dot = re.findall(pattern_dot,row[mylist[i]])
					find_email = re.findall(pattern_email,row[mylist[i]])
					row_no_in_original_file += 1
				if find_string and find_email and find_dot and find_space :
					with open('improperData.txt','a') as fp :
						defective_rows += 1
						if defective_rows == 1 :								
							func_count += 1								
							fp.write("***************************************************************************************\n")
							fp.write("THIS ROW IS PRINTED BECAUSE AN EMPTY SPACE IS PRESENT IN PLACE OF EMAIL IN THE COLUMN ")
							fp.write(mylist[i])
							fp.write(" OF THE CSV FILE\n")
							fp.write("***************************************************************************************\n")
						fp.write(str(row)+ "\n")
						fp.write("Defective row No:")
						fp.write(str(defective_rows) + "\n")
						new_row_no_in_original_file = row_no_in_original_file + 1
						fp.write("Row no in original file is ")
						fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
		return "inside function print_email_with_space "	
					
	def print_email_without_dot(self):
			
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)	
			defective_rows = 0
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        
			global func_count
			for row in real_data :			
				for i in range(int(globvar),int(globar)):	
					find_string = re.findall(pattern_string,row[mylist[i]])			
					find_space = re.findall(pattern_space,row[mylist[i]])
					find_dot = re.findall(pattern_dot,row[mylist[i]])
					find_email = re.findall(pattern_email,row[mylist[i]])
					row_no_in_original_file += 1
				if find_email and not find_dot :
					with open('improperData.txt','a') as fp :
						defective_rows += 1
						if defective_rows == 1 : 
							
							func_count += 1								
							fp.write("***************************************************************************************\n")
							fp.write("THIS ROW IS PRINTED BECAUSE DOT IS NOT PRESENT IN THE COLUMN ")
							fp.write(mylist[i])
							fp.write(" OF THE CSV FILE\n")
							fp.write("***************************************************************************************\n")
						fp.write(str(row)+ "\n")
						fp.write("Defective row No:")
						fp.write(str(defective_rows) + "\n")
						new_row_no_in_original_file = row_no_in_original_file + 1
						fp.write("Row no in original file is ")
						fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
		return "inside function print_email_without_dot"
					
	def print_string_without_email(self):
		
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)	
			defective_rows = 0
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        
			global func_count
			for row in real_data :			
				for i in range(int(globvar),int(globar)):	
					find_string = re.findall(pattern_string,row[mylist[i]])			
					find_space = re.findall(pattern_space,row[mylist[i]])
					find_dot = re.findall(pattern_dot,row[mylist[i]])
					find_email = re.findall(pattern_email,row[mylist[i]])
					row_no_in_original_file += 1
				if find_string and not find_email :
					with open('improperData.txt','a') as fp :
						defective_rows += 1
						if defective_rows == 1 :								
							func_count += 1	 							
							fp.write("***************************************************************************************\n")
							fp.write("THIS ROW IS PRINTED BECAUSE @ IS NOT PRESENT IN THE COLUMN ")
							fp.write(mylist[i])
							fp.write(" OF THE CSV FILE\n")
							fp.write("***************************************************************************************\n")
						fp.write(str(row)+ "\n")
						fp.write("Defective row No:")
						fp.write(str(defective_rows) + "\n")
						new_row_no_in_original_file = row_no_in_original_file + 1
						fp.write("Row no in original file is ")
						fp.write(str(new_row_no_in_original_file)+"\n" + "\n")	
		return "inside function print_string_without_email "	

	def print_string_with_dots_not_email_not_website(self):	
		
		with open(self.filename,'rU') as data :
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			real_data = csv.DictReader(data)	
			defective_rows = 0
			row_no_in_original_file = 0	
			line1=r.next()
			for element in line1:
				mylist = element.split(',')
	        
			global func_count
			for row in real_data :			
				for i in range(int(globvar),int(globar)):	
					find_string = re.findall(pattern_string,row[mylist[i]])			
					find_space = re.findall(pattern_space,row[mylist[i]])
					find_dot = re.findall(pattern_dot,row[mylist[i]])
					find_email = re.findall(pattern_email,row[mylist[i]])
					find_integer = re.findall(pattern_integer,row[mylist[i]])
					find_empty = re.findall(pattern_empty,row[mylist[i]])
					find_no_entry = re.findall(pattern_no_entry,row[mylist[i]])
					find_website = re.findall(pattern_website,row[mylist[i]])
					row_no_in_original_file += 1
	 			if (find_string and find_integer and not find_empty and not find_no_entry  and find_dot and not find_email and not find_website) or (find_string and not find_integer and not find_empty and find_dot and not find_email and not find_website and not find_no_entry):
					with open('improperData.txt','a') as fp :
						defective_rows += 1
						if defective_rows == 1 :								
							func_count += 1	 							
							fp.write("***************************************************************************************\n")
							fp.write("THIS ROW IS PRINTED BECAUSE DOT IS PRESENT IN THE COLUMN ")
							fp.write(mylist[i])
							fp.write(" OF THE CSV FILE\n")
							fp.write("***************************************************************************************\n")
						fp.write(str(row)+ "\n")
						fp.write("Defective row No:")
						fp.write(str(defective_rows) + "\n")
						new_row_no_in_original_file = row_no_in_original_file + 1
						fp.write("Row no in original file is ")
						fp.write(str(new_row_no_in_original_file)+"\n" + "\n")	
		return "inside function print_string_with_dots_not_email_not_website "	

	def startTool(self):
		# if filterr is None:
		# 	self.filename = filename
		with open(self.filename,'rU') as data :						
			r = csv.reader(open(self.filename, "rU"), dialect=csv.excel_tab)
			open('improperData.txt', 'w').close()
			line1=r.next()	
			arrt = []
			for element in line1:
				mylist = element.split(',')			
			real_data = csv.DictReader(data)
			defective_rows = 0
			row_no_in_original_file = 0					
			for row in real_data :					
				row_no_in_original_file += 1	
				if (len(row) != len(mylist)) :			
					defective_rows += 1
					with open('improperData.txt','a') as fp :
						count+=1
						if count == 1:
							# pass
							fp.write("***************************************************************************************\n")
							fp.write("THESE ROWS ARE PRINTED BECAUSE THEY HAVE IMPERFECT COMMAS\n")
							fp.write("***************************************************************************************\n")
						fp.write(str(row)+ "\n")
						fp.write("Defective row No:")
						fp.write(str(defective_rows) + "\n")
						new_row_no_in_original_file = row_no_in_original_file + 1
						fp.write("Row no in original file is ")
						fp.write(str(new_row_no_in_original_file)+"\n" + "\n")
					
				if (len(row) == len(mylist)):
					global counter
					counter+=1
					for i in range(int(globvar),int(globar)):
						a = i
						b = i+1
						regular_expressions(row[mylist[i]])
						purestringFunction(row[mylist[i]])
						stringFunction(row[mylist[i]])
						# pureStringWithSpacesFunction(row[mylist[i]])
						stringWithSpecialCharactersFunction(row[mylist[i]])
						websiteFunction(row[mylist[i]])
						websiteWithoutWWWFunction(row[mylist[i]])
						emailFunction(row[mylist[i]])
						zipcodeFunction(row[mylist[i]])
						phoneFunction(row[mylist[i]])
						integerFunction(row[mylist[i]])
						stateCodeFunction(row[mylist[i]])
						emptyFunction(row[mylist[i]])
						calculation()
			observations()					

								
		return "return from startTool"


InstanceExecuteProgram = ExecuteProgram('mock.csv','2','3')

def printHeader(header):
	# print "Header is",header
	r = csv.reader(open(header, "rU"), dialect=csv.excel_tab)
	line1=r.next()
	global filename
	filename = header			
	for element in line1:
		mylist = element.split(',')	
		str1 = ' '.join(mylist)
		mylister = str1 
	print element
	return "inside printHeader function"

def work_header(filesname,columns) :
	global filename				
	filename = filesname
	global else_count 
	global columnsd
	columnsd = columns
	with open(filename,'rU') as data :
		r = csv.reader(open(filesname, "rU"), dialect=csv.excel_tab)
		line1=r.next()	
		arrt = []
		for element in line1:
			mylist = element.split(',')

	for i in range(0,len(mylist)):
		if columns in mylist[i]:				
			start = mylist.index(columns)
			end = mylist.index(columns)+1				
			# x = ExecuteProgram()			
			InstanceExecuteProgram.fix_file(filename,start,end)
			InstanceExecuteProgram.startTool()
			else_count += 1
	if else_count == 1:
		pass		
	elif else_count == 0:
		print "header is not available"
	return "return from work_header"

def sample_header(filesname,columns) :
	global filename				
	filename = filesname
	global else_count 
	global columnsd
	columnsd = columns
	table=""
	row_count=0
	with open(filename,'rU') as data :
		r = csv.reader(open(filesname, "rU"), dialect=csv.excel_tab)
		line1=r.next()	
		arrt = []
		for element in line1:
			mylist = element.split(',')

	for i in range(0,len(mylist)):
		if columns in mylist[i]:				
			start = mylist.index(columns)
			with open(filename,'rU') as data :
				for line in data :
					row_count+=1
					if row_count <= 11:
						cells = line.split(",")
						table+=cells[start] + "\n"
				print table
			else_count += 1
	if else_count == 1:
		pass
	elif else_count == 0:
		print "header is not available"
	return "return from sample_header function"	

def count_rows(filesname):
	global filename
	row_count = 0
	filename=filesname
	with open(filename,'rU') as data :
		real_data = csv.DictReader(data)
		for row in real_data:
			row_count+=1
	if filename[0]==".":			
		b = filename.split("/")
		print "No of rows in",b[len(b)-1],":",row_count
	else :
		print "No of rows in",filename,":",row_count

	return "return from row count"

def ten_rows(filesname):
	print "\n"
	global filename
	row_count = 0
	stu = ""
	filename=filesname
	with open(filename,'rU') as data :
		for line in data:
			row_count+=1
			if row_count < 11:
				# print line
				stutter =stu.join(line)
				print stutter
	return "return from ten_rows"

def whole_file(filesname):
	global filename				
	filename = filesname

	with open(filename,'rU') as data :
		r = csv.reader(open(filesname, "rU"), dialect=csv.excel_tab)
		line1=r.next()	
		arrt = []
		for element in line1:
			mylist = element.split(',')

		for variable in range(0,len(mylist)):
			start = variable
			end = variable+1				
			# x = ExecuteProgram()							
			InstanceExecuteProgram.fix_file(filename,start,end)
			InstanceExecuteProgram.startTool()		
	
	return "return from whole_file"

@app.command
def columns(filename="something"):
	# x = HeaderPrint()
	printHeader(filename)

@app.command
def sample(filename="filename"):
	# x = printTenRows()
	ten_rows(filename)

@app.command
def sampleHeader(filename="filename",columns="headerName"):
	# x = executeSampleHeader()
	sample_header(filename,columns)


@app.command
def count(filename="filename"):
	print "filename is",filename
	# x = countRows()
	count_rows(filename)

@app.command
def executeColumns(filename="filename",columns="headerName"):
	# x = executerHeader()
	work_header(filename,columns)

@app.command
def execute(filename="filename"):
	# x = executeAll()
	whole_file(filename)

if __name__ == '__main__': 
	app.run()			
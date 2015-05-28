"""
This file classifies the input string into various datatypes depending on the regular_expressions.
"""
import sys
from Reader import *
# bdict={}
# bdict[' valid_verified_zipcode_without_hyphen']=bdict['valid_verified_zipcode_with_two_hyphen']=bdict['zipcode_with_two_not_successive_hyphens']=bdict['valid_verified_zipcode_with_one_hyphen']=bdict['mostly_zipcode_with_one_hyphen']=bdict['mostly_zipcode_without_hyphen']=bdict['mostly_zipcode_with_two_hyphen']=bdict['mostly_zipcode_four_digits']=bdict['phone_no_two_hyphens']=bdict['phone_no_without_hyphen_or_alphabets']=bdict['phone_no_with_alphabets']=bdict['phone_no_with_parantheses']=bdict['phone_no_one_hyphen']=bdict['phone_no_with_only_open_parantheses']=bdict['phone_no_with_only_close_parantheses']=bdict['phone_three_parts_two_hyphens']=bdict['phone_three_parts_one_hyphen_one_parantheses']=bdict['phone_three_parts_plus_one']=bdict['phone_10_digits']=bdict['phone_no_two_hyphens']=bdict['phone_no_without_hyphen_or_alphabets']=bdict['phone_no_with_parantheses']=bdict['phone_no_one_hyphen']=bdict['phone_no_with_only_open_parantheses']=bdict['phone_no_with_only_close_parantheses']=bdict['string_with_space_no_integer']=bdict['string_with_integer_spaces']=bdict['pure_uppercase_string']=bdict['string_with_integer_hyphen']=bdict['string_without_integer_without_spaces']=bdict['string_with_symbol_instead_of_at']=bdict['two_letter_uppercase_string_not_state_code']=bdict['string_first_line_address']=bdict['string_with_dots_not_email_not_website']=bdict['two_letter_lowercase_string_not_state_code']=bdict['string_with_integer_without_spaces']=bdict['website']=bdict['website_without_www']=bdict['string_without_integer_without_spaces']=bdict['string_with_space_no_integer']=bdict['pure_uppercase_string']=bdict['two_letter_uppercase_string_not_state_code']=bdict['email_without_integer']=bdict['state_code']=bdict['string_with_special_characters']=bdict['integer_with_special_characters']=bdict['email_with_integer']=bdict['email_without_integer']=bdict['decimal_integer'] = bdict['integer_with_at'] = bdict['pure_integer'] = 0
# from Displayer import *
# from Calculator import *
import re
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

def purestringFunction(entry,bdict):	
	#regular_expressions(entry)
	if adict['find_string'] and not adict['find_integer'] and not adict['find_empty'] and not adict['find_no_entry'] and not adict['find_email'] and not adict['find_http'] and not adict['find_dot'] and not adict['find_caps'] and adict['find_string'] not in lower_states and adict['find_string'] not in upper_states :		
		global string_without_integer_without_spaces		
		string_without_integer_without_spaces+=1
		bdict['string_without_integer_without_spaces']=string_without_integer_without_spaces
		return "is string without integer and without spaces"
	elif len(adict['find_caps']) == 1 and not adict['find_integer'] and not adict['find_empty'] and not adict['find_no_entry'] and not adict['find_dot'] and not adict['find_slash'] and len(adict['find_string']) > 1:		
		# global string_without_integer_without_spaces
		string_without_integer_without_spaces += 1	
		bdict['string_without_integer_without_spaces']=string_without_integer_without_spaces
		return "is string with single caps with no integer or spaces"
	elif len(adict['find_caps']) == 1 and not adict['find_integer'] and not adict['find_empty'] and not adict['find_no_entry'] and not adict['find_dot'] and not adict['find_slash'] and len(adict['find_string']) == 1:		
		# global string_without_integer_without_spaces
		string_without_integer_without_spaces += 1
		bdict['string_without_integer_without_spaces']=string_without_integer_without_spaces
		return "is string of unit length with single caps"
	elif len(adict['find_string']) > 2 and len(adict['find_caps']) == len(adict['find_string']) and not adict['find_integer'] and not adict['find_empty'] and not adict['find_no_entry'] and not adict['find_dot'] and not adict['find_slash']:		
		global pure_uppercase_string
		pure_uppercase_string+=1
		bdict['pure_uppercase_string']=pure_uppercase_string
		return "is pure uppercase string with more than 2 characters"
	elif adict['find_caps'] and len(adict['find_caps']) != len(adict['find_string']) and not adict['find_integer'] and not adict['find_empty'] and not adict['find_no_entry'] and not adict['find_dot'] and not adict['find_slash'] and not adict['find_space']:
		# global string_without_integer_without_spaces
		string_without_integer_without_spaces += 1
		bdict['string_without_integer_without_spaces']=string_without_integer_without_spaces
		return "is string with capital letters but not state code nor pure uppercase"

def stringFunction(entry,bdict):
	#regular_expressions(entry)
	if (adict['find_string'] and adict['find_integer'] and not adict['find_empty'] and not adict['find_http']  and not adict['find_no_entry'] and adict['find_dot'] and not adict['find_email']) or (adict['find_string'] and not adict['find_integer'] and not adict['find_empty'] and adict['find_dot'] and not adict['find_email'] and not adict['find_website'] and not adict['find_http']) :		
		global string_with_dots_not_email_not_website
		string_with_dots_not_email_not_website += 1
		bdict['string_with_dots_not_email_not_website']=string_with_dots_not_email_not_website
		return "is string with dot but not email"
	elif adict['find_string'] and adict['find_email'] and not adict['find_dot'] :		
		global string_with_symbol_instead_of_at
		string_with_symbol_instead_of_at+=1
		bdict['string_with_symbol_instead_of_at']=string_with_symbol_instead_of_at
		return "is string with @ instead of at"
	elif (len(adict['find_phone']) == 1 and len(adict['find_integer']) != 10 and not adict['find_string'] and adict['find_hashtag']) or (adict['find_string'] and adict['find_integer'] and len(adict['find_space']) > 1 and len(adict['find_string']) > len(adict['find_integer'])):		
		global string_first_line_address
		string_first_line_address += 1
		bdict['string_first_line_address'] = string_first_line_address
		return "is possible line1 of address"

def pureStringWithSpacesFunction(entry,bdict):
	#regular_expressions(entry)
	if (adict['find_space']) and (len(adict['find_string']) + len(adict['find_space']) == len(entry)):		
		global pureStringWithSpaces
		pureStringWithSpaces+=1
		bdict['pureStringWithSpaces'] = pureStringWithSpaces
		return "is a pure string with spaces"
	elif adict['find_space'] and adict['find_string'] and not adict['find_integer'] :		
		global string_with_space_no_integer
		string_with_space_no_integer+=1
		bdict['string_with_space_no_integer']=string_with_space_no_integer
		return "is string with spaces but no integer"

def stringWithSpecialCharactersFunction(entry,bdict):
	#regular_expressions(entry)
	if (adict['find_string'] and adict['find_special_characters']) and (len(adict['find_string'])+ len(adict['find_special_characters']) == len(entry)):
		global string_with_special_characters
		string_with_special_characters+=1
		bdict['string_with_special_characters']=string_with_special_characters
		return "is string with special characters"
def websiteFunction(entry,bdict):
	# regular_expressions(entry)
	if (adict['find_string'] and adict['find_http'] and adict['find_slash'] and adict['find_dot']) or (adict['find_string'] and adict['find_http'] and adict['find_slash'] and adict['find_dot'] and adict['find_integer']):		
		global website
		website+=1
		bdict['website']=website
		return "is possible website with http and slash"
	elif (adict['find_string'] and adict['find_website'] and adict['find_dot'] and adict['find_word_after_dot'] and not adict['find_space']) or (adict['find_string'] and adict['find_word_after_dot'] and adict['find_http'] and adict['find_dot'] and not adict['find_space'] and len(adict['find_dot']) > 1) :
		x = [j for j,val in enumerate(entry) if val=="."]
		if((x[len(x)-1]-x[0]) >= 3) :			
			# global website
			website+=1
			bdict['website']=website
			return "is possible website"
		else :
			return "single character domain name"					

def websiteWithoutWWWFunction(entry,bdict):
	#regular_expressions(entry)
	if adict['find_string'] and adict['find_dot'] and not adict['find_website'] and not adict['find_email'] and  adict['find_word_after_dot'] and not adict['find_slash'] and not adict['find_space'] and not adict['find_hashtag'] and not adict['find_comma'] and (len(adict['find_string']) > 5) and len(adict['find_dot']) > 1 :
		x = [j for j,val in enumerate(entry) if val=="."]
		if((x[len(x)-1]-x[0]) >= 3) :
			global website_without_www
			website_without_www+=1
			bdict['website_without_www']=website_without_www
			return "is possible website but without www (2 dot) and without slashes"
		else :				
			"""
			.......there can't be a single character domain name.
			"""
			global string_with_dots_not_email_not_website
			string_with_dots_not_email_not_website+=1
			bdict['string_with_dots_not_email_not_website']=string_with_dots_not_email_not_website
			return "is string with more than one dot but not website"
	if adict['find_string'] and adict['find_dot'] and not adict['find_website'] and not adict['find_email'] and  adict['find_word_after_dot'] and not adict['find_slash'] and not adict['find_space'] and not adict['find_hashtag'] and not adict['find_comma'] and (len(adict['find_string']) > 5) and len(adict['find_dot']) <= 1 :
		x = [j for j,val in enumerate(entry) if val=="."]
		if(len(entry)-x[0] > 4):				
			# global string_with_dots_not_email_not_website
			string_with_dots_not_email_not_website+=1
			bdict['string_with_dots_not_email_not_website']=string_with_dots_not_email_not_website
			return "is string with one dot but one website"
		else :				
			# global website_without_www
			website_without_www+=1
			bdict['website_without_www']=website_without_www
			return "is possible website but without www (1 dot)"
	if adict['find_string'] and adict['find_slash'] and adict['find_dot'] and not adict['find_website'] and adict['find_word_after_dot'] and not adict['find_space'] and not adict['find_hashtag'] and not adict['find_comma'] and(len(adict['find_string']) > 5):						
		x = [j for j,val in enumerate(entry) if val=="."]
		if((x[len(x)-1]-x[0]) >= 3) :
			return "is possible website but without www and with slashes"
			# global website_without_www
			website_without_www+=1
			bdict['website_without_www']=website_without_www	

def emailFunction(entry,email_array,bdict):	
	#regular_expressions(entry)
	if adict['find_string'] and adict['find_dot'] and adict['find_integer'] and adict['find_email'] and not adict['find_empty'] and not adict['find_no_entry']:		
		global email_with_integer		
		email_with_integer+=1
		bdict['email_with_integer'] = email_with_integer
		email_array.append(entry)
		# return "email_with_integer"
	elif adict['find_string'] and adict['find_email'] and adict['find_dot'] and not adict['find_empty'] and not adict['find_integer'] and not adict['find_no_entry']:		
		global email_without_integer		
		email_without_integer+=1
		bdict['email_without_integer'] = email_without_integer
		email_array.append(entry)	
		# return "is possible email but without integer"
	return email_array

def phoneFunction(entry,bdict):
	#regular_expressions(entry)	
	if adict['find_string'] and adict['find_phone'] and not adict['find_slash']  and adict['find_integer'] and not adict['find_dot'] and len(adict['find_integer']) >= 6 :		
		global phone_no_with_alphabets
		phone_no_with_alphabets+=1
		bdict['phone_no_with_alphabets']=phone_no_with_alphabets
		return "is possible phone no but with alphabets"
	if len(adict['find_phone']) == 1 and len(adict['find_integer']) == 10 and not adict['find_successive_hyphens'] and len(adict['find_integer']) > len(adict['find_string']) and adict['find_slash']:
		global phone_no_one_hyphen
		phone_no_one_hyphen+=1
		bdict['phone_no_one_hyphen']=phone_no_one_hyphen
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
			bdict['phone_three_parts_one_hyphen_one_parantheses']=phone_three_parts_one_hyphen_one_parantheses
			return "is phone no with three parts with one hyphen and a parantheseses"
		else :
			open_brace = [phone for phone,val in enumerate(entry) if val=="("]
			close_brace = [phone for phone,val in enumerate(entry) if val==")"]			
			if open_brace and not close_brace :				
				global phone_no_with_only_open_parantheses
				phone_no_with_only_open_parantheses+=1
				bdict['phone_no_with_only_open_parantheses']=phone_no_with_only_open_parantheses
				return "is phone no with only open parantheses"
			if close_brace and not open_brace :				
				global phone_no_with_only_close_parantheses
				phone_no_with_only_close_parantheses+=1
				bdict['phone_no_with_only_close_parantheses']=phone_no_with_only_close_parantheses
				return "is phone no with only close parantheses"
	if adict['find_pattern_phone_parantheses'] and not adict['find_website'] and not adict['find_string'] and len(adict['find_integer']) == 10 and not adict['find_pattern_phone_10_digits'] and not adict['find_phone_three_parts_two_hyphens'] and not adict['find_phone_three_parts_one_hyphen_one_parantheses'] and not adict['find_pattern_phone_three_parts_plus_one'] and not adict['find_pattern_phone_11_digits'] :		
		global phone_no_with_parantheses
		phone_no_with_parantheses+=1
		bdict['phone_no_with_parantheses']=phone_no_with_parantheses
		return "is phone no with parantheses"
	if adict['find_phone_three_parts_two_hyphens'] and not adict['find_string'] and len(adict['find_integer']) == 10 :		
		global phone_three_parts_two_hyphens
		phone_three_parts_two_hyphens+=1
		bdict['phone_three_parts_two_hyphens']=phone_three_parts_two_hyphens
		return  "is phone with two hyphens"
	if adict['find_phone_three_parts_two_hyphens'] and not adict['find_string'] and len(adict['find_integer']) >= 10 :
		global pure_integer
		pure_integer+=1
		# print "pure integer entry for",entry
		bdict['pure_integer']=pure_integer
		return "more than 10 integers and thus not a phone no"	

def zipcodeFunction(entry,bdict):
	#regular_expressions(entry)
	single_hyphen_split = entry.split("-")
	double_hyphen_split = entry.split("--")
	if adict['find_integer'] and adict['find_phone'] and adict['find_zipcode_one_hyphen'] and single_hyphen_split[0] in zipcodes :
		# zipcode_array.append(entry)
		global mostly_zipcode_with_one_hyphen
		mostly_zipcode_with_one_hyphen += 1
		bdict['mostly_zipcode_without_hyphen']=mostly_zipcode_without_hyphen
		return  "is Most probably a zipcode with one hyphen"
	if adict['find_integer'] and adict['find_phone'] and adict['find_zipcode_one_hyphen'] and single_hyphen_split[0] not in zipcodes :				
		global pure_integer
		pure_integer += 1
		# print "pure integfffer entry for",entry
		bdict['pure_integer']=pure_integer
		return  "has one hyphen but is not a zipcode"
	if adict['find_integer'] and adict['find_phone'] and adict['find_zipcode_two_hyphen'] and double_hyphen_split[0] in zipcodes :
		global mostly_zipcode_with_two_hyphen
		mostly_zipcode_with_two_hyphen += 1
		bdict['mostly_zipcode_with_two_hyphen']=mostly_zipcode_with_two_hyphen
		return  "is Most probably a zipcode with two hyphen"
	if adict['find_integer'] and adict['find_phone'] and adict['find_zipcode_two_hyphen'] and double_hyphen_split[0] not in zipcodes :
		# global pure_integer
		pure_integer += 1
		# print "pure integer enffftry for",entry
		bdict['pure_integer']=pure_integer
		return  "has two hyphen but is not a zipcode"
	if len(adict['find_phone']) == 2 and len(adict['find_integer']) != 10 and not adict['find_successive_hyphens'] and not adict['find_string'] and len(single_hyphen_split[0])>3 and single_hyphen_split[0] in zipcodes :					
		global zipcode_with_two_not_successive_hyphens
		zipcode_with_two_not_successive_hyphens+=1
		bdict['zipcode_with_two_not_successive_hyphens']=zipcode_with_two_not_successive_hyphens
		return  "is possible zip codes but with two but not succesive hyphens"
	if len(adict['find_phone']) == 2 and len(adict['find_integer']) != 10 and not adict['find_successive_hyphens'] and not adict['find_string'] and len(single_hyphen_split[0])>3 and single_hyphen_split[0] not in zipcodes :
		global integer_seperated_by_hyphen_not_zip_or_phone
		integer_seperated_by_hyphen_not_zip_or_phone+=1
		bdict['integer_seperated_by_hyphen_not_zip_or_phone'] =integer_seperated_by_hyphen_not_zip_or_phone
		return "integer with two hyphens but not zipcode or phone"
	if len(adict['find_phone']) == 2 and len(adict['find_integer']) != 10 and not adict['find_successive_hyphens'] and not adict['find_string'] and len(single_hyphen_split[0])<=3 :
		# global integer_seperated_by_hyphen_not_zip_or_phone
		integer_seperated_by_hyphen_not_zip_or_phone+=1
		bdict['integer_seperated_by_hyphen_not_zip_or_phone'] =integer_seperated_by_hyphen_not_zip_or_phone
		return "is integers separated by hyphen but not zipcode or phone number"

def integerFunction(entry,bdict):	
	#regular_expressions(entry)
	if adict['find_integer'] and adict['find_at_the_rate'] and not adict['find_dot'] and not adict['find_string']:
		global integer_with_at
		integer_with_at += 1
		bdict['integer_with_at']=integer_with_at
		return "is integer with @"
	if adict['find_string'] and not adict['find_space'] and adict['find_integer'] and not adict['find_email'] and not adict['find_website'] and not adict['find_dot'] and not adict['find_phone']:		
		global string_with_integer_without_spaces
		string_with_integer_without_spaces+=1
		bdict['string_with_integer_without_spaces']=string_with_integer_without_spaces
		return "is string with integer without spaces"
	if adict['find_string'] and adict['find_space'] and adict['find_integer'] and not adict['find_email'] and not adict['find_website'] and not adict['find_dot'] and not adict['find_phone']:		
		global string_with_integer_spaces
		string_with_integer_spaces+=1
		bdict['string_with_integer_spaces']=string_with_integer_spaces
		return "is string with integer and spaces"
	if adict['find_string'] and adict['find_phone'] and adict['find_integer'] and not adict['find_dot'] and len(adict['find_integer']) < 6 and adict['find_space']:		
		global string_with_integer_hyphen
		string_with_integer_hyphen += 1
		bdict['string_with_integer_hyphen'] = string_with_integer_hyphen
		return "is Mixture of string integer and hyphen and spaces"
	if adict['find_string'] and adict['find_phone'] and adict['find_integer'] and not adict['find_dot'] and len(adict['find_integer']) < 6 and not adict['find_space']:		
		# global string_with_integer_hyphen
		string_with_integer_hyphen += 1
		bdict['string_with_integer_hyphen'] = string_with_integer_hyphen
		return "is Mixture of string integer and hyphen but not spaces"	
	if adict['find_integer'] and not adict['find_phone'] and (adict['find_zipcode_without_hyphen']):
		if entry in zipcodes :				
			global mostly_zipcode_without_hyphen
			mostly_zipcode_without_hyphen += 1
			bdict['mostly_zipcode_without_hyphen']=mostly_zipcode_without_hyphen
			return  "is most probably a zipcode (without hyphen)" 
		else :
			global pure_integer						
			pure_integer += 1
			# print "pure integer entrffffffsdy for",entry			
			bdict['pure_integer']=pure_integer
			zipcode_array.append(entry)
			return  "is not a Zipcode"
	if adict['find_integer'] and not adict['find_phone'] and (adict['find_zipcode_four_digits']):
		c = "0" + entry
		if c in zipcodes :				
			global mostly_zipcode_four_digits
			mostly_zipcode_four_digits += 1
			bdict['mostly_zipcode_four_digits']=mostly_zipcode_four_digits
			return  "is most probably a zipcode (four digits)" 
		else :				
			# global pure_integer
			pure_integer += 1
			# print "purfsdfsde integer entry for",entry			
			bdict['pure_integer']=pure_integer
			return  "is a four digit integer"
	if adict['find_integer'] and not adict['find_phone'] and  not adict['find_zipcode_without_hyphen'] and not adict['find_zipcode_four_digits'] and not adict['find_string'] and adict['find_dot']:			
		global decimal_integer
		decimal_integer += 1
		bdict['decimal_integer'] = decimal_integer
		global decimal_integer_lengths
		decimal_integer_lengths.append(len(adict['find_dot']))			
		return "is Integer with decimals"
	if adict['find_integer'] and not adict['find_phone'] and  not adict['find_zipcode_without_hyphen'] and not adict['find_zipcode_four_digits'] and not adict['find_string'] and not adict['find_dot'] and not adict['find_pattern_phone_10_digits'] and not adict['find_phone_three_parts_two_hyphens'] and not adict['find_phone_three_parts_one_hyphen_one_parantheses'] and not adict['find_pattern_phone_three_parts_plus_one'] and not adict['find_pattern_phone_11_digits'] and not adict['find_special_characters'] and not adict['find_email'] :		
		# global pure_integer
		pure_integer += 1
		# print "pure integer entry forfsdfsdfsd",entry
		bdict['pure_integer'] = pure_integer
		return "is Pure integer"
	if adict['find_integer'] and not adict['find_phone'] and  not adict['find_zipcode_without_hyphen'] and not adict['find_zipcode_four_digits'] and not adict['find_string'] and not adict['find_dot'] and adict['find_pattern_phone_10_digits'] and not adict['find_pattern_phone_11_digits'] and not adict['find_string']:	
		global phone_10_digits
		phone_10_digits += 1
		bdict['phone_10_digits']=phone_10_digits
		return "is 10 digit phone no"
	if adict['find_integer'] and not adict['find_phone'] and  adict['find_pattern_phone_three_parts_plus_one'] and not adict['find_string'] :	
		global phone_three_parts_plus_one
		phone_three_parts_plus_one+=1
		bdict['phone_three_parts_plus_one']=phone_three_parts_plus_one
		return "is phone with four parts containing three spaces and +1"
	if adict['find_integer'] and not adict['find_phone'] and  adict['find_pattern_phone_11_digits'] and not adict['find_string'] and entry[0]=="1" :
		if entry[0]=="1":				
			global phone_11_digits
			phone_11_digits+=1
			bdict['phone_11_digits']=phone_11_digits
		return  "is 11 digit phone no i.e starts with 1 followed by 10 digits"
	if adict['find_integer'] and not adict['find_phone'] and  adict['find_pattern_phone_11_digits'] and not adict['find_string'] and entry[0]!="1" :
		# global pure_integer
		pure_integer+=1
		# print "pudsaasddasre integer entry for",entry
		bdict['pure_integer']=pure_integer
		return "11 digit number but not phone no"		
	if adict['find_decimal'] and adict['find_phone'] and not adict['find_string'] and entry[0] == "-" :		
		# global decimal_integer
		decimal_integer += 1
		bdict['decimal_integer']=decimal_integer
		decimal_integer_lengths.append(len(adict['find_dot']))
		return "is Negative integer with decimals"
	if adict['find_integer'] and not adict['find_dot'] and adict['find_phone'] and not adict['find_string'] and entry[0] == "-" and not adict['find_special_characters']:		
		# global pure_integer
		pure_integer += 1
		# print "pure integer entry fsfdfsdfsdfsdor",entry
		bdict['pure_integer']=pure_integer
		return "is Negative integer without decimals"
	if adict['find_integer'] and not adict['find_dot'] and adict['find_phone'] and not adict['find_string'] and entry[0] == "-" and adict['find_special_characters']:		
		pure_integer+=1
		# print "pudasdasdasdre integer entry for",entry
		bdict['pure_integer']=pure_integer
		return "is Negative integer with special characters"
	if adict['find_integer'] and adict['find_dot'] and adict['find_phone'] and not adict['find_string'] and entry[0] == "-" and not adict['find_decimal']:		
		decimal_integer+=1
		return "is decimal integer with misplaced dot"
	if adict['find_integer'] and adict['find_special_characters'] and (len(adict['find_integer'])+len(adict['find_special_characters']) == len(entry)):		
		global integer_with_special_characters
		integer_with_special_characters+=1
		bdict['integer_with_special_characters']=integer_with_special_characters
		return "is integer with special characters"


def stateCodeFunction(entry,bdict):
	#regular_expressions(entry)
	matching = [s for s in states if entry == s]
	matching_lower = [s for s in lower_states if entry == s]
	matching_upper = [s for s in upper_states if entry == s]

	if len(adict['find_caps']) and len((adict['find_string'])) == 2 and not adict['find_integer'] and not adict['find_empty'] and not adict['find_no_entry']  and not adict['find_dot'] and not adict['find_slash'] and not adict['find_small'] and matching:		
			global state_code 
			state_code+=1
			bdict['state_code']=state_code
			return "is possible state code"
	if len(adict['find_caps']) and len((adict['find_string'])) == 2 and not adict['find_integer'] and not adict['find_empty'] and not adict['find_no_entry']  and not adict['find_dot'] and not adict['find_slash'] and not adict['find_small'] and not matching:
			global two_letter_uppercase_string_not_state_code
			two_letter_uppercase_string_not_state_code += 1
			bdict['two_letter_uppercase_string_not_state_code']=two_letter_uppercase_string_not_state_code
			return "is two lettered uppercase string not state code"
	if len(adict['find_small']) and len((adict['find_string'])) == 2 and not adict['find_integer'] and not adict['find_empty'] and not adict['find_dot'] and not adict['find_no_entry'] and not adict['find_slash'] and matching_lower:
			# global state_code
			state_code+=1
			bdict['state_code']=state_code
			return "is possible state code in lowercase"
	if len(adict['find_small']) and len((adict['find_string'])) == 2 and not adict['find_integer'] and not adict['find_empty'] and not adict['find_dot'] and not adict['find_no_entry'] and not adict['find_slash'] and not matching_lower:	
			global two_letter_lowercase_string_not_state_code
			two_letter_lowercase_string_not_state_code += 1
			bdict['two_letter_lowercase_string_not_state_code']=two_letter_lowercase_string_not_state_code
			return "is two lettered lowercase string not state code"
	if len(adict['find_small']) and len((adict['find_string'])) > 2 and not adict['find_integer'] and not adict['find_empty'] and not adict['find_dot'] and not adict['find_no_entry'] and not adict['find_slash'] and matching_lower:
			# global state_code
			state_code+=1
			bdict['state_code']=state_code
			return "is possible state name in lowercase"
	if len(adict['find_small']) == len(adict['find_string'])and len(adict['find_small']) > 2 and len(adict['find_string']) > 2 and not adict['find_integer'] and not adict['find_empty'] and not adict['find_dot'] and not adict['find_no_entry'] and not adict['find_slash'] and not matching_lower and not adict['find_special_characters']:		
			# global two_letter_lowercase_string_not_state_code
			two_letter_lowercase_string_not_state_code += 1			
			bdict['two_letter_lowercase_string_not_state_code']=two_letter_lowercase_string_not_state_code
			return "is not state name"
	if len(adict['find_caps']) == len(adict['find_string']) and len(adict['find_string']) > 2 and not adict['find_integer'] and not adict['find_empty'] and not adict['find_no_entry'] and not adict['find_dot'] and not adict['find_slash'] and matching_upper:		
			# global state_code
			state_code+=1
			bdict['state_code']=state_code
			return "is possible state name in capital letters"
	if len(adict['find_caps']) == len(adict['find_string']) and len(adict['find_string']) > 2 and not adict['find_integer'] and not adict['find_empty'] and not adict['find_no_entry'] and not adict['find_dot'] and not adict['find_slash'] and not matching_upper:		
			global pure_uppercase_string
			pure_uppercase_string += 1
			bdict['pure_uppercase_string']=pure_uppercase_string
			return "is uppercase string"

def emptyFunction(entry,bdict):
	#regular_expressions(entry)
	if adict['find_empty'] :			
		global empty
		empty+=1
		return "is empty"


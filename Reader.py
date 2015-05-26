#!/usr/bin/env python
"""
This file basically contains only the global data of the whole tool
"""


# from Classifier import *
# from Displayer import *
# from Calculator import *

import re,csv,sys,requests,compago
from collections import Counter
app = compago.Application()
two_letter_lowercase_string_not_state_code = string_with_integer_spaces = email = website = string_with_space_no_integer = phone_no_with_alphabets = website_without_www = state_code = pure_uppercase_string = phone_no_two_hyphens = phone_no_with_parantheses = phone_no_without_hyphen_or_alphabets = valid_verified_zipcode_without_hyphen = empty = valid_verified_zipcode_with_two_hyphen = string_with_integer_without_spaces = pure_integer =  valid_verified_zipcode_with_one_hyphen = two_letter_uppercase_string_not_state_code = zipcode_with_two_not_successive_hyphens = string_without_integer_without_spaces = string_with_symbol_instead_of_at = string_first_line_address = integer_seperated_by_hyphen_not_zip_or_phone =  phone_no_one_hyphen = phone_no_with_only_open_parantheses = phone_no_with_only_close_parantheses = uncertain_entries = string_with_dots_not_email_not_website = mostly_zipcode_with_one_hyphen = mostly_zipcode_without_hyphen = mostly_zipcode_with_two_hyphen = mostly_zipcode_four_digits = requests_made = decimal_integer = string_with_integer_hyphen = string_with_special_characters = integer_with_special_characters = email_with_integer = email_without_integer = print_empty_count = string_dots_no_email_or_website = special_characters_print =email_dominant_column= phone_three_parts_two_hyphens= phone_three_parts_one_hyphen_one_parantheses=phone_three_parts_plus_one=phone_11_digits=phone_10_digits=row_count= else_count = func_count = local_count = count = counter = globvar = purestring = pureStringWithSpaces = 0
states = [ "AK","Alaska","AL","Alabama","AR","Arkansas","AS","American Samoa","AZ","Arizona","CA","California","CO","Colorado","CT","Connecticut","DC","District of Columbia","DE","Delaware","FL","Florida","GA","Georgia","GU","Guam","HI","Hawaii","IA","Iowa","ID","Idaho","IL","Illinois","IN","Indiana","KS","Kansas","KY","Kentucky","LA","Louisiana","MA","Massachusetts","MD","Maryland","ME","Maine","MI","Michigan","MN","Minnesota","MO","Missouri","MS","Mississippi","MT","Montana","NC","North Carolina","ND","North Dakota","NE","Nebraska","NH","New Hampshire","NJ","New Jersey","NM","New Mexico","NV","Nevada","NY","New York","OH","Ohio","OK","Oklahoma","OR","Oregon","PA","Pennsylvania","PR","Puerto Rico","RI","Rhode Island","SC","South Carolina","SD","South Dakota","TN","Tennessee","TX","Texas","UT","Utah","VA","Virginia","VI","Virgin Islands","VT","Vermont","WA","Washington","WI","Wisconsin","WV","West Virginia","WY","Wyoming" ]		
state_code_array = ["AK","AL","AR","AS","AZ","CA","CO","CT","DC","DE","FL","GA","GU","HI","IA","ID","IL","IN","KS","KY","LA","MA","MD","ME","MI","MN","MO","MS","MT","NC","ND","NE","NH","NJ","NM","NV","NY","OH","OK","OR","PA","PR","RI","SC","SD","TN","TX","UT","VA","VI","VT","WA","WI","WV","WY"]
states_and_cities = ["Wyoming","Minnesota","California","Georgia","Kansas","Vermont","Indiana","Pennsylvania","Alabama","New York","Florida","Ohio","Texas","Maryland","Louisiana","Missouri","WY","MN","CA","GA","KS","VT","IN","PA","AL","NY","FL","OH","TX","MD","LA"]
lower_states = upper_states =  arr=zipcode_array = email_array = decimal_integer_lengths= []
counter_decimal_integer = Counter(decimal_integer_lengths)
for t in range(0,len(states)-1):
	lower_states.append(states[t].lower())
for t in range(0,len(states)-1):
	upper_states.append(states[t].upper()) 
globar = 1
adict={}
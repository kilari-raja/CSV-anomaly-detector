import re
pattern_string = re.compile("[a-zA-Z]")
pattern_integer = re.compile("[0-9]")
pattern_email = re.compile("[\w+|\W+]@[\w+|\W+]")
pattern_website = re.compile("www+|WWW+")
pattern_dot = re.compile("[.]")
pattern_space = re.compile("[\w+|\W+]\s[\w+|\W+]")
pattern_special_characters = re.compile("[!|$|\\\\|/|%|^|+|=|_|*|}|~|\[|\]|:|?|`|<|>|{]")
pattern_phone = re.compile("-")



def only_string(x):
    find_string = re.findall(pattern_string,x)
    return len(find_string)
def string_with_spaces(x):
	find_space = re.findall(pattern_space,x)
	find_string = re.findall(pattern_string,x)
	return len(find_string) + len(find_space)
def string_with_spaces_and_integers(x):
	find_space = re.findall(pattern_space,x)
	find_string = re.findall(pattern_string,x)
	find_integer = re.findall(pattern_integer,x)
	return len(find_string) + len(find_space) + len(find_integer)
def string_with_integer_without_spaces(x):
	find_string = re.findall(pattern_string,x)
	find_integer = re.findall(pattern_integer,x)
	return len(find_string) + len(find_integer)
def string_with_dot(x):
	find_dot = re.findall(pattern_dot,x)
	find_string = re.findall(pattern_string,x)
	return len(find_string) + len(find_dot)
def only_integer(x):
    find_integer = re.findall(pattern_integer,x)
    return len(find_integer)
def integer_with_spaces(x):
	find_space = re.findall(pattern_space,x)
	find_integer = re.findall(pattern_integer,x)
	return len(find_integer) + len(find_space)
def email(x):
	find_email = re.findall(pattern_email,x)
	find_dot = re.findall(pattern_dot,x)
	return len(find_email) + len(find_dot)
def website(x):
	find_website = re.findall(pattern_website,x)
	find_dot = re.findall(pattern_dot,x)
	return len(find_website) + len(find_dot)
def decimal_integers(x):
	find_dot = re.findall(pattern_dot,x)
	find_integer = re.findall(pattern_integer,x)
	return len(find_integer) + len(find_dot)
def decimal_integers_with_spaces(x):
	find_dot = re.findall(pattern_dot,x)
	find_integer = re.findall(pattern_integer,x)
	find_space = re.findall(pattern_space,x)
	return len(find_integer) + len(find_dot) + len(find_space)
def decimal_integers_with_string(x):
	find_dot = re.findall(pattern_dot,x)
	find_integer = re.findall(pattern_integer,x)
	find_string = re.findall(pattern_string,x)
	return len(find_integer) + len(find_dot) + len(find_string)
def string_with_special_characters(x):
	find_special_characters=re.findall(pattern_special_characters,x)
	find_string = re.findall(pattern_string,x)
	find_phone = re.findall(pattern_phone,x)
	return len(find_string) + len(find_special_characters) + len(find_phone)
def integer_with_special_characters(x):
	find_special_characters=re.findall(pattern_special_characters,x)
	find_integer = re.findall(pattern_string,x)
	find_phone = re.findall(pattern_phone,x)
	return len(find_integer) + len(find_special_characters) + len(find_phone)


def test_string():    
    assert only_string("raj") == 3
    assert string_with_spaces("raj kumar") == 9
    assert string_with_spaces_and_integers("raj kumar 92") == 12
    assert string_with_integer_without_spaces("raj492") == 6
    assert string_with_dot("raj.kumar") == 9
    assert string_with_special_characters("raj_`!$^{}[]k")==13
    assert string_with_special_characters("raj\<>|!=k")==10
    assert string_with_special_characters("raj-k")==5
    


def test_integer():
    assert only_integer("123") == 3
    assert integer_with_spaces("44 92")== 5
    assert decimal_integers("44.92")== 5
    assert decimal_integers_with_spaces("4 4.92")== 6
    assert decimal_integers_with_string("4.84r")== 5
    # assert integer_with_special_characters("1")==1

def test_email():
	assert email("raj04@gmail.com") == 2
	assert email("raj04@gmailcom") == 1
	assert email("raj04gmail.com") == 1
	assert email("raj04gmailcom") == 0

def test_website():
	assert website("www.raj.com") ==3
	assert website("ww.raj.com") ==2
	assert website("raj.com") ==1
	assert website("ww.raj") ==1
	assert website("wwraj") ==0
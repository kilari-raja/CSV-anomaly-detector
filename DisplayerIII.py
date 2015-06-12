""" This file contains the function that prints improper data back to the user."""

from regex import *
# from Reader import *
from commonFunc import print_in_improperTxt, correct_place
global print_array


def get_mylist(filesname):
    r = csv.reader(open(filesname, "rU"), dialect=csv.excel_tab)
    line1 = r.next()
    for element in line1:
        mylist = element.split(',')
    return mylist


def get_real_data(filesname):
    rows = []
    with open(filesname, 'rU')as data:
        real_data = csv.reader(data)
        for row in real_data:
            rows.append(row)
    return rows


def print_uppercase_entries(filesname, start, end, datum, print_array):
    defective_rows = row_no_in_original_file = func_count = funct_count = 0
    for i in range(1, len(datum)):
        find_uppercase = re.findall(pattern_uppercase, datum[i][start])
        row_no_in_original_file += 1
        if find_uppercase:
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              29, print_array)
    return print_array


def print_empty_entries(filesname, start, end, datum, print_array):
    defective_rows = row_no_in_original_file = func_count = funct_count = 0
    for i in range(1, len(datum)):
        find_empty = re.findall(pattern_empty, datum[i][start])
        find_no_entry = re.findall(pattern_no_entry, datum[i][start])
        row_no_in_original_file += 1
        if find_empty or find_no_entry:
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              6, print_array)
    return print_array


def print_string_entries(filesname, start, end, datum, print_array):
    defective_rows = row_no_in_original_file = func_count = funct_count = 0
    for i in range(1, len(datum)):
        find_string = re.findall(pattern_string, datum[i][start])
        row_no_in_original_file += 1
        if find_string:
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              26, print_array)
    return print_array


def print_string_only_entries(filesname, start, end, datum, print_array):
    defective_rows = row_no_in_original_file = func_count = funct_count = 0
    for i in range(1, len(datum)):
        find_string = re.findall(pattern_string, datum[i][start])
        row_no_in_original_file += 1
        if find_string and len(find_string) == len(datum[i][start]):
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              21, print_array)
    return print_array


def print_string_with_integer_and_space_entries(filesname, start, end, datum, print_array):
    defective_rows = row_no_in_original_file = func_count = funct_count = 0
    for i in range(1, len(datum)):
        find_string = re.findall(pattern_string, datum[i][start])
        find_integer = re.findall(pattern_integer, datum[i][start])
        find_space = re.findall(pattern_space, datum[i][start])
        row_no_in_original_file += 1
        if find_string and find_integer and find_space:
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              28, print_array)
    return print_array


def print_integer_entries(filesname, start, end, datum, print_array):
    defective_rows = row_no_in_original_file = func_count = funct_count = 0
    for i in range(1, len(datum)):
        find_integer = re.findall(pattern_integer, datum[i][start])
        row_no_in_original_file += 1
        if find_integer and len(find_integer) != len(datum[i][start]):
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              11, print_array)
    return print_array


def print_integer_only_entries(filesname, start, end, datum, print_array):
    defective_rows = row_no_in_original_file = func_count = funct_count = 0
    for i in range(1, len(datum)):
        find_integer = re.findall(pattern_integer, datum[i][start])
        find_string = re.findall(pattern_string, datum[i][start])
        row_no_in_original_file += 1
        if find_integer and not find_string and len(find_integer) == len(datum[i][start]):
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              13, print_array)
    return print_array


def print_improper_decimal_integers(filesname, start, end, datum, print_array):
    defective_rows = row_no_in_original_file = func_count = funct_count = 0
    counter_decimal_integer = Counter(decimal_integer_lengths)
    for i in range(1, len(datum)):
        find_integer = re.findall(pattern_integer, datum[i][start])
        find_string = re.findall(pattern_string, datum[i][start])
        find_dot = re.findall(pattern_dot, datum[i][start])
        row_no_in_original_file += 1
        if find_integer and not find_string and len(decimal_integer_lengths) > 0 and (
        len(find_dot) != counter_decimal_integer.most_common(1)[0][0]):
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              9, print_array)
    return print_array
# def improper_integer_entries(filesname, start, end, datum, print_array):
#     defective_rows = row_no_in_original_file = func_count = funct_count = 0
#     for i in range(1, len(datum)):
#         find_phone = re.findall(pattern_phone, datum[i][start])
#         find_integer = re.findall(pattern_integer, datum[i][start])
#         find_string = re.findall(pattern_string, datum[i][start])
#         find_hashtag = re.findall(pattern_hashtag, datum[i][start])
#         find_pattern_phone_parantheses = re.findall(patten_phone_parantheses, datum[i][start])
#         find_slash = re.findall(pattern_slash, datum[i][start])
#         row_no_in_original_file += 1
#         if len(find_phone) == 1and len(find_integer)!= 10 and not find_string and not find_hashtag and not find_pattern_phone_parantheses and not find_slash:
#             defective_rows += 1
#             funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              # row_no_in_original_file, func_count, i,
                                              # 10, print_array)
#     return print_array


def print_email_entries(filesname, start, end, datum, print_array):
    defective_rows = row_no_in_original_file = func_count = funct_count = 0
    for i in range(1, len(datum)):
        find_email = re.findall(pattern_email, datum[i][start])
        find_dot = re.findall(pattern_dot, datum[i][start])
        find_space = re.findall(pattern_space, datum[i][start])
        row_no_in_original_file += 1
        if find_email and find_dot and not find_space:
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              5, print_array)
    return print_array


def print_website_entries(filesname, start, end, datum, print_array):
    defective_rows = row_no_in_original_file = func_count = funct_count = 0
    for i in range(1, len(datum)):
        find_website = re.findall(pattern_website, datum[i][start])
        find_dot = re.findall(pattern_dot, datum[i][start])
        row_no_in_original_file += 1
        if find_website and find_dot:
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              32, print_array)
    return print_array


def print_special_characters(filesname, start, end, datum, print_array):
    defective_rows = row_no_in_original_file = func_count = funct_count = 0
    for i in range(1, len(datum)):
        find_special_characters = re.findall(pattern_special_characters, datum[i][start])
        row_no_in_original_file += 1
        if find_special_characters:
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              23, print_array)
    return print_array


def print_special_characters_phone(filesname, start, end, datum, print_array):
    defective_rows = row_no_in_original_file = func_count = funct_count = 0
    for i in range(1, len(datum)):
        find_special_characters_phone = re.findall(pattern_special_characters_phone, datum[i][start])
        row_no_in_original_file += 1
        if find_special_characters_phone:
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              24, print_array)
    return print_array


def print_special_characters_website(filesname, start, end, datum, print_array):
    defective_rows = row_no_in_original_file = func_count = funct_count = 0
    for i in range(1, len(datum)):
        find_special_characters_website = re.findall(pattern_special_characters_website, datum[i][start])
        row_no_in_original_file += 1
        if find_special_characters_website:
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              25, print_array)
    return print_array


def print_hyphen(filesname, start, end, datum, print_array):
    defective_rows = row_no_in_original_file = func_count = funct_count = 0
    for i in range(1, len(datum)):
        find_phone = re.findall(pattern_phone, datum[i][start])
        row_no_in_original_file += 1
        if find_phone:
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              8, print_array)
    return print_array


def print_space_entries(filesname, start, end, datum, print_array):
    defective_rows = row_no_in_original_file = func_count = funct_count = 0
    for i in range(1, len(datum)):
        find_space = re.findall(pattern_space, datum[i][start])
        find_string = re.findall(pattern_string, datum[i][start])
        find_integer = re.findall(pattern_integer, datum[i][start])
        row_no_in_original_file += 1
        if (find_string and find_space)or (find_integer and find_space):
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              22, print_array)
    return print_array


def print_no_dots(filesname, start, end, datum, print_array):
    defective_rows = row_no_in_original_file = func_count = funct_count = 0
    for i in range(1, len(datum)):
        find_string = re.findall(pattern_string, datum[i][start])
        find_dot = re.findall(pattern_dot, datum[i][start])
        row_no_in_original_file += 1
        if (find_string and not find_dot):
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              18, print_array)
    return print_array


def print_pure_integer_not_zipcode(filesname, start, end, datum, print_array):
    defective_rows = row_no_in_original_file = func_count = funct_count = 0
    for i in range(1, len(datum)):
        find_integer = re.findall(pattern_integer, datum[i][start])
        find_string = re.findall(pattern_string, datum[i][start])
        find_phone = re.findall(pattern_phone, datum[i][start])
        find_zipcode_without_hyphen = re.findall(pattern_zipcode_without_hyphen, datum[i][start])
        find_zipcode_four_digits = re.findall(patter_zipcode_four_digits, datum[i][start])
        find_dot = re.findall(pattern_dot, datum[i][start])
        row_no_in_original_file += 1
        if find_integer and not find_phone and not find_zipcode_without_hyphen and (not 
            find_zipcode_four_digits and not find_string and not find_dot):
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              12, print_array)
    return print_array


def print_integer_more_than_string(filesname, start, end, datum, print_array):
    defective_rows = row_no_in_original_file = func_count = funct_count = 0
    for i in range(1, len(datum)):
        find_integer = re.findall(pattern_integer, datum[i][start])
        find_string = re.findall(pattern_string, datum[i][start])
        find_website = re.findall(pattern_website, datum[i][start])
        row_no_in_original_file += 1
        if (len(find_integer) > len(find_string)and not find_website):
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              15, print_array)
    return print_array


def print_string_more_than_integer(filesname, start, end, datum, print_array):
    defective_rows = row_no_in_original_file = func_count = funct_count = 0
    for i in range(1, len(datum)):
        find_integer = re.findall(pattern_integer, datum[i][start])
        find_string = re.findall(pattern_string, datum[i][start])
        row_no_in_original_file += 1
        if (len(find_string) > len(find_integer)):
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              16, print_array)
    return print_array


def print_not_state_code(filesname, start, end, datum, print_array):
    defective_rows = row_no_in_original_file = func_count = funct_count = 0
    for i in range(1, len(datum)):
        row_no_in_original_file += 1
        if (datum[i][start] not in states)and (datum[i][start] not in lower_states)and (
         (datum[i][start] not in upper_states)and (datum[i][start] != " "))and (
          (datum[i][start] != "")):
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              17, print_array)
    return print_array


def print_symbols(filesname, start, end, datum, print_array):
    defective_rows = row_no_in_original_file = func_count = funct_count = 0
    for i in range(1, len(datum)):
        row_no_in_original_file += 1
        find_string = re.findall(pattern_string, datum[i][start])
        find_at_the_rate = re.findall(pattern_at_the_rate, datum[i][start])
        find_dot = re.findall(pattern_dot, datum[i][start])
        find_string = re.findall(pattern_string, datum[i][start])
        find_hashtag = re.findall(pattern_hashtag, datum[i][start])
        find_space = re.findall(pattern_space, datum[i][start])
        find_open_parantheses = re.findall(pattern_open_parantheses, datum[i][start])
        find_close_paranthses = re.findall(pattern_close_parantheses, datum[i][start])
        find_integer = re.findall(pattern_integer, datum[i][start])
        if find_string and find_at_the_rate and not find_dot:
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              34, print_array)
        if find_string and find_hashtag and not find_space:
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              1, print_array)
        if find_integer and find_hashtag and not find_space:
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              0, print_array)
        if (find_string and find_open_parantheses)or(find_string and find_close_paranthses):
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              19, print_array)
        if find_integer and find_at_the_rate and not find_dot:
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              36, print_array)
        if find_integer and find_at_the_rate and find_dot and not find_string:
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              35, print_array)
        if (find_integer and find_open_parantheses)or (find_integer and find_close_paranthses):
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              14, print_array)
    return print_array


def print_decimal_values(filesname, start, end, datum, print_array):
    defective_rows = row_no_in_original_file = func_count = funct_count = 0
    for i in range(1, len(datum)):
        row_no_in_original_file += 1
        find_integer = re.findall(pattern_integer, datum[i][start])
        find_zipcode_without_hyphen = re.findall(pattern_zipcode_without_hyphen, datum[i][start])
        find_zipcode_four_digits = re.findall(patter_zipcode_four_digits, datum[i][start])
        find_string = re.findall(pattern_string, datum[i][start])
        find_dot = re.findall(pattern_dot, datum[i][start])
        if find_integer and not find_zipcode_without_hyphen and (not 
            find_zipcode_four_digits and not find_string and find_dot):
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file,func_count,
                                              i,2, print_array)
    return print_array


def print_state_code(filesname, start, end, datum, print_array):
    defective_rows = row_no_in_original_file = func_count = funct_count = 0
    for i in range(1, len(datum)):
        row_no_in_original_file += 1
        if(datum[i][start] in state_code_array)and(datum[i][start] not in states_and_cities):
            for j in range(i+1, len(datum)):
                key = (datum[i][start], datum[j][start])
                if key[0] == key[1]:
                    defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              30, print_array)
    return print_array


def print_state_code_lowercase(filesname, start, end, datum, print_array):
    defective_rows = row_no_in_original_file = func_count = funct_count = 0
    for i in range(1, len(datum)):
        row_no_in_original_file += 1
        find_lowercase = re.findall(pattern_lowercase, datum[i][start])
        if (datum[i][start].upper()in state_code_array)and find_lowercase:
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              31, print_array)
    return print_array


def print_improper_email_entries(filesname, start, end, datum, print_array):
    defective_rows = row_no_in_original_file = func_count = funct_count = 0
    for i in range(1, len(datum)):
        find_string = re.findall(pattern_string, datum[i][start])
        find_space = re.findall(pattern_space, datum[i][start])
        find_dot = re.findall(pattern_dot, datum[i][start])
        find_at_the_rate = re.findall(pattern_at_the_rate, datum[i][start])
        find_email = re.findall(pattern_email, datum[i][start])
        row_no_in_original_file += 1
        if len(find_at_the_rate) >=2:
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              37, print_array)
        if find_string and find_email and find_dot and find_space:
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              37, print_array)
        if find_email and not find_dot:
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              37, print_array)
        if find_string and not find_email:
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              37, print_array)
    return print_array


def print_string_with_dots_not_email_not_website(filesname, start, end, datum, print_array):
    defective_rows = row_no_in_original_file = func_count = funct_count = 0
    for i in range(1, len(datum)):
        find_string = re.findall(pattern_string, datum[i][start])
        find_space = re.findall(pattern_space, datum[i][start])
        find_dot = re.findall(pattern_dot, datum[i][start])
        find_email = re.findall(pattern_email, datum[i][start])
        find_integer = re.findall(pattern_integer, datum[i][start])
        find_empty = re.findall(pattern_empty, datum[i][start])
        find_no_entry = re.findall(pattern_no_entry, datum[i][start])
        find_website = re.findall(pattern_website, datum[i][start])
        row_no_in_original_file += 1
        if ((find_string and find_integer and not find_empty and not find_no_entry and
            find_dot and not find_email and not find_website)or
            (find_string and not find_integer and not find_empty and
             find_dot and not find_email and not find_website and not
              find_no_entry))and len(find_string) > 3:
            defective_rows += 1
            funct_count = print_in_improperTxt(datum, start, defective_rows,
                                              row_no_in_original_file, func_count, i,
                                              3, print_array)
    return print_array


def print_zip_code(filesname, start, end, datum, print_array):
    defective_rows = row_no_in_original_file = func_count = funct_count = 0
    for i in range(1, len(datum)):
        row_no_in_original_file += 1
        find_phone = re.findall(pattern_phone, datum[i][start])
        find_string = re.findall(pattern_string, datum[i][start])
        find_integer = re.findall(pattern_integer, datum[i][start])
        find_pattern_phone_parantheses = re.findall(patten_phone_parantheses, datum[i][start])
        find_hashtag = re.findall(pattern_hashtag, datum[i][start])
        find_slash = re.findall(pattern_slash, datum[i][start])
        find_space = re.findall(pattern_space, datum[i][start])
        find_dot = re.findall(pattern_dot, datum[i][start])
        if len(find_phone) == 1and len(find_integer) < 10 and not find_string and (not
            find_hashtag and not find_pattern_phone_parantheses)and not find_slash and (not 
            find_space):
            y = datum[i][start].split("-")[0]
            for j in range(0, len(zipcodes)):
                if y == zipcodes[j]:
                    defective_rows += 1
                    funct_count = print_in_improperTxt(datum, start, defective_rows,
                                                      row_no_in_original_file, func_count, i,
                                                      33, print_array)
        elif len(find_integer) == 5 and not find_phone and not find_hashtag and (not 
            find_dot and not find_string and not find_space):
            for j in range(0, len(zipcodes)):
                if datum[i][start] == zipcodes[j]:
                    defective_rows += 1
                    funct_count = print_in_improperTxt(datum, start, defective_rows,
                                                      row_no_in_original_file, func_count, i,
                                                      20, print_array)
        elif len(find_integer) == 4 and not find_phone and not find_hashtag and (not 
            find_dot and not find_string and not find_space):
            c = "0" + datum[i][start]
            for j in range(0, len(zipcodes)):
                if c == zipcodes[j]:
                    defective_rows += 1
                    funct_count = print_in_improperTxt(datum, start, defective_rows,
                                                      row_no_in_original_file, func_count, i,
                                                      7, print_array)
    return print_array


def print_improper_zip_code(filesname, start, end, datum, print_array):
    defective_rows = row_no_in_original_file = func_count = funct_count = 0
    here = there = nowhere = 0
    for i in range(1, len(datum)):
        row_no_in_original_file += 1
        find_phone = re.findall(pattern_phone, datum[i][start])
        find_string = re.findall(pattern_string, datum[i][start])
        find_integer = re.findall(pattern_integer, datum[i][start])
        find_pattern_phone_parantheses = re.findall(patten_phone_parantheses, datum[i][start])
        find_hashtag = re.findall(pattern_hashtag, datum[i][start])
        find_slash = re.findall(pattern_slash, datum[i][start])
        find_space = re.findall(pattern_space, datum[i][start])
        find_dot = re.findall(pattern_dot, datum[i][start])
        if len(find_phone) == 1and len(find_integer) < 10 and not find_string and (not 
            find_hashtag and not find_pattern_phone_parantheses)and not find_slash and (not 
            find_space):
            present_in_row = 0
            y = datum[i][start].split("-")[0]
            if zipcodes[y] and len(y) >3:
                for j in range(0, len(zipcodes[y])):
                    for k in range(0, len(datum[i])):
                        if (zipcodes[y][j]==datum[i][k]):
                            present_in_row += 1
                        else:
                            pass
                if present_in_row == 0:
                    print "datum[i][start] 222 is", datum[i][start]
                    defective_rows += 1
                    funct_count = print_in_improperTxt(datum, start, defective_rows,
                                                      row_no_in_original_file, func_count, i,
                                                      39, print_array)
        elif len(find_integer) == 5 and not find_phone and not find_hashtag and (not 
            find_dot and not find_string and not find_space):
            present_in_row= 0
            if zipcodes[datum[i][start]]:
                for j in range(0, len(zipcodes[datum[i][start]])):
                    for k in range(0, len(datum[i])):
                        if (zipcodes[datum[i][start]][j]==datum[i][k]):
                            present_in_row += 1
                        else:
                            pass
                if present_in_row == 0:
                    print "datum[i][start] 333 is", datum[i][start]
                    defective_rows += 1
                    funct_count = print_in_improperTxt(datum, start, defective_rows,
                                                      row_no_in_original_file, func_count, i,
                                                      39, print_array)
                    correct_place(datum[i][start])
        elif len(find_integer) == 4 and not find_phone and not find_hashtag and (not 
            find_dot and not find_string and not find_space):
            present_in_row = 0
            c = "0" + datum[i][start]
            if zipcodes[c]:
                for j in range(0, len(zipcodes[c])):
                    for k in range(0, len(datum[i])):
                        if (zipcodes[c][j]==datum[i][k]):
                            present_in_row += 1
                        else:
                            pass
                if present_in_row == 0:
                    print "datum[i][start] 111is", datum[i][start]
                    defective_rows += 1
                    funct_count = print_in_improperTxt(datum, start, defective_rows,
                                                      row_no_in_original_file, func_count, i,
                                                      39, print_array)
    return print_array

customDict = dict(
	UPPERCASE = "AN UPPERCASE", #	32
	EMPTY = "AN EMPTY ENTRY",   #7
	STRING = "A STRING ENTRY",   #29
	STRING_WITHOUT_HYPHEN = "A STRING WITHOUT HYPHEN",   #30
	PURE_STRING = "A PURE STRING",   #24
	STRING_WITH_INTEGER_AND_SPACES = "A STRING WITH INTEGER AND SPACES",   #31
	INTEGER = "AN INTEGER",   #12
	INTEGER_ONLY = "ONLY INTEGER",   #14
	IMPROPER_DECIMAL = "AN IMPROPER DECIMAL INTEGER",   #10
	IMPROPER_INTEGER = "AN IMPROPER INTEGER",   #11
	EMAIL = "AN EMAIL",   #5
	WEBSITE = "WEBSITE",   #35
	SPECIAL_CHARACTER = "A SPECIAL CHARACTER",   #26
	SPECIAL_CHARACTER_FOR_PHONE = "A SPECIAL CHARACTER (unlikely for phone)",   #27
	SPECIAL_CHARACTER_FOR_WEBSITE = "A SPECIAL CHARACTER (unlikely for website)",   #28
	HYPHEN = "A HYPHEN",   #9
	SPACE = "A SPACE",   #25
	NO_DOTS = "NO DOTS",   #20
	INTEGER_BUT_NOT_ZIPCODE  = "PURE INTEGER (but not zipcode)",   #13
	MORE_INTEGER_THAN_STRING = "INTEGERS DOMINATE STRING",   #16
	MORE_STRING_THAN_INTEGER = "STRING DOMINATES INTEGER",   #17
	NON_US_STATE_CODE = "NON US STATE CODE",   #19
	at_the_rate_BUT_NOT_EMAIL_ENTRY = "@ BUT NOT EMAIL",   #37
	CONTAINS_HASHTAG_WITH_STRING = "# ALONGSIDE STRINGS",   #1
	CONTAINS_HASHTAG_WITH_INTEGER = "# ALONGSIDE INTEGERS",   #0
	PARANTHESES_WITH_STRING = "STRING_WITH_PARANTHESES", #22
	at_the_rate_WITH_INTEGERS = "@ WITH INTEGERS", #40
	at_the_rate_WITH_DECIMAL_INTEGERS = "@ WITH DECIMAL INTEGERS",   #39
	INTEGER_WITH_PARANTHESES = "INTEGER WITH PARANTHESES",   #15
	DECIMAL_VALUE = "DECIMAL VALUE",   #2
	US_STATE_CODE = "US STATE CODE",   #33
	US_STATE_CODE_IN_LOWERCASE = "US STATE CODE IN LOWERCASE",   #34
	ZIPCODE_WITH_HYPHEN = "ZIP CODE WITH HYPHEN",   #36
	POSSIBLE_ZIPCODE = "POSSIBLE ZIPCODE",   #23
	FOUR_DIGIT_ZIPCODE = "FOUR DIGIT ZIP CODE",   #8
	DUPLICATE_EMAIL = "DUPLICATE EMAIL",   #4
	MULTIPLE_at_the_rate = "MULTIPLE AT THE RATE",   #18
	EMAIL_WITH_SPACE = "EMAIL WITH SPACE",   #6
	at_the_rate_WITHOUT_DOT = "@ WITHOUT DOT",   #38
	NO_at_the_rate = "@ IS NOT PRESENT",   #21
	DOT_BUT_NOT_EMAIL_OR_WEBSITE = "DOT (but not email or website)",   #3
)
sortedDict = [(key,customDict[key]) for key in sorted(customDict)]



# [('CONTAINS_HASHTAG_WITH_INTEGER', '# ALONGSIDE INTEGERS'), ('CONTAINS_HASHTAG_WITH_STRING', '# ALONGSIDE STRINGS'), ('DECIMAL_VALUE', 'DECIMAL VALUE'), ('DOT_BUT_NOT_EMAIL_OR_WEBSITE', 'DOT (but not email or website)'), ('DUPLICATE_EMAIL', 'DUPLICATE EMAIL'), ('EMAIL', 'AN EMAIL'), ('EMAIL_WITH_SPACE', 'EMAIL WITH SPACE'), ('EMPTY', 'AN EMPTY ENTRY'), ('FOUR_DIGIT_ZIPCODE', 'FOUR DIGIT ZIP CODE'), ('HYPHEN', 'A HYPHEN'), ('IMPROPER_DECIMAL', 'AN IMPROPER DECIMAL INTEGER'), ('IMPROPER_INTEGER', 'AN IMPROPER INTEGER'), ('INTEGER', 'AN INTEGER'), ('INTEGER_BUT_NOT_ZIPCODE', 'PURE INTEGER (but not zipcode)'), ('INTEGER_ONLY', 'ONLY INTEGER'), ('INTEGER_WITH_PARANTHESES', 'INTEGER WITH PARANTHESES'), ('MORE_INTEGER_THAN_STRING', 'INTEGERS DOMINATE STRING'), ('MORE_STRING_THAN_INTEGER', 'STRING DOMINATES INTEGER'), ('MULTIPLE_at_the_rate', 'MULTIPLE AT THE RATE'), ('NON_US_STATE_CODE', 'NON US STATE CODE'), ('NO_DOTS', 'NO DOTS'), ('NO_at_the_rate', '@ IS NOT PRESENT'), ('PARANTHESES_WITH_STRING', 'STRING_WITH_PARANTHESES'), ('POSSIBLE_ZIPCODE', 'POSSIBLE ZIPCODE'), ('PURE_STRING', 'A PURE STRING'), ('SPACE', 'A SPACE'), ('SPECIAL_CHARACTER', 'A SPECIAL CHARACTER'), ('SPECIAL_CHARACTER_FOR_PHONE', 'A SPECIAL CHARACTER (unlikely for phone)'), ('SPECIAL_CHARACTER_FOR_WEBSITE', 'A SPECIAL CHARACTER (unlikely for website)'), ('STRING', 'A STRING ENTRY'), ('STRING_WITHOUT_HYPHEN', 'A STRING WITHOUT HYPHEN'), ('STRING_WITH_INTEGER_AND_SPACES', 'A STRING WITH INTEGER AND SPACES'), ('UPPERCASE', 'AN UPPERCASE'), ('US_STATE_CODE', 'US STATE CODE'), ('US_STATE_CODE_IN_LOWERCASE', 'US STATE CODE IN LOWERCASE'), ('WEBSITE', 'WEBSITE'), ('ZIPCODE_WITH_HYPHEN', 'ZIP CODE WITH HYPHEN'), ('at_the_rate_BUT_NOT_EMAIL_ENTRY', '@ BUT NOT EMAIL'), ('at_the_rate_WITHOUT_DOT', '@ WITHOUT DOT'), ('at_the_rate_WITH_DECIMAL_INTEGERS', '@ WITH DECIMAL INTEGERS'), ('at_the_rate_WITH_INTEGERS', '@ WITH INTEGERS')]
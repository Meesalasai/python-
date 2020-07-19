import re  #for regular expression

patterns = ['term1', 'term2']

text = "This is a string with term1, not the other!"

for pattern in patterns:
    print("I'm searching for:" + pattern)

    if re.search(pattern, text):
        print("MATCHEDes")
    else:
        print("NOT MATCHED")

print("\n")

pattern1 = "term1"
match = re.search(pattern1, text)
print(type(match)) #<class 're.Match'> - special regular expression Match object that returned by the search method
#the Match object more than boolean, it already contains the information about where the match starts and where it ends
print(type(match.start())) #<class 'int'>
print(match.start()) #22 index position where that match starts
#if we will shorter text:
text1 = "term1"
match1 = re.search(pattern1, text1)
print(match1.start()) #outputs 0
print("\n")

#Regular expression also have the ability to split on a particular pattern
split_term = "@"
email = "user@gmail.com"
print(re.split(split_term, email)) #['user', 'gmail.com']
#also you can realise that with built-in string method:
email1 = "user@gmail.com".split('@')
#But the first comes from the regular expression library
print("\n")

print(re.findall('match', 'test phrase match in match middle')) #['match', 'match']
#just takes the pattern or a string anda returns a list of all non overlapping matches in string
print("\n")

def multi_re_find(patterns, phrase):
    for pat in patterns:
        print("Searching for pattern {}:".format(pat))
        print(re.findall(pat, phrase))
        print('\n')

#There are 5 ways to express repeatition in a pattern
#a pattern followed by the asterix (*) is repeated 0 or more time

test_phrase = 'sdsdd..sssddd..sdddsddd...dsds...dsssssss...sddddd'
test_pattern = ['sd*']
#this * stands for is I want to find an "s" followed by 0 or more 'd's
multi_re_find(test_pattern, test_phrase) #['sd', 'sdd', 's', 's', 'sddd', 'sddd', 'sddd', 'sd', 's', 's', 's', 's', 's', 's', 's', 's', 'sddddd']

#if we want 1 or more 'd's, we need to put (+) plus sign:
test_pattern1 = ['sd+']
multi_re_find(test_pattern1, test_phrase) #['sd', 'sdd', 'sddd', 'sddd', 'sddd', 'sd', 'sddddd']

#if I wanted 0 or 1 time, I can put a (?) question mark:
test_pattern2 = ['sd?']
multi_re_find(test_pattern2, test_phrase) #['sd', 'sd', 's', 's', 'sd', 'sd', 'sd', 'sd', 's', 's', 's', 's', 's', 's', 's', 's', 'sd']

#how to defina a specific count, let's say what is it followed by three 3 'd's:
test_pattern3 = ['sd{3}']
multi_re_find(test_pattern3, test_phrase) #['sddd', 'sddd', 'sddd', 'sddd']

#if you want to specify 2 or 3 'd's:
test_pattern4 = ['sd{2,3}']
multi_re_find(test_pattern4, test_phrase) #['sdd', 'sddd', 'sddd', 'sddd', 'sddd']

#let's say I want 1 or more 'd's and 's' followed by several letters:
#so I want to know where s is followed by either s or d, not together but separate here
test_pattern5 = ['s[sd]+']
multi_re_find(test_pattern5, test_phrase) #['sdsdd', 'sssddd', 'sdddsddd', 'sds', 'sssssss', 'sddddd']

#Let's talk about exclusion and we can use (^) carrot symbol for that.To exclude terms
test_phrase2 = 'This is a string! But it has a punctuation. How can we remove it?'
test_pattern6 = ['[^!.?]+'] #this character remove all this followed !.? characters
multi_re_find(test_pattern6, test_phrase2) #['This is a string', ' But it has a punctuation', ' How can we remove it']

test_pattern7 = ['[a-z]+']
multi_re_find(test_pattern7, test_phrase2) #['his', 'is', 'a', 'string', 'ut', 'it', 'has', 'a', 'punctuation', 'ow', 'can', 'we', 'remove', 'it']

test_pattern7 = ['[A-Z]+']
multi_re_find(test_pattern7, test_phrase2) #['T', 'B', 'H']

#You can use "escape" codes to find specific types of patterns in your data such as digits non digits whitespace and more
#Those are indicated using a "backslash" \
#It means the escapes are indicated by prefixing the character with the backslash
#The way we do that is by making it into a literal value with the letter 'r' and we type an 'r' outside of the string there tben a backslash then a special code for the escape
text_phrase3 = 'This is a string with numbers 123123 and symbols like #hashtad &ampersand and @at'

#For returning digits:
test_pattern8 = [r'\d+'] #this will return back a sequence of digits
multi_re_find(test_pattern8, text_phrase3) # ['123123']

#It will return non-digits:
test_pattern9 = [r'\D+']
multi_re_find(test_pattern9, text_phrase3) #['This is a string with numbers ', ' and symbols like #hashtad &ampersand and @at']

#Sequence of the whitespace: (not super useful, but if you want to count how much whitespace there is
test_pattern10 = [r'\s+']
multi_re_find(test_pattern10, text_phrase3) #[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

#capital S for the nonwhitespace:
test_pattern11 = [r'\S+']
multi_re_find(test_pattern11, text_phrase3) #['This', 'is', 'a', 'string', 'with', 'numbers', '123123', 'and', 'symbol', 'like', '#hashtad', '&ampersand', 'and', '@at']

#for all the alphanumeric characters those are letters and numbers:
test_pattern12 = [r'\w+']
multi_re_find(test_pattern12, text_phrase3) #['This', 'is', 'a', 'string', 'with', 'numbers', '123123', 'and', 'symols', 'like', 'hashtad', 'ampersand', 'and', 'at']

#non-alphanumeric those are symbols and spaces
test_pattern12 = [r'\W+']
multi_re_find(test_pattern12, text_phrase3) #[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' #', ' &', ' ', ' @']

#SO you should have a solid understanding of how to be able to reference the regular expressions

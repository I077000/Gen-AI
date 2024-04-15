# Excersises Day 4- String

"""
1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
"""

words = ['Thity', 'Days', 'of', 'Python']

sentence = ' '.join(words)

print(sentence)

"""
2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
"""

words = ['Coding', 'For', 'All']

sentence = ' '.join(words)

print(sentence)

"""
3. Declare a variable named company and assign it to an initial value "Coding For All".
"""

company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())

"""
Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
"""
company = "coding for all"
print(company.capitalize())
print(company.swapcase())
print(company.title())

"""
Cut(slice) out the first word of Coding For All string.
"""

sentence = "Coding For All string"
print(sentence.split(' ')[0])

"""
Check if Coding For All string contains a word Coding using the method index, find or other methods.
"""
print(sentence.find('Coding'))

"""
Replace the word coding in the string 'Coding For All' to Python.
"""
sentence = 'Coding For All'
sentence_replace = sentence.lower().replace('coding','Python')
print(sentence_replace.title())

"""
Create an acronym or an abbreviation for the name 'Python For Everyone'.
"""
sentence = "Python For Everyone"
words = sentence.split(" ")
acronym = []
for word in words:
    acronym.append(word[0:1])
    
print(''.join(acronym))

"""
Use index to determine the position of the first occurrence of C in Coding For All.
"""
sentence = "Coding For All"
print(sentence.index('C'))

"""
Use index to determine the position of the first occurrence of F in Coding For All.
"""
sentence = "Coding For All"
print(sentence.index("F"))

"""
Use rfind  and rindex to determine the position of the last occurrence of l in Coding For All People.
rfind and rindex provide same out put highest index of the occurance.
difference is  rfind returns -1 if char not found, while rindex throws exception.

"""
sentence =  "Coding For All People"
print(sentence.rindex('l'))
print(sentence.rfind('l'))

"""
rPartition: Python rpartition() function is used to partition a string at the last occurrence of the given string and return a tuple that includes 3 parts – the part before the separator, the argument string (separator itself), and the part after the separator.

The syntax for Python string rpartition() is as follows:
string.rpartition(separator)
"""

# Python program to illustrate rpartition()
string = 'Hello my name is Jimmy'
# when separator is found
print(string.rpartition('is'))

# when separator is not found
print(string.rpartition('who'))

string2 = 'Cricket is fun to watch, isnt it true?'
# when separator occurs multiple times in the string
print(string2.rpartition('is'))

"""
 rjust in Python:
 The string rjust() method returns a new string of the specified length after 
 inserting a specified character in the original string’s left side i.e. it returns a right-justified string of the specified width.
  The syntax followed by the Python rjust() function is as follows:
"""

s = 'Python'
width = 10
print('Original string:', s)
print('Modified string:', s.rjust(width))

s = 'Programming'
width = 18
# specifying fillchar parameter
fillchar = '^'
print('Original string:', s)
print('Modified string:', s.rjust(width, fillchar))

"""
Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
"""

sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find("because"))

"""
Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

"""

sentence = 'You cannot end a sentence with because because because is a conjunction'
repeated_word = []
print(sentence.partition('because'))
repeated_word.append(sentence.partition('because')[1])


"""
Does ''Coding For All' start with a substring Coding?
"""
sentence = "Coding For All"
print(sentence.startswith('Coding'))
print(sentence.endswith('coding'))

"""
'   Coding For All      '  , remove the left and right trailing spaces in the given string.
"""

sentence = '   Coding For All      ' 
print(sentence)
print(sentence.strip())

"""
Which one of the following variables return True when we use the method isidentifier():
30DaysOfPython
thirty_days_of_python
"""

print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

"""
The following list contains the names of some of python libraries: 
['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. 
Join the list with a hash with space string.
"""

lib_list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" # ".join(lib_list))

"""
Use the new line escape sequence to separate the following sentences.
I am enjoying this challenge.
I just wonder what is next.
"""

sentence = '''
I am enjoying this challenge.
I just wonder what is next.'''
print('I am enjoying this challenge.\n I just wonder what is next.')

"""
Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
"""

radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with raidus {} is {} meters square".format(str(radius),str(area)))

"""
Make the following using string formatting methods:
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144

"""
a=8
b=6
print(f'{a}+{b} = {a+b}')
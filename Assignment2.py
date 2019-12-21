#Import regex library
import re

def longest_sentence(a):
	"""Returns element [0] of list of string sorted by length of string elements splitted by whitespace in descending order 

	Parameters:
	a (list): The list of strings to perform above

	Returns: Element [0] of list of string sorted by length of string elements splitted by whitespace in descending order
	""" 
	longest_sentence = sorted(a,key=lambda x: len(x.split()), reverse=True)[0]
	return(longest_sentence) 

def strip_delimiters(a):
	""" Removes delimiters from the list of strings

	Parameters:
	a (list): The list of strings to remove delimiters 

	Returns: List of strings without delimiters 
	""" 
	a=[item.lower() for item in a]
	words_strip=[]
	for item in a:
		words_strip.append(item.strip(delimiters))
	return(words_strip)

def longest_word(a):
	"""Returns element [0] of list of string sorted by length in descending order 

	Parameters:
	a (list): The list of strings to perform above

	Returns: Element [0] of list of string sorted by length in descending order 
	""" 
	for item in a:
		new=(sorted(list(set(a)), key=len, reverse=True)[0])
		return(new)
def freq_dict(a):
	"""Convert a list of words into a dictionary of word-frequency pairs 

	Parameters:
	a (list): The list of strings to perform above

	Returns: Dictionary of word-frequency pairs 
	""" 
	word_freq = [a.count(item) for item in a]
	d = dict(zip(a,word_freq))
	return d

def sort_freq_dict(a):
	"""Turns a dictionary of word-frequency pairs to list and sorts by descending order

	Parameters:
	a (dict): The dictionary of word-frequency pairs to perform above

	Returns: List of word-frequency pairs sorted by descending order
	""" 
	freq_sort = [(a[key], key) for key in a]
	freq_sort.sort()
	freq_sort.reverse()
	return freq_sort

def remove_stopwords(a,b):
	"""Removes elements listed in (b) from list (a) 

	Parameters:
	a (list): List of elements to perform above
	b (list): List of elements to be removed from a

	Returns: List of elements (a) without elements (b)
	""" 
	stopwords_removed=[word for word in a if word not in b]
	return stopwords_removed

def remove_delimiters_dubs(a):
	"""Remove delimiters and duplicates from list of elements

	Parameters:
	a (list): List of elements to perform above
	
	Returns: List of elements without delimiters and duplicates 
	""" 
	words_strip=[]
	for item in a:
		words_strip.append(item.strip(delimiters))
	new=(list(set((words_strip))))
	return(new)

def list_to_str(a):
	"""Converts list of elements to string

	Parameters:
	a (list): List of elements to perform above
	
	Returns: String containing list (a) elements 
	""" 
	str1=""
	return str1.join(a) 


#Open and read files
f=open('Sapir1921_chapter1.txt')
text=f.read()
f1=open('stopwordlist.txt')
stop_words=f1.read()

#Process stopwords file: create list of stopwords 
stop_words=(re.sub("\s+", " ", stop_words)).split()

#Replace ellipsis by a period in text
text_process = re.sub(r'\.+', ".", text)

#Replace whitespace by a space in text
text_process = re.sub("\s+", " ", text_process)

#Define acronyms at the end of sentences and replace with ||acronym||.
acronyms_end = r'(\b[A-Z][a-zA-Z\.]*[A-Z]\b\.?) +(?=[A-Z0-9]|["\'])'
text_process1 = re.sub(acronyms_end, "||\\1||. ", text_process)

#Split text into sentences 
sentences = re.split(r'(?<=[^A-Z.].[.?!"\')\]]) +(?=[A-Z0-9]|[\|"\'])', text_process1)



#Get the longest sentence in text
sentence_longest = longest_sentence(sentences)


#Define delimiters
delimiters = '\<\"\'\[\{\(\@.,;:?!>]})&=/'

#Replace two hypens by a period
words = re.sub("--", ". ", text_process)

#Create list of words in text
words = words.split()



#Remove delimiters from list of words
words_stripped = strip_delimiters(words)


#Get the longest word in text
word_longest=longest_word(words_stripped)


#Remove stopwords from list of words stripped by delimiters
stopwords_removed=remove_stopwords(words_stripped, stop_words)

#Create a dict of word-frequency pairs from word list without stopwords
words_freq=freq_dict(stopwords_removed)

#Turn a dict of word-frequency pairs into list and sort by descending order
freq_sorted=sort_freq_dict(words_freq)

#Get five most frequent words with frequencies 
five_most_freq=freq_sorted[:5]


#Replace first word of each sentence with a space and append it to a list

first_words_removed=[]
for x in sentences:
	first_words_removed.append(re.sub(r'^\W*\w+\W*', ' ', x))

	
#Convert word list (without first word in each sentence) to string 
words_string=list_to_str(first_words_removed)

#Replace two hypens by a period
words2=(re.sub("--", ". ", words_string)).split()

#Remove delimiters and duplicates from word list (without first word in each sentence)	
words2_stripped = remove_delimiters_dubs(words2)

#Remove stopwords from word list (without first word in each sentence)
words2_stopwords_removed=remove_stopwords(words2_stripped, stop_words)

#Convert to string word list (without first word in each sentence)
words2_string = ' '.join([str(elem) for elem in words2_stopwords_removed])

#Get list A-L of named entities 
list_a_l = sorted(re.findall(r'([A-L][a-z]+)', words2_string))

#Get list M-Z of named entities 
list_m_z = sorted(re.findall(r'([M-Z][a-z]+)', words2_string))


print('The longest sentence in text is:\n\n',sentence_longest,'\n')
print('The longest word in text is:',f"'{word_longest}'",'\n')
print('Five most frequent words in text with their frequencies (frequency, word) are:\n',five_most_freq,'\n')
print('Named entities (list from A-L) in text are:\n\n', list_a_l, '\n')
print('Named entities (list from M-Z) in text are:\n\n', list_m_z)
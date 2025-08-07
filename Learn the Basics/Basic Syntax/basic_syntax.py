# Most basic
print('Hello World!')

# .!/usr/bin/python3 -> we can also do this and this way to can execute the script like its a .sh script
print ("Hello, World!")



#Python Class names start with an uppercase letter. All other identifiers start with a lowercase letter.
#Starting an identifier with a single leading underscore indicates that the identifier is private identifier.
#Starting an identifier with two leading underscores indicates a strongly private identifier.
#If the identifier also ends with two trailing underscores, the identifier is a language-defined special name.



#Reserved words
#and 	as 	assert
#break 	class 	continue
#def 	del 	elif
#else 	except 	False
#finally 	for 	from
#global 	if 	import
#in 	is 	lambda
#None 	nonlocal 	not
#or 	pass 	raise
#return 	True 	try
#while 	with 	yield



#Multilines statements
total = "item_one, " + \
        "item_two, " + \
        "item_three"

print(f'total: {total}')

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']

print(f'days: {days}')


#Quotations in Python
#Python accepts single ('), double (") and triple (''' or """) quotes to denote string literals, as long as the same type of quote starts and ends the string.
#The triple quotes are used to span the string across multiple lines. For example, all the following are legal −

word = 'word'
print (word)

sentence = "This is a sentence."
print (sentence)

paragraph = """This is a paragraph. It is
 made up of multiple lines and sentences."""
print (paragraph)


#Single line comment -> #
#Multiline comment (below)
'''
This is a multiline
comment.
'''



#ifs
expression = True
if expression :
   print(True)
elif expression :
   print(True)
else :
   print(True)

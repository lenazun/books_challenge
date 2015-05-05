#!/usr/bin/env python
import shlex

#This version uses a dictionary to store the book info
LIBRARY = {}


def addBook(args):
	"""add "$title" "$author": adds a book to the library with the given title and author. 
	All books are unread by default.
	>>> addBook(["Moby Dick", "Herman Melville"])
	Added "Moby Dick" by Herman Melville.
	"""

	title, author = args

	if title not in LIBRARY.keys():
		LIBRARY[title] = [author, 'unread']
		print 'Added "{}" by {}.'.format(title, author) 
	else:
		print 'The book "{}" is already in your library.'.format(title)



def markRead(args):
	"""read "$title": marks a given book as read.
	>>> markRead(['Moby Dick'])
	You've read "Moby Dick".
	"""

	title = args[0]

	if title in LIBRARY.keys():
		LIBRARY[title][1] = 'read'
		print 'You\'ve read "{}".'.format(title) 
	else:
		print 'The book "{}" is not in your library. Add it first!'.format(title) 



def show(args):
	"""
	show all: displays all of the books in the library
	>>> show(['all', 'all'])
	"Moby Dick" by Herman Melville (read)
	show unread: display all of the books that are unread
	show all by "$author": shows all of the books in the library by the given author.
	>>> show(['all', 'Herman Melville'])
	"Moby Dick" by Herman Melville (read)
	show unread by "$author": shows the unread books in the library by the given author
	"""

	status, author = args

	if len(LIBRARY.keys()) == 0:
		print "Your library is empty."

	else:
		#dictionary filters given the search criteria
		if status != 'all' and author != 'all':
			to_print = {title:record for (title, record) in LIBRARY.iteritems() if record[0] == author and record[1] == status}
		elif author != 'all':
			to_print = {title:record for (title, record) in LIBRARY.iteritems() if record[0] == author}
		elif status != 'all':	
			to_print = {title:record for (title, record) in LIBRARY.iteritems() if record[1] == status}

		else:
			to_print = LIBRARY

		count = 0		
		for title, record in to_print.items():
				print '"{}" by {} ({})'.format(title, record[0], record[1]) 
				count += 1

		if count == 0:
			print 'Your have no {} books by "{}".'.format(status, author) 


def main():

	print "Welcome to your library!"

	keywords =['add', 'read', 'show', 'by', 'quit']
	
	while True:

		try:
			input = shlex.split(raw_input("> "))

		except ValueError, err:
			print "Oh noes! There's an error: " + str(err)
			continue

		#splits the command from the input, small dispatch table for functions
		action = ' '.join([i.lower() for i in input if i in keywords][:4])

		commands = {'add': addBook,
					'read': markRead,
					'show': show,
					'show by': show,
					'quit' : ''
					}

		#splits the arguments from the input and checks for empty strings/spaces
		args = [i for i in input if i not in keywords 
								and i.isspace() == False
								and i != '']

		if action == 'show' and len(args) == 1:
			args.append('all')
		
		if action not in commands.keys():
			print "Mmmm... I don't understand! Try another command"

		#quit: quits the program.
		elif action == 'quit':
			break

		elif action:

			try: 
				commands[action](args)

			except:
				print "Invalid input. Remember to use quotation marks around sentences"
				continue

		else:
			continue



if __name__ == '__main__':
	# import doctest
	# doctest.testmod()
    main()




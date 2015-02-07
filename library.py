#!/usr/bin/env python
import shlex


library = {}


def addBook(title, author):
	if title not in library.keys():
		library[title] = [author, 'unread']
		print 'Added "{}" by {}.'.format(title, author) 
	else:
		print 'The book "{}" is already in your library.'.format(title)

def markRead(title):
	if title in library.keys():
		library[title][1] = 'read'
		print 'You\'ve read "{}"'.format(title) 
	else:
		print 'The book "{}" is not in your library. Add it first!'.format(title) 

def show(status, author):

	if len(library.keys()) == 0:
		print "Your library is empty."

	else:
		if author != 'all' and status != 'all':
			to_print = {title:record for (title, record) in library.iteritems() if record[0] == author and record[1] == status}
		elif author != 'all':
			to_print = {title:record for (title, record) in library.iteritems() if record[0] == author}
		elif status != 'all':	
			to_print = {title:record for (title, record) in library.iteritems() if record[1] == status}

		else:
			to_print = library

		count = 0		
		for title, record in to_print.items():
				print '"{}" by {} ({})'.format(title, record[0], record[1]) 
				count += 1

		if count == 0:
			print 'Your have no {} books by "{}".'.format(status, author) 



def main():

	print "Welcome to your library!"

	keywords =['add', 'read', 'show', 'all', 'unread', 'by', 'author', 'quit']
	commands = ['add', 'read', 'show all', 'show unread', 'show all by', 'show unread by', 'quit']

	while True:

		input = shlex.split(raw_input("> "))

		command = ' '.join([i for i in input if i in keywords][:4])

		if command not in commands:
			print "Mmmm... I don't understand! Try another command"

		elif command == 'quit':
			break

		elif command == 'add':
			try:
				addBook(input[1], input[2])
			except:
				print "You need a title and an author. Use quotation marks around Title and Author"
				continue

		elif command == 'read':
			markRead(input[1])

		elif command == 'show all':
			show('all', 'all')

		elif command == 'show all by':
			show('all', input[3])

		elif command == 'show unread':
			show('unread', 'all')

		elif command == 'show unread by':
			show('unread', input[3])

		else:
			continue


		#print library



if __name__ == '__main__':
    main()




# add "$title" "$author": adds a book to the library with the given title and author. All books are unread by default.
# read "$title": marks a given book as read.
# show all: displays all of the books in the library
# show unread: display all of the books that are unread
# show all by "$author": shows all of the books in the library by the given author.
# show unread by "$author": shows the unread books in the library by the given author
# quit: quits the program.


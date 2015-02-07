#!/usr/bin/env python
import shlex


library = {}

def addBook(title, author):
	if title not in library.keys():
		library[title] = [author, 'unread']
		print 'Added "' + title + '" by ' + author
	else:
		print "That title is already in your library!"

def markRead(title):
	if title in library.keys():
		library[title][1] = 'read'
		print 'You\'ve read "' + title + '"'
	else:
		print "That title is not in your library. Add it first!"

def showAll():
	if len(library.keys()) > 0:
		for title, record in library.items():
			print '"' + title + '" by ' + record[0] +  ' (' + record[1] + ')'
	else:
		print "Your library is empty"

def showUnread():

	count = 0
	for title, record in library.items():
		if record[1] == 'unread':
			print '"' + title + '" by ' + record[0] +  ' (' + record[1] + ')'
			count += 1

	if count == 0:
		print "Your have no unread books"

def showAuthor(author):
	count = 0
	for title, record in library.items():
		if record[0] == author:
			print '"' + title + '" by ' + record[0] +  ' (' + record[1] + ')'
			count += 1

	if count == 0:
		print "Your have no books by that author"


def showUreadbyAuthor(author):
	count = 0
	for title, record in library.items():
		if record[0] == author and record[1] == 'unread':
			print '"' + title + '" by ' + record[0] +  ' (' + record[1] + ')'
			count += 1

	if count == 0:
		print "Your have no unread books by that author"






def main ():

	print "Welcome to your library!"

	while True:
		input = shlex.split(raw_input("> "))

		if input[0].lower() == 'quit':
			break

		elif input[0].lower() == 'add':
			try:
				addBook(input[1], input[2])
			except:
				print "You need a title and an author"
				continue

		elif input[0].lower() == 'read':
			markRead(input[1])


		elif input[0].lower() == 'show' and len(input) > 1:

			if input[1].lower() == 'all':

				if len(input) == 4 and input[2].lower() == 'by':
					showAuthor(input[3])
				else:
					showAll()
			
			elif input[1].lower() == 'unread':

				if len(input)== 4 and input[2].lower() == 'by':
					showUreadbyAuthor(input[3])
				else:
					showUnread()

			else:
				continue

		else:
			print "I don't understand. Try a different command."

		print library



if __name__ == "__main__":
    main()





# add "$title" "$author": adds a book to the library with the given title and author. All books are unread by default.
# read "$title": marks a given book as read.
# show all: displays all of the books in the library
# show unread: display all of the books that are unread
# show all by "$author": shows all of the books in the library by the given author.
# show unread by "$author": shows the unread books in the library by the given author
# quit: quits the program.


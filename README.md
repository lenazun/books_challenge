# Personal library challenge
This is a coding challenge for a pre-job interview

Write a small system for managing a personal library. The system should be accessible from the command line.

the program should accept the following commands:

add "$title" "$author": adds a book to the library with the given title and author. All books are unread by default.

read "$title": marks a given book as read.

show all: displays all of the books in the library

show unread: display all of the books that are unread

show all by "$author": shows all of the books in the library by the given author.

show unread by "$author": shows the unread books in the library by the given author

quit: quits the program.

## Some other stipulations:

You can use whatever language you want.

Assume that there can never be two books with the same title in the system (even if they were to have different authors). The user shouldn't be allowed to add two books with the same title.

Do not use a persistence mechanism (ie, a SQL database) for the books. Store them in memory. That is, every time you run the program, the list of books should be empty. Using a database can make some aspects of this a little too easy :)

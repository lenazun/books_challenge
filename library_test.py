
import library

def main():

    print "Adding books:"

    library.addBook(["Moby Dick", "Melville"])
    library.addBook(["La ciudad y los Perros", "Vargas Llosa"])
    library.addBook(["Laberintos", "Borges"])
    library.addBook(["Ficciones", "Borges"])

    print "Adding bad books:"

    library.addBook(["Moby Dick", "Melville"])
    library.addBook([" ", " "])

    print "Mark as read:"
    library.markRead(["Ficciones"])
    library.markRead(["Moby Dick"])

    print "Badly mark as read:"

    library.markRead(["Moby"])

    print "Show all:"
    library.show(['all', 'all'])

    print "Show all by author"
    library.show(['all', 'Borges'])
    library.show(['all', 'Vargas Llosa'])

    print "Show unread by author"
    library.show(['unread', 'Borges'])
    library.show(['unread', 'Melville'])


if __name__ == '__main__':
    main()
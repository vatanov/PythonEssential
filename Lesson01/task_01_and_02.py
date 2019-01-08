"""
Создайте класс, описывающий книгу. Он должен содержать информацию
об авторе, названии, годе издания и жанре. Создайте несколько разных книг.
Определите для него операции проверки на равенство и неравенство,
методы __repr__ и __str__.
"""


class Comment:
    def __init__(self, body):
        self.body = body

    def __repr__(self):
        return self.body


class Book:
    def __init__(self, author, name, year, genre, *comments):
        # Another way:
        # def __init__(self, author, name, year, genre, comments=[]):
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre
        self.comments = comments

    def __eq__(self, other):
        return self.author == other.author and \
               self.name == other.name and \
               self.year == other.year and \
               self.genre == other.genre
        # Another way:
        # if self.author == other.author and self.name == other.name and self.year == other.year and self.genre == other.genre:
        #     return True
        # else:
        #    return False

    def __repr__(self):
        return 'Book({}, {}, {}, {})'.format (self.author, self.name, self.year, self.genre)

    def __str__(self):
        return 'Book: author: {}, name: {}, year: {}, genre: {}, comments: {}'.format (
            self.author,
            self.name,
            self.year,
            self.genre,
            self.comments
        )


python_crash_course = Book ('Eric Matthers', 'Python crash course', 2017, 'Education')
learning_python = Book ('Mark Lutz', 'Learning Python', 2011, 'Education')
learning_python2 = Book ('Mark Lutz', 'Learning Python', 2011, 'Education')

comments = [Comment ('comment 1'), Comment ('comment 2'), Comment ('comment 3')]
hh_guide_galaxy = Book ('Adams Douglas',
                        "The hitch hacker's guide to the galaxy",
                        1979,
                        'Science fiction',
                        comments)

print (repr (python_crash_course))
print (python_crash_course)

print (learning_python == learning_python2)
print (python_crash_course == hh_guide_galaxy)

print (hh_guide_galaxy)

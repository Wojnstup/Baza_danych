book_with_student = '''
    SELECT Title, Author, Name, Surname
    FROM Book
    INNER JOIN Student
    ON Book.StudentID = Student.StudentID;
    '''
only_book = '''
    SELECT BookID, Title, Author FROM Book
'''

only_students = '''
    SELECT StudentID, Name, Surname FROM Student
'''

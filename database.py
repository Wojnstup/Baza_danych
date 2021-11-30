import sqlite3
  
def create_tables():
    conn = sqlite3.connect('data.db')
    
    cursor = conn.cursor()
      
    cursor.executescript('''

        CREATE TABLE Student(
        StudentID INTAGER NOT NULL,
        Name text,
        Surname text,
        Class int,
        Age int,
        Gender text,
        PRIMARY KEY(StudentID)
        );

        CREATE TABLE Book(
        BookID INTAGER NOT NULL,
        Title text,
        Author text,
        Pages int,
        Series text,
        Part int,
        
        StudentID INTAGER NOT NULL,
        FOREIGN KEY(StudentID) REFERENCES Student(StudentID),
        PRIMARY KEY(BookID)
        );
        
    ''')
        
    conn.commit()
    conn.close()

def insert_students():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.executescript('''
        INSERT INTO Student VALUES 
        (1, "Adam", "Kowalski", 7, 13, "M"),
        (2, "Bartosz", "Nowak", 6, 12, "M"),
        (3, "Czeslaw", "Wisniewski", 7,13, "M"),
        (4, "Danuta", "Kaminska", 7,14, "F"),
        (5, "Eryk", "Szymanski", 7,12, "M"),
        (6, "Franek", "Mazur", 5,11, "M"),
        (7, "Grzegorz", "Kaczmarek", 8, 14, "M"),
        (8, "Hannna", "Grabowska", 3, 10, "F"),
        (9, "Igor", "Krol", 3, 10, "M"),
        (10, "Julia", "Zajac", 8, 13, "F")
            ''')

    connection.commit()
    connection.close()

def insert_books():

    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
   
    cursor.executescript('''
    INSERT INTO Book VALUES
    (1, "Harry Potter i kamien filozoficzny", "J.K. Rowling", 260, "Harry Potter", 1,  1),
    (2, "Igrzyska Smierci", "Susan Collins", 245, "Igrzyska Smierci", 1, 1),
    (3, "Muzyka Duszy", "Terry Pratchet", 360, "Swiat Dysku", 16, 5),
    (4, "Wesele", "Stanislaw Wyspianski", 120, "Brak", 0, 3)
            ''')

    connection.commit()
    connection.close()


def fetch_query(query):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    
    cursor.execute(query)
    
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result

def insert_book(title,author,pages,series,part,student_id):

    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Book")
    ID = len(cursor.fetchall()) + 1

    cursor.execute('''
       INSERT INTO Book VALUES (?,?,?,?,?,?,?) 

            ''', (ID, title,author,pages,series,part,student_id))

    connection.commit()
    connection.close()

def insert_student(name,surname,_class,age,gender):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Student")
    ID = len(cursor.fetchall()) + 1

    cursor.execute('''
       INSERT INTO Student VALUES (?,?,?,?,?,?) 

            ''', (ID, name,surname,_class,age,gender))

    connection.commit()
    connection.close()
#create_tables()
#insert_students()
#insert_books()

#fetch_query(book_with_student)

#insert_book("Harry Potter i Czara Ognia", "J.K. Rowling", 400, "Harry Potter", 4, 1)

  #  elif choice == 2:
        









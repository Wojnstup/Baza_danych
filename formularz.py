from flask import Flask, request, render_template, redirect, session
from queries import *
import database

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/book")
def book():
    return render_template("form.html")

@app.route("/add_book")
def add_book():
    try:
        title = request.args.get("title")
        author = request.args.get("author")
        pages = int(request.args.get("pages"))
        series = request.args.get("series")
        part = int(request.args.get("part"))
        student_id = int(request.args.get("StudentID"))

        database.insert_book(title,author,pages,series,part,student_id)
        return "<h1>Added succesfully</h1>"

    except:
        return "<h1>Erorr<h1>"

@app.route("/student")
def student():
    return render_template("form_stud.html")


@app.route("/add_student")
def add_student():
    #try:
    if 1 ==1:
        name = request.args.get("name")
        surname = request.args.get("surname")
        _class = request.args.get("class")
        age = int(request.args.get("age"))
        gender = request.args.get("gender")

        database.insert_student(name,surname,_class,age,gender)
        return "<h1>Added succesfully</h1>"

    #except:
    #    return "<h1>Erorr<h1>"


def run():
    app.run()

if __name__ == "__main__":
    print("Co chcesz zrobic?")
    print("\t1 <- Kwerenda")
    print("\t2 <- Dodaj ksiazke badz ucznia")
    print("")

    try:
        choice = int(input(">> "))
    except:
        print("Wrong input")
        exit 

    if choice == 1:
        print("Wybierz kwerende:")
        print("\t1 <- Najwazniejsze informacje o ksiazkach")
        print("\t2 <- Najwazniejsze informacje o uczniach")
        print("\t3 <- Informacje o wyporzyczeniu ksiazki przez ucznia")
        print("")
        try:
            choice2 = int(input(">> "))
        except:
            print("Wrong input!")
            exit

        if choice2 == 1:
            for i in database.fetch_query(only_book): 
                print(i)
        elif choice2 == 2:
            for i in database.fetch_query(only_students):
                print(i)
        elif choice2 == 3:
            for i in database.fetch_query(book_with_student):
                print(i)

    elif choice == 2:
       app.run() 



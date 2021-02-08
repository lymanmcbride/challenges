#  Version:     3.9.1
#  Name:        Lyman McBride
#  Date:        January 26, 2021
#  Purpose:     Weekly coding challenge. This one is a program
#               asking for user input and allowing them to interact with the database

import sqlite3

#create database
def create_db():
    conn = sqlite3.connect('db_languages.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_languages( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_language TEXT, \
            col_translation TEXT \
            );")
        conn.commit()
        cur,count = count_records(cur)
        if count < 1:
            sql = """INSERT INTO tbl_languages (col_language,col_translation) VALUES (?,?)""" 
            values = [('english', 'Welcome'),('czech', 'Vitejte'),('danish', 'Velkomst'),('dutch', 'Welkom'),('estonian', 'Tere tulemast'),('finnish', 'Tervetuloa'),('flemish', 'Welgekomen'),('french', 'Bienvenue'),('german', 'Willkommen'),('irish', 'Failte'),('italian', 'Benvenuto'),('latvian', 'Gaidits'),('lithuanian', 'Laukiamas'),('polish', 'Witamy'),('spanish', 'Bienvenido'),('swedish', 'Valkommen'),('welsh', 'Croeso')]
            cur.executemany(sql, values)
            conn.commit()
    conn.close()

def count_records(cur):
    count = ""
    cur.execute("SELECT COUNT(*) FROM tbl_languages")
    count = cur.fetchone()[0]
    return cur,count

def greet():
    print("Hello! Welcome to our welcome database! We have a short list of translations of the word 'Welcome!'")
    
def get_language():
    language = input("What language would you like to translate to?\nType 'options' for other options. ('q' for quit)\n").lower()
    return language

def options():
    option = input('a. List the languages in the database.\nb. Add a new language.\nc. back\nd. quit.\n').lower()
    return option

def show_options(cur):  
    cur.execute("SELECT col_language FROM tbl_languages")
    languages = cur.fetchall()
    print("\n\n")
    for tup in languages:
        for word in tup:
            print(word.capitalize())
    return cur

def welcome(cur, language):
    cur.execute("SELECT col_translation FROM tbl_languages WHERE col_language = ?", (language,))
    translation = cur.fetchall()
    for tup in translation:
        for word in tup:
            print("'Welcome' in {} is '{}'".format(language.capitalize(), word))
    return cur

def add_language(cur):
    add_lang = input("What language would you like to add to the database?\n").lower()
    add_translation = input("How do you say 'Welcome' in {}?".format(add_lang)).lower()
    cur.execute("""INSERT INTO tbl_languages (col_language,col_translation) VALUES (?,?)""", (add_lang, add_translation))
    return cur


if __name__ == "__main__":
    create_db()
    greet()
    conn = sqlite3.connect('db_languages.db')
    with conn:
        cur = conn.cursor()
        go = True
        while go:
            language = get_language()
            if language == "options":
                go1 = True
                while go1:
                    option = options()
                    if option == 'a':
                        cur = show_options(cur)
                    elif option == 'b':
                        cur = add_language(cur)
                    elif option == 'c':
                        go1 = False
                    elif option == 'd':
                        print("Thank You!")
                        go1 = False
                        go = False
                    else:
                        print("Please type a valid input, either 'a', 'b', or 'c'.")
            if language == 'q':
                print("Thank you!")
                go = False
            else:
                cur = welcome(cur, language)
    conn.close()
    



# Wendy Bronson
# Module 6 Assignment: Movies Table Queries
# Date: June 2026
#
# Purpose:
# Connect to the MySQL movies database and run table queries
# for studio, genre, and film records.

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "Whitedove031973$",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    # Display Studio records
    cursor.execute("SELECT studio_id, studio_name FROM studio")

    studios = cursor.fetchall()

    print("\n-- DISPLAYING Studio RECORDS --")

    for studio in studios:
        print("Studio ID: {}".format(studio[0]))
        print("Studio Name: {}\n".format(studio[1]))

    # Display Genre records
    cursor.execute("SELECT genre_id, genre_name FROM genre")

    genres = cursor.fetchall()

    print("\n-- DISPLAYING Genre RECORDS --")

    for genre in genres:
        print("Genre ID: {}".format(genre[0]))
        print("Genre Name: {}\n".format(genre[1]))

    # Display films under two hours
    cursor.execute(
        "SELECT film_name, film_runtime FROM film WHERE film_runtime < 120"
    )

    films = cursor.fetchall()

    print("\n-- DISPLAYING Short Film RECORDS --")

    for film in films:
        print("Film Name: {}".format(film[0]))
        print("Runtime: {}\n".format(film[1]))

    # Display films ordered by director
    cursor.execute(
        "SELECT film_name, film_director FROM film ORDER BY film_director"
    )

    directors = cursor.fetchall()

    print("\n-- DISPLAYING Director RECORDS in Order --")

    for director in directors:
        print("Film Name: {}".format(director[0]))
        print("Director: {}\n".format(director[1]))

    print("\nDatabase user {} connected to MySQL on host {} with database {}".format(
        config["user"], config["host"], config["database"]
    ))
    cursor.close()
    db.close()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password is invalid.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist.")
    else:
        print(err)

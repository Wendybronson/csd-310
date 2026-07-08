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
    print("Connected to the movies database!")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid username or password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist.")
    else:
        print(err)


def show_films(cursor, title):

    print("\n-- {} --".format(title))

    query = """
    SELECT
        film_name AS Name,
        film_director AS Director,
        genre_name AS Genre,
        studio_name AS Studio
    FROM film
    INNER JOIN genre
        ON film.genre_id = genre.genre_id
    INNER JOIN studio
        ON film.studio_id = studio.studio_id;
    """

    cursor.execute(query)
    films = cursor.fetchall()

    for film in films:
        print("Film Name: {}".format(film[0]))
        print("Director: {}".format(film[1]))
        print("Genre Name ID: {}".format(film[2]))
        print("Studio Name: {}".format(film[3]))
        print()


try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    show_films(cursor, "DISPLAYING FILMS")

    cursor.execute("""
    INSERT INTO film
    (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
    VALUES
    ('Jurassic Park', 1993, 127, 'Steven Spielberg', 3, 2)
    """)

    db.commit()

    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    cursor.execute("""
    UPDATE film
    SET genre_id = 1
    WHERE film_name = 'Alien'
    """)

    db.commit()

    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")

    cursor.execute("""
    DELETE FROM film
    WHERE film_name = 'Gladiator'
    """)

    db.commit()
    cursor.execute("""
                   DELETE
                   FROM film
                   WHERE film_name = 'Jurassic Park'
                   """)

    db.commit()

    cursor.execute("""
                   INSERT INTO film
                   (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
                   VALUES ('Jurassic Park', 1993, 127, 'Steven Spielberg', 3, 2)
                   """)

    db.commit()

    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

    cursor.close()
    db.close()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password is invalid.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist.")
    else:
        print(err)
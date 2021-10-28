




import flask
from sqlalchemy.orm import sessionmaker
from db_setup import BookORM, engine, Book

app = flask.Flask(__name__)

# création de notre session (connection) à notre base de données...
# evite des conflits au niveau des connections simultannées
DBSession = sessionmaker(bind=engine)
# TOUT SE PASSE A TRAVERS DE CETTE VARIABLE
session = DBSession

@app.route("/")
@app.route("/books")
def get_books():
    # query la table definie par le ORM, et choppe toutes les valeurs
    session.query(BookORM).all()

    # retourne une reponse bidon, avec un code 200 (réussite)
    return flask.make_response("All good", 200)

@app.route("/books/add/<str:title>/<author>/<genre>")
def add_book(title: str, author, genre):
    
    new_book = Book(title, author, genre=genre)

    # do some processing on the book data

    # crée le mapping relationnel à partir de book
    orm = new_book.orm()

    # ajoute localement
    session.add(orm)

    # synchronise
    session.commit()

    return flask.make_response("Book added and saved", 200)

@app.route("/books/delete/<int:book_id>")
def add_book(book_id):
    # trouve le livre par id dans le ORM
    book_to_delete = session.query(BookORM).filter_by(id=book_id)

    # supprime cet element dans le ORM
    session.delete(book_to_delete)

    # synchronise
    session.commit()

    return flask.make_response("book deleted", 200)


if __name__ == "__main__":
    app.run(debug=True)
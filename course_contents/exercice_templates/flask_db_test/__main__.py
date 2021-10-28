
import flask

app = flask.Flask(__name__)

class Book:
    def __init__(
        self,
        title: str,
        author: str,
        isbn: str
    ):
        self._title = title,
        self._author = author,
        self._isbn = isbn

@app.route("/")
@app.route("/books")
def get_books():
    return flask.redirect(flask.url_for("dashboard"))

@app.route("/dashboard")
def login():
    return "test"

@app.errorhandler(404)
def not_found():
    """ Page not found. """
    return flask.make_response(flask.render_template("400.html"), 404)

@app.route("/books/new/", methods=['GET', 'POST'])
def add_books():
    if flask.request == 'POST':
        # si communication se passe via des formulaire (form) html
        title = flask.request.form['title']
        author = flask.request.form['author']
        isbn = flask.request.form['isbn']

        b = Book(title, author, isbn)
        return title+author+isbn
    else:
        # get extract vars
        # ajout via POSTMAN (logociel de interfacage http)
        return "none"

@app.route("/books/<int:book_id>/delete")
def del_books(book_id):
    """ deletes the book with the id from the database """
    print(book_id)
    return str(book_id)

@app.route("/books/edit/")
def edit_books():
    pass


if __name__ == "__main__":
    app.run(debug=True)
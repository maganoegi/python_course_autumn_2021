
# DEFINITION DES ROUTES ET VIEWS..
import flask

app = flask.Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/index")
def  home():
    """ definition of the ROOT route and the 
    associated behaviour """

# ROUTE HTTP METHODS...
# par defaut, flask travaille avec les methodes GET...
# pour travailler avec POST, faul le specifier.
@app.route('/api/v1/users/', methods=['GET', 'POST', 'PUT'])
def users():
    """ logic that allows us to return the users... """
    if flask.request == 'POST':
        # si communication se passe via des formulaires
        name = flask.request.form['name']
        age = flask.request.form['age']


@app.route('/user/[username]')
def profile(username):
    """ get a specific user """


@app.route('/[int:year]/[int:month]/[title]')
def article(year, month, title):
    """ reponse a une route dynamique -> 
    variables multiples"""

# ROUTE RESPONSES...
# il y a 3 types de reponses possibles:
    # Render Page Template
    # Créer un response object
    # Redirection à un autre vue



# RENDER PAGE TEMPLATE....
@app.route("/")
def home():
    """Serve homepage template

    Flask va regarder dans notre 'templates/' folder, 
    qui doit se trouver 
    a coté de notre __main__.py
    """
    return flask.render_template("index.html")

@app.route("/")
def home():
    """On peut aussi lui donner des variables...."""
    return flask.render_template(
        'index.html',
        title='Flask-Login.',
        body="You are now logged in!"
    )

# CREER UN RESPONSE OBJECT 
@app.route("/api/v2/test_response")
def users():
    """ Si on construit un endpoint purement informatif 
    (ou on cherche pas a retourner des pages) 
    nous allons alors construire des reponses"""

    headers = {"Content-Type": "application/json"}
    return flask.make_response(
        'My Processes Data',
        200,
        headers=headers
    )

# REDIRECTION ENTRE DES VIEWS
@app.route("/login")
def login():
    """ va nous rediriger vers dashboard.html 
    pour le login """

    return flask.redirect(flask.url_for('dashboard'))


# REQUEST OBJECT
""" 
    * request.method:
        POST, GET, PUT, DELETE
    * request.args : 
        des variables nommées
    * request.data :
        retourne le BODY qui  fait partie du message
    * request.form : 
        vous permet de travailler des formulaires
    * request.headers : 
        HTTP response headers
"""





# Error Handling
@app.errorhandler(404)
def not_found():
    """Page not found."""
    return flask.make_response(
        flask.render_template("404.html"),
        404
     )

@app.errorhandler(400)
def bad_request():
    """Bad request."""
    return flask.make_response(
        flask.render_template("400.html"),
        400
    )

@app.errorhandler(500)
def server_error():
    """Internal server error."""
    return flask.make_response(
        flask.render_template("500.html"),
        500
    )
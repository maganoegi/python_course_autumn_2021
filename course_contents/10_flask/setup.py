
# on import le module flask...
import flask

# annonce de la variable globale de l'application
app = flask.Flask(__name__)

@app.route('/')
def home():
    print("notre première route est definie")

if __name__ == '__main__':
    app.run(debug=True)


from server import app

@app.route("/")
def home():
    print("success")
    return "success"
from flask import Flask

app = Flask(__name__)
app.config['JSON_AS_SCII'] = False

@app.route("/primeiraapi")
def index():
    return "<h1>Your Api it's working...</h1>"

app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return "<h1>This is the main page.</h1>"



@app.route("/about")
def about():
    return render_template('index.html', name="whoooooooooop")
@app.route("/person/<lastname>")
def person(lastname=None):
    return render_template('person.html',
                           lastname = lastname
                           )

if __name__=="__main__":
    app.debug=True
    app.run() #This has to go at the end

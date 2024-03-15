from flask import Flask
app = Flask(__name__)

@app.route('/') # When user navigates to the home page url, do the following.
def hello_world():
    return 'Hello, World!'

@app.route("/bye") # Only gets called if the user goes to the bye webpage.
def say_bye():
    return "Bye"

if __name__ == "__main__":
    app.run()
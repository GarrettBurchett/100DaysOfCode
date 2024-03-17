from flask import Flask
app = Flask(__name__)

def make_bold(func):
    def wrapper():
        return '<b>' + func() + '</b>'
    return wrapper

def make_emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper

def make_underlined(func):
    def wrapper():
        return '<u>' + func() + '</u>'
    return wrapper

@app.route('/') # When user navigates to the home page url, do the following.
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>'\
           '<p>This is a paragraph.</p>'\
           '<img src="https://media.giphy.com/media/9aVfqdOyOtGGQ/giphy.gif">'

@app.route("/bye") # Only gets called if the user goes to the bye webpage.
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye"

@app.route("/username/<name>") # Uses whatever is typed in for <name> variable as the name value
def greet(name):
    return f"Hello {name}"

if __name__ == "__main__":
    app.run(debug=True) # Turns on debugging mode for the Flask server
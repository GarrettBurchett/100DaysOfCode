from flask import Flask
import random
app = Flask(__name__)

number = random.randint(0, 9)

@app.route('/')
def game_start():
    return '<h1>Guess a number between 0 and 9</h1>'\
           '<img src="https://media.giphy.com/media/l378khQxt68syiWJy/giphy.gif?cid=790b76112h1j9ksuzyc20c6ab7h4jw9qwsiho2ol1qyntjn9&ep=v1_gifs_search&rid=giphy.gif&ct=g">'

@app.route('/<int:num>')
def high_low(num):
    if int(num) == number:
        return '<h1 style="color: green">You guessed the number!</h1>'\
               '<img src="https://media.giphy.com/media/PS7d4tm1Hq6Sk/giphy.gif?cid=790b7611dddm22y54bu3zob972ygm6pj1988qv1wu22w2gin&ep=v1_gifs_search&rid=giphy.gif&ct=g">'
    elif int(num) < number:
        return '<h1 style="color: red">Too low, try again!</h1>'\
               '<img src="https://media.giphy.com/media/TgmiJ4AZ3HSiIqpOj6/giphy.gif?cid=790b76118wo61qkohv94vyob3wn7iejcoa0gbmnuodvn8qki&ep=v1_gifs_search&rid=giphy.gif&ct=g">'
    else:
        return '<h1 style="color: purple">Too high, try again!</h1>'\
        '<img src="https://media.giphy.com/media/l2YWy9pD8sZEUMF0s/giphy.gif?cid=790b7611amf6xfgdfxv0owxi9j72mtcsu74rb1qhg25om0rh&ep=v1_gifs_search&rid=giphy.gif&ct=g">'


if __name__ == "__main__":
    app.run(debug=True)
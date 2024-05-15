from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    year = datetime.date.today().year
    your_name = 'Garrett Burchett'
    return render_template('index.html', num=random_number, year=year, name=your_name)

@app.route('/guess/<name>')
def guess_age_and_gender(name):
    age_response = requests.get(f'https://api.agify.io?name={name}').json()
    guessed_age = age_response['age']
    gender_response = requests.get(f'https://api.genderize.io?name={name}').json()
    guessed_gender = gender_response['gender']
    return render_template('guess.html', name=name, gender=guessed_gender, age=guessed_age)

@app.route('/blog')
def blog():
    response = requests.get(' https://api.npoint.io/bef7a6652c0027296c26').json()
    return render_template('blog.html', posts=response)

if __name__ == '__main__':
    app.run(debug=True)
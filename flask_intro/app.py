from flask import Flask, render_template, request



import pandas as pd  
import numpy as np 
df = pd.DataFrame({'x': np.random.random(10),
'y': np.random.random(10)}).to_html()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', table = df)

@app.route('/hello')
def name():
    name = request.args.get('name')
    return render_template('hithere.html', name = name)

@app.route('/form', methods = ["GET", "POST"])
def formpage():
    if request.method == "POST":
        name = request.form.get('person')
        age = request.form.get('age')
        d = {'name': name, 'age': age}
        return render_template('submitted.html', name = d)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
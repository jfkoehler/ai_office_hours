from flask import Flask, render_template, request



import pandas as pd  
import numpy as np 
df = pd.DataFrame({'x': np.random.random(10),
'y': np.random.random(10)}).to_html()

#lookup the top 10 county's by state through cases in USA
def state_lookup(state):
  df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv')
  state_df = df.loc[df['state'] == state]
  state_df = state_df.groupby('county')[['cases', 'deaths']].sum()
  return state_df.nlargest(10, 'cases').plot(kind = 'bar')


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
        state = request.form.get('state')
        
        d = state_lookup(state)
        return render_template('submitted.html', state_table = d)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
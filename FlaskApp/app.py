from flask import Flask
from flask import render_template
import pandas as pd

#df = pd.read_csv('Dog_Names.csv')
#savePath = './templates/table.html'
#df.to_html(open(savePath, 'w'), index=False)

app = Flask(__name__)

@app.route("/gb")
def goodbye():
    return "GoodBye"

@app.route('/')
def hello(name=None):
    return render_template('table.html', name=name)


if __name__ == '__main__':
    app.run()

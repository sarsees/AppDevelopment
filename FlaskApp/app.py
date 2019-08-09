from flask import Flask
from flask import render_template
import pandas as pd
#import sqlite3
#from sqlalchemy import create_engine
#DATABASE = 'sqlite:////Volumes/Part810/NewsTool/p810.db'

#conn = create_engine(DATABASE)
#df = pd.read_sql_table("NLP_Articles", con=conn)
#conn.close()

df = pd.read_csv('Dog_Names.csv')
savePath = './templates/table.html'
html_table = df.to_html(index=False, table_id="demo")

app = Flask(__name__)

@app.route("/gb")
def goodbye():
    return "GoodByeShamefulManticor"

@app.route('/')
def hello(name=None):
    return render_template('table.html', name=name,html_table=html_table)


if __name__ == '__main__':
    app.run()

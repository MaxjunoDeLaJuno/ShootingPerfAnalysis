"""
main.py — Shooting Performance Analysis

Goal :
- Analyse shooting performance on a target in a shooting range
- Application with shooting template (rifle, distance, nb of shots)
- Compare each shooting sessions performances
- Display data with a graphical interface
"""
import sys
from datetime import datetime

import pandas as p
from dash import Dash, dcc, html

import sqlite3
from flask import g

sys.path.append("./src")
import ShootingPerf, ShootingSession

app = Dash(__name__)

CONFIG = {
    "app_name": "ShootingPerfAnalysis",
    "version": "0.1"
}

DATABASE = f"./databases/{CONFIG["app_name"]}.db"

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(exception=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

# get an object <ShootingData> from "./src/ShootingSession.py"
def getShootingData():
    pass
    
# get an object <ShootingPerf> from "./src/ShootingPerf.py"
def getShootingPerf():
    pass

# save the data <ShootingPerf> in "ShootingPerfAnalysis.db"
def saveShootingPerf():
    pass


# data from the shooting session
data = (


)

# html layout
app.layout = html.Div(

)

# # Test for db creation
with app.server.app_context():
    db = get_db()

if __name__ == "__main__":
    log(f"starting of {CONFIG['app_name']} v{CONFIG['version']}")
    

    app.run(debug=True) 

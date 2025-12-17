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



CONFIG = {
    "app_name": "ShootingPerfAnalysis",
    "version": "0.1"
}

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

# get an object <ShootingData> from "./src/ShootingSession.py"
def getShootingData():
    pass
    
# get an object <ShootingPerf> from "./src/ShootingPerf.py"
def getShootingPerf():
    pass

# write the object <ShootingPerf> in ""
def saveShootingPerf():
    pass


# data from the shooting session
data = (


)

app = Dash(__name__)

# html layout
app.layout = html.Div(

)

if __name__ == "__main__":
    log(f"starting of {CONFIG['app_name']} v{CONFIG['version']}")

    app.run(debug=True) 

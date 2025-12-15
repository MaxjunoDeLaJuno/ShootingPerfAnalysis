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

CONFIG = {
    "app_name": "ShootingPerfAnalysis",
    "version": "0.1"
}

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")


if __name__ == "__main__":
    log(f"starting of {CONFIG['app_name']} v{CONFIG['version']}")


    success = True

    if success:
        sys.exit(0)
    else:
        sys.exit(1)


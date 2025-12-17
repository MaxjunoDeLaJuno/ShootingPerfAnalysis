#!/bin/bash

set -e
SCRIPT_DIR=$(dirname $0)

# Pour checker si c'est la première fois que l'user execute le script
if [ ! -d "$SCRIPT_DIR/.venv" ]; then
  python3 -m venv $SCRIPT_DIR/.venv
  mkdir databases
  first_install=true
else
  first_install=false
fi

source $SCRIPT_DIR/.venv/bin/activate

if [ "$first_install" = true ]; then
    # pip install pandas
    pip install -r $SCRIPT_DIR/requirements.txt
fi

#flask --app $SCRIPT_DIR/app.py run
python $SCRIPT_DIR/app.py

deactivate

# Merci pour le script @Maxxavec2x 🙏
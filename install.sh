#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo -e "${RED}Datei als root ausführen!${NC}"
  exit
fi

apt update ||
apt install libglib2.0-dev || dnf install glib2-devel

mkdir -p ~/.local/bin/fitforfactory/.venv
python -m venv ~/.local/bin/fitforfactory/.venv

git clone https://github.com/Dennis-89/BodyCompositionScale2.git ~/.local/bin/fitforfactory/src/
~/.local/bin/fitforfactory/.venv/bin/pip install ~/.local/bin/fitforfactory/src
rm -r ~/.local/bin/fitforfactory/src
~/.local/bin/fitforfactory/.venv/bin/pip install -m requirements.txt
cp -r src/* ~/.local/bin/fitforfactory/
cp src/FitForFactory/Pictures/header.PNG ~/.local/bin/fitforfactory/
cp FitForFactory.desktop /usr/share/applications/FitForFactory.desktop

chown -c $USER /usr/share/applications/FitForFactory.desktop
chown -cR $USER ~/.local/bin/fitforfactory/

echo -e "${GREEN}Installation erfolgreich! Dieser Ordner kann gelöscht werden.${NC}"

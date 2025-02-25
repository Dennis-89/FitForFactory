#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

if [ "$EUID" -ne 0 ]
  then echo -e "${RED}Datei als root ausführen!${NC}"
  exit
fi

(apt update && install libglib2.0-dev) || dnf install glib2-devel

mkdir -p /usr/local/share/applications/fitforfactory/.venv
python3 -m venv /usr/local/share/applications/fitforfactory/.venv

git clone https://github.com/Dennis-89/BodyCompositionScale2.git /usr/local/share/applications/fitforfactory/src/
/usr/local/share/applications/fitforfactory/.venv/bin/pip install /usr/local/share/applications/fitforfactory/src
rm -r /usr/local/share/applications/fitforfactory/src
/usr/local/share/applications/fitforfactory/.venv/bin/pip install -r requirements.txt
cp -r src/FitForFactory/* /usr/local/share/applications/fitforfactory/
cp src/FitForFactory/Pictures/header.PNG /usr/local/share/applications/fitforfactory/
rm -r /usr/local/share/applications/fitforfactory/QtDesigner
cp FitForFactory.desktop /usr/share/applications/FitForFactory.desktop

chmod +x /usr/share/applications/FitForFactory.desktop

echo -e "${GREEN}Installation erfolgreich! Dieser Ordner kann gelöscht werden. Um einfach alle Dateien wieder zu löschen, die <uninstall.sh> nicht löschen.${NC}"

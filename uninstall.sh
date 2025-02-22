#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo -e "${RED}Datei als root ausführen!${NC}"
  exit
fi

rm -r /usr/local/share/applications/fitforfactory
rm /usr/share/applications/FitForFactory.desktop

echo -e "${GREEN}Alle Dateien gelöscht!${NC}"

#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"    # Path to the script

buildings_file="source_buildings.json"
events_file="source_events.json"
superusers_file="superusers.json"
technologies_file="source_technologies.json"

echo "This script is a shortcut to erase the game app database and create it anew with its initial fixtures."
echo

read -p "Do you really wish to erase the database? All data will be permanently lost. [yes|No] " -r
if [[ $REPLY =~ ^[Yy]es$ ]]; then
    rm "${SCRIPT_DIR}/"db.sqlite3
    rm "${SCRIPT_DIR}/"game/migrations/[0-9]*.py
    echo "Database deletion complete."
    echo
else
    echo "Database deletion cancelled."
    echo
fi

read -p "Do you wish to create an empty database? Fixtures may be loaded afterwards. [yes|No] " -r
if [[ $REPLY =~ ^[Yy]es$ ]]; then
    python "${SCRIPT_DIR}/"manage.py makemigrations
    python "${SCRIPT_DIR}/"manage.py migrate
    echo "Database creation complete."
    echo
else
    echo "Database creation cancelled."
    echo
fi

#python "${SCRIPT_DIR}/"manage.py flush
#echo

read -p "Do you wish to load the initial fixtures (not creating a database beforehand will result in an error)? [yes|No] " -r
if [[ $REPLY =~ ^[Yy]es$ ]]; then
    python "${SCRIPT_DIR}/"manage.py loaddata $events_file
    python "${SCRIPT_DIR}/"manage.py loaddata $superusers_file
    python "${SCRIPT_DIR}/"manage.py loaddata $technologies_file
    python "${SCRIPT_DIR}/"manage.py loaddata $buildings_file    # buildings come after technologies
    echo "Fixture load complete."
    #echo
else
    echo "Fixture load cancelled."
    #echo
fi
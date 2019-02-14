#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"    # Path to the script

INIT_FIXTURES_DIR="${SCRIPT_DIR}/game/init_fixtures"

BUILDINGS_FILE1="source_buildings_era1.json"
BUILDINGS_FILE2="source_buildings_era2.json"
EVENTS_FILE="source_events.json"
SUPERUSERS_FILE="superusers.json"
TECHNOLOGIES_FILE="source_technologies.json"

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
    python3 "${SCRIPT_DIR}/"manage.py makemigrations
    python3 "${SCRIPT_DIR}/"manage.py migrate
    echo "Database creation complete."
    echo
else
    echo "Database creation cancelled."
    echo
fi

#python3 "${SCRIPT_DIR}/"manage.py flush
#echo

read -p "Do you wish to load the initial fixtures (not creating a database beforehand will result in an error)? [yes|No] " -r
if [[ $REPLY =~ ^[Yy]es$ ]]; then
    python3 "${SCRIPT_DIR}/"manage.py loaddata "${INIT_FIXTURES_DIR}/"$EVENTS_FILE
    python3 "${SCRIPT_DIR}/"manage.py loaddata "${INIT_FIXTURES_DIR}/"$SUPERUSERS_FILE
    python3 "${SCRIPT_DIR}/"manage.py loaddata "${INIT_FIXTURES_DIR}/"$TECHNOLOGIES_FILE
    # buildings come after technologies
    python3 "${SCRIPT_DIR}/"manage.py loaddata "${INIT_FIXTURES_DIR}/"$BUILDINGS_FILE1
    python3 "${SCRIPT_DIR}/"manage.py loaddata "${INIT_FIXTURES_DIR}/"$BUILDINGS_FILE2
    echo "Fixture load complete."
    #echo
else
    echo "Fixture load cancelled."
    #echo
fi
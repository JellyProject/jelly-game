#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"    # Path to the script

buildings_file="buildings.json"
events_file="events.json"
technologies_file="technologies.json"

echo "This script is a shortcut to flush the game app database and fill it with its initial fixtures."
echo

python "${SCRIPT_DIR}/"manage.py flush
echo

read -p "Do you wish to load the fixtures (not flushing the database beforehand will result in an error)? [yes|No] " -r
#echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]es$ ]]; then
    python "${SCRIPT_DIR}/"manage.py loaddata $buildings_file
    python "${SCRIPT_DIR}/"manage.py loaddata $events_file
    python "${SCRIPT_DIR}/"manage.py loaddata $technologies_file
else
    echo "Fixture load cancelled."
fi

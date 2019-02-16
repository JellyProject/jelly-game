#Description

Jelly game -temporary name- is an online multiplayer game in which each player
leads a fictional country throughout the ages. The actions performed by a player
are expected to impact the economical, environmental and social standings of his
country, and eventually the world as a whole.
The game website is powered by a Django backend and a Javascript GUI. 

#Installation

**Clone the project**

`git clone https://github.com/JellyProject/jelly-game.git`

`git checkout master-dev`

##Back

**Requirements**

Make sure you have django, django-rest-framework, django-cors-headers and
django-extensions installed on your machine.

`pip3 install django django-rest-framework django-cors-headers django-extensions`

**Migrate the database**

`cd jelly-game/back/`

`python manage.py makemigrations`

`python manage.py migrate`

**Load initial fixtures**

`python manage.py loaddata game/init_fixtures/source_events_era1.json game/init_fixtures/source_events_era2.json game/init_fixtures/source_technologies.json game/init_fixtures/source_buildings_era1.json game/init_fixtures/source_buildings_era2.json`

**Run server**

`python manage.py runserver`

##Front

**Requirements**

You will need an up-to-date version of nodejs to run this project. Using nvm
may help for this.

The axios package is also needed.

`npm install axios` 

**Install dependencies**

`cd ../front`

`npm install`

**Run development server**

`npm start`

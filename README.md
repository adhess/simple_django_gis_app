# Introduction
This project is a Python Engineer Coding Test provided by mozio.

# Database structure
```
         1   *             1   *
Provider ----- ServiceArea ----- Coordinate
```

A Provider have multiple ServiceArea.

Each ServiceArea has multiple Coordinates to make the Polygon.

The order of insertion in database for coordinates defines how we draw the polygon. 
# Deployment
This code is deployed on Heroku.

You can access the application using [this link](https://mozio-gis.herokuapp.com/)

## Install dependency
```
pip install pipenv
pipenv install
pipenv shell
```

## Migrate database
```
python3 manage.py makemigrations
python3 manage.py migrate
```
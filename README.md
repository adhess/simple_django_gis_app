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

# APIs
#### create, insert, delete and update providers, service_areas and coordinate:
```    
    https://mozio-gis.herokuapp.com/api/provider/
    https://mozio-gis.herokuapp.com/api/service_area/
    https://mozio-gis.herokuapp.com/api/coordinate/
```
#### retrieve service areas by provider Id:
```    
    https://mozio-gis.herokuapp.com/api/service_areas_by_provider_id/?provider_id=1
```
#### retrieve coordinates by service areas Id:
```    
    https://mozio-gis.herokuapp.com/api/coordinates_by_service_area/?service_area_id=2
```

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
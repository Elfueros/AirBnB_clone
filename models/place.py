#!/usr/bin/python3
"""place : Defines class Place that derives from BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Definition of Place that inherits from Basrmodel
    Attributes:
        /* public class attributes */
        city_id (str) : id of a corresponding City object
        user_id (str) : id of a corresponding User object
        name (str) : name of the place
        description (str) : description of the place
        number_rooms (int) : number of rooms in place
        number_bathrooms (int) : number of bathrooms in place
        max_guest (int) : maximum number of guests accepted
        price_by_night (int) : price of place by night
        latitude (float) : latitude of place
        longitude (float) : longitude of place
        amenity_ids (list of str) : id of a corresponding Amenity obect
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

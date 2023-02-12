from models.base_model import BaseModel


class Place(BaseModel):
    """Place class"""
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

    def __init__(self, *args, **kwargs):
        """Instantiation of Place"""
        super().__init__(self, *args, **kwargs)

    def __str__(self):
        """String representation of Place"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Update the public instance attribute updated_at"""
        super().save(self)

    def to_dict(self):
        """Returns a dictionary containing all keys/values"""
        return super().to_dict(self)

    def delete(self):
        """Delete the current instance from the storage"""
        super().delete(self)


if __name__ == "__main__":
    pass

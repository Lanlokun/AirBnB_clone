from models.base_model import BaseModel

class User(BaseModel):
    """User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Instantiation of User"""
        super().__init__(self, *args, **kwargs)

    def __str__(self):
        """String representation of User"""
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

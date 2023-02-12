import json


class FileStorage:
    """
    This class serializes instances to a JSON file and deserializes
    JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def user(self):
        return self.__user

    def place(self):
        return self.__place

    def state(self):
        return self.__state

    def city(self):
        return self.__city

    def amenity(self):
        return self.__amenity

    def review(self):
        return self.__review

    def placeamenity(self):
        return self.__placeamenity

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                new_dict = json.load(f)
            for key, value in new_dict.items():
                FileStorage.__objects[key] = eval(value["__class__"])(**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):

        """Delete obj from __objects if it’s inside"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]
                self.save()

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()


if __name__ == "__main__":
    pass

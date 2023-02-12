class FileStorage:
    """This class serializes instances to a JSON file and deserializes
    JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return Storage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        Storage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in Storage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(Storage.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)"""
        try:
            with open(Storage.__file_path, "r") as f:
                new_dict = json.load(f)
            for key, value in new_dict.items():
                Storage.__objects[key] = eval(value["__class__"])(**value)
        except:
            pass
    
    def delete(self, obj=None):

        """Delete obj from __objects if it’s inside"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            if key in Storage.__objects:
                del Storage.__objects[key]
                self.save()
    
    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()

if __name__ == "__main__":
    pass
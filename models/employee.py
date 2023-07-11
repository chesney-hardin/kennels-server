class Employee():
    """this class will serve as a blueprint for all objects that get created for an employee
    """
    def __init__(self, id, name, address, location_id):
        self.id = id
        self.name = name
        self.address = address
        self.location_id = location_id
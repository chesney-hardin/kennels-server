class Customer():
    """this class will serve as a blueprint for all objects that get created for a customer.
    """
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
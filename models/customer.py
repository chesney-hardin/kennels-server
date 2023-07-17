class Customer():
    """this class will serve as a blueprint for all objects that get created for a customer.
    """
    def __init__(self, id, name, address, email = "", password = ""):
        self.id = id
        self.name = name
        self.address = address
        self.email = email
        self.password = password
        
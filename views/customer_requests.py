CUSTOMERS = [
    {
        "id": 1,
        "name": "Ryan Tanay"
    }
]

def get_all_customers():
    """function to return all customer data
    """
    return CUSTOMERS

def get_single_customer(id):
    """function to find single customer
    """
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] ==id:
            requested_customer = customer

    return requested_customer

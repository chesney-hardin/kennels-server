EMPLOYEES = [
    {
        "id": 1,
        "name": "Jenna Solis"
    }
]

def get_all_employees():
    """function to return all employee data
    """
    return EMPLOYEES

def get_single_employee(id):
    """function to find single employee
    """
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] ==id:
            requested_employee = employee

    return requested_employee

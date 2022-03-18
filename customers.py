"""Customers at Ubermelon."""


class Customer(object):
    """Ubermelon customer."""

    # TODO: need to implement this
    def __init__(self,
                 first_name,
                 last_name,
                 email,
                 password
                 ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        
    def __repr__(self):
        return f"<Customer: {self.first_name},{self.last_name},{self.email},{self.password}>"
    
def read_customers_from_file(filepath):
    
    customers = {}
    
    with open(filepath) as file:
        for line in file:
            (first_name,
             last_name,
             email,
             password) = line.strip().split("|")
            
            customers[email] = Customer(first_name,
                                        last_name,
                                        email,
                                        password)
    
    return customers
            
def get_by_email(email):
    if email in customers:
        return customers[email]
    else: return False

customers = read_customers_from_file("customers.txt")
customers = []
class Customer():

    def __init__(self, customer_id, name, pnr):
        global customers
        self.customer_id = customer_id
        if str(customer_id) not in str(customers):
            self.name = name
            self.pnr = pnr
            customers.append(customer_id)
        else:
            self.duplicate_customer_id()
 
    def change_name(self, new_name):
            self.name = new_name
        
    def show_customer_info(self, pnr):
        print("Customer name: ", self.name)
        print(" ")
        print("Customer_id: ", self.customer_id)
        print(" ")
        print("Customer_pnr: ", self.pnr)
        
    def get_customer(self):
        customer = str(self.customer_id) + ":" + self.name + ":" + str(self.pnr) + ":"
        return customer 
    
    def duplicate_customer_id(self):
        print("This Id is already used!")
        return False
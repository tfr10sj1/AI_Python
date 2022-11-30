from Account import Account as ac
account_obj = ""
class Customer():

    def __init__(self, customer_id, name, pnr):
        self.customer_id = customer_id
        self.name = name
        self.pnr = pnr
     
    def add_account(self, account_nbr, balance):
        global account_obj
        account_obj += ac(account_nbr, balance).get_account()
        
    def change_name(self, new_name):
            self.name = new_name
        
    def show_customer_info(self, pnr):
        print("Customer name: ", self.name)
        print(" ")
        print("Customer_id: ", self.customer_id)
        print(" ")
        print("Customer_pnr: ", self.pnr)
        
    def get_customer(self):
        global account_obj
        customer = str(self.customer_id) + ":" + self.name + ":" + str(self.pnr) + ":"
        if account_obj != "":
            customer += account_obj
        return customer 